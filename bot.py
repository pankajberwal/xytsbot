import json 
import requests
import ytsmovies
from dbhelper import DBHelper
import time

db=DBHelper()

TOKEN = "618142674:AAGrzlf2Dap6iLw-2stObBad5tDlLGzy59M"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url=URL+"getupdates?timeout=100"
    if offset:
        url=url+"&offset={}".format(offset)
    js=get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    

'''text, chat = get_last_chat_id_and_text(get_updates())
last_movie_container=set([""])
movie_container=ytsmovies.get_list()
latest_movies=movie_container.difference(last_movie_container)
for movie in movie_container:
	send_message(movie, chat)'''

def send_movie(latest_movie_list):
	id_list=db.get_id()
	for ID in id_list:
		send_message(latest_movie_list,ID)



def handle_updates(updates):
	for update in updates['result']:
		text=update['message']['text']
		chat_id=update['message']['chat']['id']
		user_name=update['message']['chat']['username']
		id_list=db.get_id()
		if text =='/start':
			starter_message='Helloo {} , Some amazing movies HD torrents updates you can get here.If you don\'t want these updates just send /stop message.'.format(user_name) 
			send_message('starter_message',chat_id)
			db.add_id(chat_id,user_name)

		elif text =='/stop':
				db.delete_id(chat_id)

def handle_movies(latest_movie_list):
	db.delete_movie()
	for latest_movie in latest_movie_list:
		db.add_movie(latest_movie)
 
		

def main():
	db.setup()
	last_update_id=None
	last_movie_list=set([""])
	movies=set([""])

	while True:
		updates=get_updates(last_update_id)
		movie_list=ytsmovies.get_list()
		if len(updates["result"]) > 0:
        	last_updateid=get_last_update_id(updates)+1
            handle_updates(updates)
            movie_list=ytsmovies.get_list()
			latest_movie_list=movie_list.difference(last_movie_list)
			handle_movies(latest_movie_list)
			movies=db.get_movie_list()
			IDS=db.get_id()
			for chat_ids in IDS:
				send_message(movies,) #send movies using for loop to every chat id complexity prblm.
			last_movie_list=movie_list.copy()
		time(0.5)


if __name__=='__main__':
	main()




