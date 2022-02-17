import os
import telebot


bot = telebot.TeleBot("5149509357:AAGbNSL98Q7YdFJbvs5KWH5WaHUQ33Wtoc8")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm SLBOTINFOBOT")


@bot.message_handler(commands=["info"])
def send_message(message):
  bot.send_message(message.chat.id, "contact me @sitedown")



bot.polling()
