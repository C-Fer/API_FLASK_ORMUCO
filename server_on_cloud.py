import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict

from auth_login import get_token

env_url = 'https://api-uat-001.ormuco.com'
nova_port = '8774'
headers = {'X-Auth-Token': get_token()}
image_Ref = request.form.get('imagenes')
flavor_Ref = request.form.get('flavors')
network_id = request.form.get('redes')
key = request.form.get('llaves')
s_group = request.form.get('grupos')
def make_server():
    server_to_create = {
    "server": {
        "name": "CamiloFernandezServer",
        "imageRef": image_Ref['id'],
        "flavorRef": flavor_Ref['id'],
        "networks": [
            {
            "uuid": network_id['id']
            }
        ],
        "key_name": key['name'],
        "security_groups": [
            {
                "name": s_group['id']
            }
        ]
    }
}
    server_on_cloud = requests.post(f'{env_url}:{nova_port}/v2.1/servers',json=server_to_create, headers=headers)
    return "Servidor creado"