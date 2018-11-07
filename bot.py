# !bin/python3
# initial group me Bot file

import requests
url = 'https://api.groupme.com/v3/bots/post'
m_Text = "LETS GO"
data = {
        "text" : "RISE AND GRIND YOU CRAZY KIDS {0}".format(m_Text), 
        "bot_id" : "2e542107791110329aabd6cbd9"}
response = requests.post(url, data=data)