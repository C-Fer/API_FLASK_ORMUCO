import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict

from auth_login import get_token

env_url = 'https://api-uat-001.ormuco.com'
glance_port='9292'
headers = {'X-Auth-Token': get_token()}

def get_images():
    images=requests.get(url=f"{env_url}:{glance_port}/v2/images", headers=headers).json().get('images')
    return images