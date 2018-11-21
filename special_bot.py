#!/bin/python3

# special bot - this one is for spanksgiving mkay

import requests
import secrets

test_group = "2e542107791110329aabd6cbd9"
OGs_group = "7ba46a2f9140727115d4c715cd"

# groupme API URL
url = 'https://api.groupme.com/v3/bots/post'

# nouns
m_Nouns = [ 'GOOOOOOD MORNING HUNTSVEGAS']

# shouts
m_Shouts = ['ENJOY YOUR BREAK!!']

# build the request 
data = {"text" : "{0}, {1}".format(secrets.choice(m_Nouns),
                                                secrets.choice(m_Shouts)), 
        "bot_id" : test_group}

# Run that shit
response = requests.post(url, data=data)
