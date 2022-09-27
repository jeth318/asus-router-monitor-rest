import os
from asus_router import AsusRouter
from flask import Flask, make_response, render_template, jsonify
from flask_cors import CORS
import json
from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = dotenv_values(".env")
routerIp = os.environ['ROUTER_IP']
routerUser = os.environ['ROUTER_USER']
routerPass = os.environ['ROUTER_PASS']

try:
    port = os.environ["PORT"]
except:
    print("No custom port specified in the .env file. Using fallback port 3555.")
    port = 3555

app = Flask(__name__)
CORS(app)

ar = AsusRouter(routerIp, routerUser, routerPass)


def res(data):
    try:
        return make_response(jsonify(data))
    except Exception as e:
        return make_response("Error")

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/settings')
def settings():
    return res(ar.get_settings())


@app.route('/online-clients')
def onlineClients():
    return ar.get_online_clients()


@app.route('/dhcp-list')
def dhcpList():
    return res(ar.get_dhcp_list())


@app.route('/cpu-usage')
def cpuUsage():
    return res(ar.get_cpu_usage())


@app.route('/memory-usage')
def memoryUsage():
    return res(ar.get_memory_usage())


@app.route('/client-info/<mac>')
def clientInfo(mac):
    id = mac.replace("-", ":")
    print(id)
    return res(ar.get_client_info(id))


@app.route('/clients-info')
def clientsInfo():
    return res(ar.get_clients_info())


if __name__ == '__main__':
    app.run(host='localhost', port=port)
