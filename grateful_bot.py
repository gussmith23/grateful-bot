#import urllib2
import json
import telegram
import random
  
bot = telegram.Bot(token='139221176:AAEjiPC22KVRF48oSjIhrLOTL_86G3s4Zks')
print(bot.getMe())

last_update = 0 if len(bot.getUpdates()) < 1 else bot.getUpdates()[-1]['update_id']

good_words = open('positive words.txt','r').read().split('\n')
print(good_words)

thanks_strings = ['thanks','thank']
thanks_reply_strings = ['thanks','thank you', 'thanks :)', 'thank you!']
positive_reply_strings = ['stay positive!','good job!', 'nice!']

# How often should we send a reply to a positive message?
reply_percentage = 0.2;

def onUpdate(update):

  text = update['message']['text'].lower()
  chat_id = update['message']['chat']['id']
  message_id = update['message']['message_id']

  # If the message is direct
  if text.find('@grateful_bot') != -1:
    
    # Search for a thank you
    thanked = False;
    for thanks_string in thanks_strings:
      if thanks_string in text: thanked = True
      
    # If thanked
    if thanked:
      bot.sendMessage(chat_id = chat_id,text = random.choice(thanks_reply_strings),reply_to_message_id=message_id)
      
  
  # Else look for positive words
  else:
    found_good_word = False
    for good_word in good_words:
      if good_word in text: 
        found_good_word = True
        break
    
    # If we found a positive word, send a nice message back
    if found_good_word:
      if(random.random() < reply_percentage): 
        bot.sendMessage(chat_id = chat_id,text = random.choice(thanks_reply_strings+positive_reply_strings),reply_to_message_id=message_id)
  
    
  return

while True:
  for update in bot.getUpdates(offset=last_update):
    last_update = update['update_id'] + 1
    print("New last update id:")
    print(last_update)
    print(update)
    onUpdate(update)
    

