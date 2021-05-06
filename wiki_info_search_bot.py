from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from wiki import search_wiki


TOKEN = "1721099482:AAHyZurvhmP7rHx7541uetKil6v5Y2axTII"

def wiki(update, context):
    word = (update.message.text).lower()
    update.message.reply_text("Идет поиск...")
    a = search_wiki(word)
    if a == []:
        update.message.reply_text("Запрос в википедии не найден")
    else:
        response, url = a
        update.message.reply_text(response+url)





def start(update, context):
    update.message.reply_text("Пртвет! я wiki_info_search_bot\nЯ могу найти информацию в википедии\nЕсли не знаешь как пользоваться ботом напиши: /help")



def help(update, context):
    update.message.reply_text("Напиши что-нибудь и я найду информацию в википедии")




def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, wiki))
    updater.start_polling()
    updater.idle()


main()
