#!/usr/bin/env python3

from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def print_public_ip():
  response = requests.get('http://checkip.dyndns.org')
  public_ip = response.text.split(': ')[1].split('<')[0]
  return f"Your public IP address is: {public_ip}"

if __name__ == '__main__':
  app.run()
