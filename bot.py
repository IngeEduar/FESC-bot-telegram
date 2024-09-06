from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram.ext import CallbackContext
import logging

from app.services.MenuService import MenuService
from app.services.QuestionService import QuestionService

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

menuService = MenuService()
menuService.pushMenu()

questionService = QuestionService()
questionService.pushQuestions()

# Función para el comando /start
async def start(update: Update, context: CallbackContext):
    menuInit = menuService.getMenuById(0)
    question = menuInit.get_question()

    keyboard = [[InlineKeyboardButton(q.get_question(), callback_data=str(q.get_question()))] for q in question.get_options()]

    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = question.get_response()

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    response = questionService.getQuestionByQuestion(query.data)

    await query.answer()

    if response.get_options():
        keyboard = [[InlineKeyboardButton(q.get_question(), callback_data=str(q.get_question()))] for q in response.get_options()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(response.get_response(), reply_markup=reply_markup)
    else:
        await query.message.reply_text(response.get_response())


# Función para manejar mensajes que no son comandos
async def handle_message(update: Update, context: CallbackContext):
    message_text = update.message.text

    response = questionService.getQuestionByQuestion(message_text)
    options = response.get_options() 

    if options:
        keyboard = [[InlineKeyboardButton(q.get_question(), callback_data=str(q.get_question()))] for q in options]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(response.get_response(), reply_markup=reply_markup)
    else:
        await update.message.reply_text(response.get_response())

if __name__ == '__main__':
    application = ApplicationBuilder().token('6926738487:AAGg9bzg33Xene7dPOVdB3wyuKOhl9eeEf8').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button, pattern='^(?!\/start).*$'))  # Manejar preguntas frecuentes y submenús
    #application.add_handler(CallbackQueryHandler(submenu_button, pattern='.*'))  # Manejar submenú
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    webhook_url = 'https://c295-38-252-236-215.ngrok-free.app'

    # Configurar el webhook
    application.bot.set_webhook(url=webhook_url)

    # Iniciar el bot
    application.run_webhook(
        listen='0.0.0.0',
        port=5002,
        url_path='',
        webhook_url=webhook_url,
        drop_pending_updates=True
    )
