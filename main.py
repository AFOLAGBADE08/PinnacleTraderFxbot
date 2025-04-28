import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Get the bot token from environment variable
TOKEN = os.getenv('BOT_TOKEN')

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    # Define the reply keyboard
    keyboard = [['Payment Information', 'VIP Channel Access', 'Contact Support']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(f"Hello {user.first_name}!\n\nWelcome to Pinnacle Trader FX.\n\nPlease choose an option below:", reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == 'Payment Information':
        update.message.reply_text("To join Pinnacle Trader FX VIP:\n\nBank Transfer:\nBank Name: [Your Bank Name]\nAccount Name: [Your Account Name]\nAccount Number: [Your Account Number]\n\nCrypto Payment:\nBTC Wallet: [Your Bitcoin Wallet Address]\n\nAfter payment, send a screenshot here. We will verify and add you.")

    elif text == 'VIP Channel Access':
        update.message.reply_text("After successful payment confirmation, you will be given exclusive access to our VIP signals channel.\n\nPlease complete your payment first.")

    elif text == 'Contact Support':
        update.message.reply_text("For support, kindly message our admin:\n\n@YourTelegramUsername\n\nWe are here to help you!")

    else:
        update.message.reply_text("Please choose an option from the keyboard.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers for /start and regular messages
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

# Run the bot
if name == 'main':
    main()
