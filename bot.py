# !bin/python3
# initial group me Bot file

import requests
import secrets

# initial groupme API URL
url = 'https://api.groupme.com/v3/bots/post'

# nouns
m_Nouns = [ 'YOU CRAZY KIDS',
            # 'YOU SHITBIRDS',
            # 'ANDREW "RICKY C" MUNSTER',
            'PARTY PEOPLE']

# shouts
m_Shouts = ['LETS GO!',
            'AND EAT SHIT CHANG',
            'TECH HALL STILL SMELLS BAD',
            'IM SORRY ABOUT MY LATE FEE RIA',
            'EVEN U ZHANG',
            'LETS GET THIS BREAD',
            'LETS DO THIS SHIT',
            'LETS ENGINERD']

# build the request 
data = {
        "text" : "RISE AND GRIND {0}, {1}".format(secrets.choice(m_Nouns), secrets.choice(m_Shouts)), 
        "bot_id" : "2e542107791110329aabd6cbd9"}

# Run that shit
response = requests.post(url, data=data)