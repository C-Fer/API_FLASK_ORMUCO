import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict

from auth_login import get_token

env_url = 'https://api-uat-001.ormuco.com'
nova_port = '8774'
headers = {'X-Auth-Token': get_token()}

def get_flavors():
   flavors = requests.get(url=f"{env_url}:{nova_port}/v2.1/flavors", headers=headers).json().get('flavors')
   return flavors