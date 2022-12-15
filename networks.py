import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict

from auth_login import get_token

env_url = 'https://api-uat-001.ormuco.com'
neutron_port='9696'
headers = {'X-Auth-Token': get_token()}

def get_networks():
    networks = requests.get(url=f"{env_url}:{neutron_port}/v2.0/networks", headers=headers).json().get('networks')
    return networks