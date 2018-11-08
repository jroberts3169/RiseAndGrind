# !bin/python3
# this script is meant to hype up the REAL OG's group me every morning
# WORK IN PROGRESS OK

import requests
import secrets

# initial groupme API URL
url = 'https://api.groupme.com/v3/bots/post'

# nouns
m_Nouns = [ 'YOU CRAZY KIDS',
            'YOU SHITBIRDS',
            'ANDREW "RICKY C" MUNSTER',
            'PARTY PEOPLE',
            'NERDS',
            'GAMERS?',
            'BABY SHARKS']

# shouts
m_Shouts = ['LETS GO!',
            'AND EAT SHIT CHANG',
            'TECH HALL STILL SMELLS BAD',
            'IM SORRY ABOUT MY LATE FEE RIA',
            'EVEN U ZHANG',
            'LETS GET THIS BREAD',
            'LETS DO THIS SHIT',
            'LETS ENGINERD',
            'LETS YEET THIS YEAST',
            'LETS GET THIS MF GUALA',
            'IT\'S TIME TO DO DO DO DOOO DOOOOOO']

# build the request 
data = {"text" : "RISE AND GRIND {0}, {1}".format(secrets.choice(m_Nouns), secrets.choice(m_Shouts)), 
        "bot_id" : "2e542107791110329aabd6cbd9"}

# Run that shit
response = requests.post(url, data=data)