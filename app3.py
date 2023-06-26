
import telebot
import requests


# res = requests.post('localhost:5000/api')
url = 'http://localhost:5000/api'


TOKEN = '6153803955:AAHgiy2476feLE1SrMTl7RKM_zCv_q-1ftw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	
	print()
	user = message.from_user.username
	prompt = message.text
	myobj = {
	"user_id":user,
	"prompt": prompt
	}
	x = requests.post(url, json = myobj)
	ans = x.json()
	print("GPT ANSWER : ",ans)
	bot.reply_to(message, ans['message']['content'])

bot.infinity_polling()