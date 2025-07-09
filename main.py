from telegram.ext import Updater, MessageHandler, Filters

import os

# Получаем токен из переменных окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")

def reply(update, context):
    user_message = update.message.text
    update.message.reply_text(f"Вы сказали: {user_message}")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
