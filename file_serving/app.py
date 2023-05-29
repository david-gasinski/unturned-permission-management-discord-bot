# Flask app which hosts the XML permissions
from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True 

@app.route('/permissions')
def permissions():
    resp = make_response(render_template('Permissions.config.xml'))
    resp.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return resp

@app.route('/kits')
def permissions():
    resp = make_response(render_template('Kits.configuration.xml'))
    resp.headers['Content-Tyhttps://dl.dropboxusercontent.com/s/4ibdkww0egek8r5/perm_management.zippe'] = 'text/plain; charset=utf-8'
    return resp
