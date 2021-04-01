# -*- coding: utf-8 -*-

import telebot  # Connect with Telegram
import time     # Sleep script
from GoogleNews import GoogleNews   # Get Google News
import json     # Read JSON Files
from datetime import datetime   # Get current time


token = json.loads(open("token.json").read()) # Get the token in "token.json"
bot = telebot.TeleBot(token['token']) # Load bot with token

@bot.message_handler(commands=['help']) # Help command
def main(message):
    bot.reply_to(message, "❓️ Cosa può fare questo bot?\n➡️ Inoltra gli ultimi annunci e le ultime notizie riguardanti il Superbonus Casa 110%\n❓️ Come posso fermare l'invio delle notizie?\n➡️ Ti basta arrestare e bloccare il bot cliccando sul menù in alto a destra\n❓️ Chi è lo sviluppatore del bot?\n➡️ https://t.me/diskxo ")



@bot.message_handler(commands=['start']) # Start command
def main(message):
    chatid = message.chat.id
    print("🆕 L'id utente: " + str(chatid) + " ha appena avviato il bot!")
    bot.reply_to(message, "Benvenuto nel bot Telegram dedicato al bonus Casa 110%! 🏠🎉\nQui riceverai tutti gli aggiornamenti in tempo reale sul Bonus. 📰\nUsa /help per maggiori informazioni sul bot. 🙋")
    
    while True:
        now = datetime.now()    
        current_time = now.strftime("%H:%M:%S")  # Get time  

        print("--- ⚠️ Controllo nuove notizie alle ore: " + current_time)  # Print new scan
            
        googlenews = GoogleNews(lang='it')
        googlenews.search('Bonus 110')
        pages_range = range(7)
        for n in pages_range:
            googlenews.get_page(n)

        links = googlenews.get_links()   # Get links of news
        var_lettura = open("newsdb.txt", "r").read()
        array = var_lettura.split('\n')
        
        for link in links:
            var_lettura = open("newsdb.txt", "r").read()
            array = var_lettura.split('\n')
                            
            if link in array:
                pass
                
            else:
                print("⚠️🏠Nuova notizia sul Superbonus Casa 110%!\n" + link) 
                bot.send_message(chatid, "⚠️🏠Nuova notizia sul Superbonus Casa 110%!\n" + link)
                
                var_scrittura = open("newsdb.txt", "a")
                var_scrittura.write(link + '\n')
                var_scrittura.close()
            
                
        print("--- ⚠️ Finito controllo in data: " + current_time)    # Print scan refresh
        time.sleep(10)    


print("Bot Online! 🚀🏠")
bot.polling()