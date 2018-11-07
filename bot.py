# !bin/python3
# initial group me Bot file

import requests
url = 'https://api.groupme.com/v3/bots/post'
headers = {'Content-type': 'application/json'}
data = {'text': 'RISE AND GRIND YOU CRAZY KIDS'}
params = {'bot_id': '2e542107791110329aabd6cbd9-8'}
r = requests.post(url=url, data=data, headers=headers, params=params)