from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from google_sheets import GoogleSheet

anketa_router = Router()


class SAnketa(StatesGroup):

    get_name = State()
    get_city = State()
    get_level_neuro_network = State()
    get_skills_python = State()
    get_free_lessons = State()
    get_solve = State()
    get_actual_topic = State()
    get_kind_work = State()
    get_salary = State()
    get_goals = State()
    get_phone = State()


@anketa_router.callback_query(F.data == "start_anketa")
async def get_name(callback: types.CallbackQuery, state: FSMContext):

    await state.set_state(SAnketa.get_name)

    await callback.message.answer("Как тебя зовут?")
    await callback.answer()


@anketa_router.message(SAnketa.get_name)
async def get_city(message: types.Message, state: FSMContext):

    await state.update_data(name=message.text)
    await state.set_state(SAnketa.get_city)
    await message.answer("Из какого ты города (региона)?")


@anketa_router.message(SAnketa.get_city)
async def get_level_neuro_network(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(SAnketa.get_level_neuro_network)
    await message.answer("Изучал ли уже нейросети? Где и какой уровень?")


@anketa_router.message(SAnketa.get_level_neuro_network)
async def get_skills_python(message: types.Message, state: FSMContext):
    await state.update_data(level_neuro_network=message.text)
    await state.set_state(SAnketa.get_skills_python)
    await message.answer("Какой у тебя уровень питон?")


@anketa_router.message(SAnketa.get_skills_python)
async def get_free_lessons(message: types.Message, state: FSMContext):
    await state.update_data(skills_python=message.text)
    await state.set_state(SAnketa.get_free_lessons)
    await message.answer("Хотел бы пройти бесплатные уроки по питону для новичков?")


@anketa_router.message(SAnketa.get_free_lessons)
async def get_solve(message: types.Message, state: FSMContext):
    await state.update_data(free_lessons=message.text)
    await state.set_state(SAnketa.get_solve)
    await message.answer("Присылать ли тебе разборы задач с собеседований (Google, Yandex etc.)? ")


@anketa_router.message(SAnketa.get_solve)
async def get_actual_topic(message: types.Message, state: FSMContext):
    await state.update_data(get_solve=message.text)
    await state.set_state(SAnketa.get_actual_topic)
    await message.answer("Актуальна ли для тебя обучение по теме разработки нейросетей?")


@anketa_router.message(SAnketa.get_actual_topic)
async def get_work(message: types.Message, state: FSMContext):
    await state.update_data(actual_topic=message.text)
    await state.set_state(SAnketa.get_kind_work)
    await message.answer("Где и кем ты работаешь или чем занимаешься?")


@anketa_router.message(SAnketa.get_kind_work)
async def get_salary(message: types.Message, state: FSMContext):
    await state.update_data(kind_work=message.text)
    await state.set_state(SAnketa.get_salary)
    await message.answer("Какой у тебя уровень дохода сейчас?")


@anketa_router.message(SAnketa.get_salary)
async def get_aims(message: types.Message, state: FSMContext):
    await state.update_data(salary=message.text)
    await state.set_state(SAnketa.get_goals)
    await message.answer("Какие перед тобой стоят профессиональные цели применительно к ИИ?")


@anketa_router.message(SAnketa.get_goals)
async def get_number(message: types.Message, state: FSMContext):
    await state.update_data(goals=message.text)
    await state.set_state(SAnketa.get_phone)
    await message.answer("Твой мобильный номер телефона?")


@anketa_router.message(SAnketa.get_phone)
async def get_number(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()

    # Записываем данные в гугл таблицу
    sheets = GoogleSheet()
    await sheets.insert_data(data=data)

    await message.answer("Данные сохранены")
    await state.clear()

