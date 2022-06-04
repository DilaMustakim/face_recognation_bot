from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from face_compare import cmp_photo

ADMIN_ID = 1292625070
TOKEN = "5230567040:AAHb5uvJZDFsfqaEuksW6vGSOWGBS2p4Quo"


def start_func(update, context):
    update.message.reply_photo(
        photo=open('photos/Hello.jpg', 'rb'),
        caption="Hello!!!"
    )
    update.message.reply_text(text="Rasm tashlang!")


def photo_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download(f'new_photos/student.jfif')
    txt = cmp_photo()
    update.message.reply_text(text=txt)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

    updater.start_polling()
    updater.idle()


main()
