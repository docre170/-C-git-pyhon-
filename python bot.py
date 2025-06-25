from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Fonction pour gérer la commande /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bonjour! Je suis votre bot.')

# Fonction pour gérer les messages texte
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Remplacez 'YOUR_TOKEN' par le token que vous avez obtenu de BotFather
    updater = Updater("7641075475:AAF2beDVrEYYD24srkgFCIcDCOuy5RhfRWw")

    # Obtenir le dispatcher pour enregistrer les gestionnaires
    dispatcher = updater.dispatcher

    # Enregistrer les gestionnaires de commandes et de messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Démarrer le bot
    updater.start_polling()

    # Exécuter le bot jusqu'à ce qu'il soit arrêté
    updater.idle()

if __name__ == '__main__':
    main()