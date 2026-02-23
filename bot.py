import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# ТОКЕН ОТ BOTFATHER — вставь свой реальный токен
TOKEN = "8307551404:AAGFeY0OBS3-w1-TjRoFzPxyIy6yaADaDtM"

# Сайт ПК-клуба — заменяй на реальный адрес
SITE_URL = "https://wagonless-terry-spongily.ngrok-free.dev" # если сайт в интернете, то https://example.com

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 Перейти на сайт OneTap",
                url=SITE_URL
            )
        ],
        [
            InlineKeyboardButton(
                "📋 Посмотреть меню",
                callback_data="show_menu"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {user.first_name}! 🔥\n"
        "Это бот ПК-клуба OneTap в нукусе.\n"
        "Здесь можно быстро забронировать мощный ПК.\n\n"
        "Нажми кнопку ниже, чтобы перейти на сайт:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "show_menu":
        await query.message.reply_text(
            "Меню:\n"
            "1. Перейти на сайт\n"
            "2. Свободные ПК\n"
            "3. Мои брони\n"
            "4. Профиль\n\n"
            "Выбери номер или напиши /start"
        )
    else:
        await query.message.reply_text("Функция в разработке...")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Ты написал: {update.message.text}\n\n"
        "Напиши /start чтобы увидеть меню и кнопку сайта"
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот OneTap PC Club запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()