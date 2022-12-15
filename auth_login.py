
import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict

env_url = 'https://api-uat-001.ormuco.com'
keystone_port = '5000'
glance_port='9292'
nova_port = '8774'
neutron_port='9696'

server_specifications={}
url = "https://api-uat-001.ormuco.com:5000/v3/auth/tokens"
payload = {
    
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }
    }

}
# 0. Authentication Request 
def get_token():
    token = requests.post(url=f"{env_url}:{keystone_port}/v3/auth/tokens", json=payload)
    token_id = token.json().get('token').get('id')
    return token_id