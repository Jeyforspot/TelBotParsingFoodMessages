from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from tgbot.config import load_config
from tgbot.handlers import routers_list
from tgbot.infrastructure.db import sql_start
from tgbot.services import broadcaster

config = load_config(".env")
# Webserver settings
# bind localhost only to prevent any external access
# WEB_SERVER_HOST = "::"
WEB_SERVER_HOST = "0.0.0.0"
# Port for incoming request from reverse proxy. Should be any available port
# WEB_SERVER_PORT = 8350
WEB_SERVER_PORT = 8080

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = "/bot/"
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = ""
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
# BASE_WEBHOOK_URL = "https://foodforvadia.alwaysdata.net/"
BASE_WEBHOOK_URL = "https://947d-176-100-4-97.ngrok.io"

async def on_startup(bot: Bot):
    admin_ids = config.tg_bot.admin_ids
    sql_start()
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)
    await broadcaster.broadcast(bot, admin_ids, "Бот був запущений")


def main():
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher()
    dp.startup.register(on_startup)

    dp.include_routers(*routers_list)

    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
