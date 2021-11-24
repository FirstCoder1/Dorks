# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, send_file, request, make_response
from google.cloud import firestore
from service.firestore_service import get_session_data
from dotenv import load_dotenv
from pathlib import Path
import logging
import sys
import os
from flask_cors import CORS
from utility import load_blueprints
import config

app = Flask(__name__, template_folder="dist")
app.secret_key = config.secret_key
CORS(app)
blueprints = load_blueprints()
CORS(app, resources={r"/*": {"origins": "https://cbb2-104-227-23-10.ngrok.io/"}}, supports_credentials=True)
#CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)

for bp in blueprints:
    app.register_blueprint(bp)
db = firestore.Client()
load_dotenv(dotenv_path=Path(r"/Users/tmatembo/Desktop/Dorks/Dorks/client/.env"))

@app.route('/css/<path:filename>')
def css(filename):
    return send_file(os.path.join(os.getcwd(), "dist/css/%s" % filename))


@app.route('/js/<path:filename>')
def js(filename):
    return send_file(os.path.join(os.getcwd(), "dist/js/%s" % filename))


@app.route('/img/<path:filename>')
def img(filename):
    if 'favicon' in filename or 'android' in filename:
        return ''
        # return send_file(os.path.join(os.getcwd(), "dist/favicon.png"))
    return send_file(os.path.join(os.getcwd(), "dist/img/%s" % filename))



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    session_data = get_session_data(db.transaction(), request.cookies.get('session_id'))
    resp = make_response(render_template('index.html'))
    resp.set_cookie('session_id', session_data['session_id'])
    return resp


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(port=5000, debug=True)

# [END gae_python37_app]
