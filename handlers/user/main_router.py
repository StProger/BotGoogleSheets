from aiogram import Router

from .start import start_router
from .anketa_router import anketa_router

main_router_user = Router()

main_router_user.include_routers(
    start_router,
    anketa_router
)
