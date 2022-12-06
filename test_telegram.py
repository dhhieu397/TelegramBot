
import telegram
my_token = "5857410606:AAH3fvyS-JxjEYWo9p0nB8HMYIZ1P0Kcwpo"

#tạo bot
bot = telegram.Bot(token=my_token)
#gửi thử text message
bot.sendMessage(chat_id="1173569762", text="Gửi từ pycharm, xin vui lòng đợi khi có cảnh báo!!")
bot.sendPhoto(chat_id="1173569762", photo= open("but.png","rb"), caption="Có nặc danh, hãy vui lòng check lại và không"
                                                                         "cung cấp code cho ai... ")