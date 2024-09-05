from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram.ext import CallbackContext
import logging

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define las respuestas de las preguntas frecuentes y sus submenús
FAQS = {
    "¿Cuál es tu nombre?": {
        "res": "Soy un bot de asistencia.",
        "submenu": {
            "Nombre completo": "Mi nombre completo es Bot Assist.",
            "¿Por qué me preguntas?": "Solo para conocerte mejor."
        }
    },
    "¿Cómo puedo contactarte?": {
        "res": "Puedes escribirme por aquí.",
        "submenu": {
            "Soporte técnico": "Nuestro soporte técnico está disponible 24/7.",
            "Ventas": "Puedes contactar con ventas al correo ventas@example.com."
        }
    },
    "¿Cuál es el horario de atención?": {
        "res": "Atendemos de lunes a viernes de 9 AM a 6 PM.",
        "submenu": {
            "Vacaciones": "Estamos cerrados durante las vacaciones de diciembre.",
            "Feriados": "Atendemos en los días feriados nacionales."
        }
    }
}

DEFAULT_RESPONSE = "Lo siento, no tengo la respuesta a esa pregunta."

# Función para el comando /start
async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton(question, callback_data=question)] for question in FAQS.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = "¡Hola! Soy tu asistente virtual. Elige una de las siguientes preguntas para obtener una respuesta."
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Función para manejar los botones de respuestas y submenús
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    question = query.data
    response_info = FAQS.get(question, {}) 
    response = response_info.get("res", DEFAULT_RESPONSE)
    submenu = response_info.get("submenu", {})

    # Enviar la respuesta correspondiente
    await query.answer()
    await query.message.reply_text(response)

    # Mostrar el submenú si existe
    if submenu:
        keyboard = [[InlineKeyboardButton(option, callback_data=f"{question}|{option}")] for option in submenu.keys()]
        reply_markup = InlineKeyboardMarkup(keyboard)
        submenu_message = "Elige una opción para más detalles."
        await query.message.reply_text(submenu_message, reply_markup=reply_markup)

# Función para manejar los botones de submenú
async def submenu_button(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data.split('|', 1)
    parent_question = data[0]
    option = data[1]
    submenu = FAQS.get(parent_question, {}).get("submenu", {})
    response = submenu.get(option, DEFAULT_RESPONSE)

    # Enviar la respuesta correspondiente del submenú
    if response:
        await query.answer()
        await query.message.reply_text(response)

# Función para manejar mensajes que no son comandos
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = FAQS.get(user_message, {}).get("res", DEFAULT_RESPONSE)
    await update.message.reply_text(response)

# Función principal
if __name__ == '__main__':
    application = ApplicationBuilder().token('6926738487:AAGg9bzg33Xene7dPOVdB3wyuKOhl9eeEf8').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button, pattern='^(?!\/start).*$'))  # Manejar preguntas frecuentes y submenús
    application.add_handler(CallbackQueryHandler(submenu_button, pattern='.*'))  # Manejar submenú
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    webhook_url = 'https://af92-38-252-236-215.ngrok-free.app'

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
