from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup


async def get_news():
    list_news = []

    r = requests.get('https://vnexpress.net/')
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')

    mydivs = soup.find_all('h3', {'class': 'title-news'}) # find all h3 tag have classname: title-news
    # print(len(mydivs)) #22 news

    # duyệt qua từng news:
    for new in mydivs:
        newdict = {}
        newdict['link'] = new.a.get('href')
        newdict['title'] = new.a.get('title')
        list_news.append(newdict)
        return list_news
        # #lấy text trong thẻ a
        # print(new.a.text)
        # print(new.a.get('href'))  # get attribute 'href' link from tag 'a'


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text(f'Hello AI Engineer {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = get_news()
    str1 = ""
    for item in data:
        str1 += item["title"]+ "\n"
    update.message.reply_text(f'{str1}')
        # await update.message.reply_text(f'{item["link"]}')
    # await update.message.reply_text(f'tin tức mới nhất\n {data[0]}')



app = ApplicationBuilder().token("5900003013:AAFg5uJV49FdgPuOzPo8nqXVEQVn_VPDwTo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news)) # lệnh news; function news

app.run_polling()
