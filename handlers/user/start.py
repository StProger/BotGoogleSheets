from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards import menu

start_router = Router()


@start_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()

    text = "Привет/Салют, это Академия нейросетей The Founder!\n" \
           "Каждую неделю мы проводим живые тех.разборы ИИ-стартапов.\n" \
           "Их еще нет в РФ, но они уже подняли инвестиции и их срочно нужно копировать!\n\n" \
           "Показывая, как копировать/воссоздать их ИИ-технологию, мы обучаем нейросетям с нуля.\n" \
           "Также в этом канале ты получишь бесплтаные уроки по Питону с обратной связью кураторов.\n" \
           "Подробные разборы задач с собеседований в ТОП-5 IT-компаний РФ  (Google, Yandex etc.)\n\n" \
           "Если хочешь присоединиться к нам, пожалуйста, ответь на вопросы анкеты участника стартап-клуба.\n" \
           "Это позволит нам понять твой уровень и правильно подобрать мероприятие.\n" \
           "Затем наш бот отправит тебе уроки и пригласит на следующий живой разбор.\n\n" \
           "Нажимай кнопку \"Начать\" внизу 👇🏻"

    await message.answer(text=text,
                         reply_markup=menu.get_button_start())

