import os
from asus_router import AsusRouter
from flask import Flask, make_response, render_template, jsonify
from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = dotenv_values(".env")
routerIp = os.environ['ROUTER_IP']
routerUser = os.environ['ROUTER_USER']
routerPass = os.environ['ROUTER_PASS']

app = Flask(__name__)

rtax58u = AsusRouter(routerIp, routerUser, routerPass)


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
    return res(rtax58u.get_settings())


@app.route('/online-clients')
def onlineClients():
    return res(rtax58u.get_online_clients())


@app.route('/dhcp-list')
def dhcpList():
    return res(rtax58u.get_dhcp_list())


@app.route('/cpu-usage')
def cpuUsage():
    return res(rtax58u.get_cpu_usage())


@app.route('/memory-usage')
def memoryUsage():
    return res(rtax58u.get_memory_usage())


@app.route('/client-info/<mac>')
def clientInfo(mac):
    id = mac.replace("-", ":")
    print(id)
    return res(rtax58u.get_client_info(id))


@app.route('/clients-info')
def clientsInfo():
    try:
        return res(rtax58u.get_clients_info())
    except Exception as e:
        print("ERR", str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9988)
