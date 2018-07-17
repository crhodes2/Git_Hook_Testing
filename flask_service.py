from flask import Flask, request, render_template
import os, sys, json, importlib
import requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)


#########################################################
#                   GET AND POST
#                  REQUEST METHOD
#########################################################

@app.route('/', methods=['POST'])
def index():

    # RECEIVE THE POST REQUEST
    jsonRequest = request.json  # request payload taken straight from the gitHub repository

    # baseStatusUrl = jsonRequest["pull_request"]["head"]["repo"]["statuses_url"]
    # pullRequestId = jsonRequest["pull_request"]["id"]
    # print('Receive a POST Request from GitHub!: \t', jsonRequest)
    # print('Pull Request ID: \t', jsonRequest["pull_request"]["id"])
    # print('Pull Request ID (variable): \t', pullRequestId)
    # print('any PR statuses url: \t', baseStatusUrl)

    payloadBody = {"state":"success", "target_url":"http://example.com/build/status", "description":"build succeeded", "context":"continuous-integration/abigail" }

    authentication = HTTPBasicAuth('crhodes2', '18a0c4df0757c68f13767c0568e1bfc66169c512')

    completeStatusUrl = jsonRequest["pull_request"]["statuses_url"]

    responseObject = requests.post(url=completeStatusUrl, json=payloadBody, auth=authentication)
    print("Response Object ->", responseObject)

    return "done"


@app.route('/responseAPI', methods=['POST'])
def randomAPI():
    with open("responseAPI_Success.json", "r") as file:
        s = json.load(file)
    with open("responseAPI_Failure.json", "r") as file:
        f = json.load(file)
    with open("responseAPI_Pending.json", "r") as file:
        p = json.load(file)

    return json.dumps(s)

#########################################################
#                 MAIN PROGRAM


if __name__ == "__main__":
  app.run(debug=True)


























# ###################################################################################################################################################################
# #                   PROFILE
#
# @app.route('/profile/<name>')
# def profile(name):
#     return render_template("profile.html", name=name)
#
#
# #########################################################
# #                      ID
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#
#     return "<h2> Post ID is %s <h2>" % post_id