import requests
from flask import Flask, render_template, url_for, request, redirect, g 
from collections import defaultdict
#from server_on_cloud import make_server
from auth_login import get_token
from networks import get_networks
from images import get_images
from flavors import get_flavors
from securityGroups import get_security_group
from keypairs import get_keypairs

app = Flask(__name__)

headers = {'X-Auth-Token': get_token()}

print("------------------------------------------------------------------------------")
''''''
env_url = 'https://api-uat-001.ormuco.com'
nova_port = '8774'

@app.route('/', methods=["GET"])
def index():
    images = get_images()
    networks= get_networks()
    flavors = get_flavors()
    keypairs = get_keypairs()
    securitygroups = get_security_group()
    return render_template("index.html", networks = networks, images = images, flavors = flavors, securitygroups = securitygroups, keypairs = keypairs)

@app.route('/create_instance', methods = ["POST"])
def create_i():
    image_Ref = request.form.get('imagenes')
    flavor_Ref = request.form.get('flavors')
    network_id = request.form.get('redes')
    key = request.form.get('llaves')
    s_group = request.form.get('grupos')

    server_to_create = {
    "server": {
        "name": "FUNCIONAA",
        "imageRef": image_Ref,
        "flavorRef": flavor_Ref,
        "networks": [
            {
            "uuid": network_id
            }
        ],
        "key_name": key,
        "security_groups": [
            {
                "name": s_group
            }
        ]
    }
}
    server_on_cloud = requests.post(f'{env_url}:{nova_port}/v2.1/servers',json=server_to_create, headers=headers)
    print(server_on_cloud.reason)
    print(server_on_cloud.text)
    return "Servidor Creado"
"""Función para la pagina de Images"""
@app.route('/images/', methods=["GET"])
def viewImages():
    return render_template("images.html", images = get_images())

"""Función para la pagina de Networks"""
@app.route('/networks/', methods=["GET"])
def viewNetwork():
    return render_template("networks.html", networks=get_networks())


"""Función para la pagina de Flavors"""
@app.route('/flavors/', methods=["GET"])
def viewFlavor():
    return render_template("flavors.html", flavors = get_flavors())

"""Función para la pagina de Security Groups"""
@app.route('/security-g/', methods=["GET"])
def viewSecurityGroups():
    return render_template("securitygroups.html", security_groups = get_security_group())

"""Función para la pagina de Key_Pairs"""
@app.route('/key-p/', methods=["GET"])
def viewKeyPairs():
    return render_template("keypairs.html", keypairs = get_keypairs())



if (__name__ == "__main__"):
    app.run(debug=True)
