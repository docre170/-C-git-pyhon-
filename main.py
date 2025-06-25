from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bonjour! Je suis votre bot.')

def main() -> None:
    # Remplacez 'YOUR_TOKEN_HERE' par votre token de bot
    updater = Updater("7641075475:AAF2beDVrEYYD24srkgFCIcDCOuy5RhfRWw")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    # Démarrer le bot
    updater.start_polling()

    # Exécuter le bot jusqu'à ce qu'il soit arrêté
    updater.idle()

if __name__ == '__main__':
    main()