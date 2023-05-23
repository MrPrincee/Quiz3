import requests
import json
import sqlite3
from win10toast import ToastNotifier



url = "https://randomuser.me/api"
#1
get = requests.get("https://randomuser.me/api")
print(get)
print(get.json)
print(get.status_code)
print(get.text)
print(get.headers)

#2
res = json.loads(get.text)
resd = json.dumps(res,indent=4)
print(resd)


#3 გამოაქვს მომხმარებლის სქესი
gender = get.json()["results"][0]['gender']
print(gender)

#4
# conn = sqlite3.connect("user_database.sqlite")
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE users_gender
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# gender VARCHAR(50));''')
#
# cursor.execute("INSERT INTO users_gender (gender) VALUES (?)",(gender))
# conn.commit

#5

info = ToastNotifier()
info.show_toast(f'Users gender is {gender}')
