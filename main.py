import telepot

token = '838033724:AAG0Mafn_anbMPfW871LGZ_wdHHIhpgR0ys'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getUpdates())
