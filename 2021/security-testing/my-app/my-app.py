#!/usr/bin/env python3

import os
from flask import Flask

app = Flask(__name__)
env_var = os.getenv('FAVORITE_BEER', 'Westmalle')

@app.route('/')
def default():
    return f'Docker Switzerland Meetup: HACKDOCKERFEST! My favorite beer is {env_var}'

print("Starting basic web app")

app.run(host='0.0.0.0', port=80)
