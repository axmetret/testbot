#Test new telebot
#!/bin/python
import telepot
token = ''
TelegramBot = telebot.Bot(token)
#
print TelegramBot.getMe()
#
print TelegrarmBot.getUpdates()

