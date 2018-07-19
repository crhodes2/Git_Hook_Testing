from flask import Flask, request, render_template
import os, sys, json, importlib
import requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)


#########################################################
#                   GET AND POST
#                  REQUEST METHOD
#########################################################


github_auth_key = str(os.environ['GITHUB_AUTH_KEY'])
authentication = HTTPBasicAuth('crhodes2', github_auth_key)

def buildPending():
    payloadPending = {"state":"pending", "target_url":"http://www.google.com", "description":"build pending", "context":"continuous-integration/jama" }
    return payloadPending

@app.route('/', methods=['GET', 'POST'])
def index():

    # RECEIVE THE POST REQUEST
    jsonRequest = request.json  # request payload taken straight from the gitHub repository

    # payloadBody = {"state":"pending", "target_url":"http://www.google.com", "description":"build pending", "context":"continuous-integration/jama" }
    # baseStatusUrl = jsonRequest["pull_request"]["head"]["repo"]["statuses_url"]
    # pullRequestId = jsonRequest["pull_request"]["id"]
    # print('Receive a POST Request from GitHub!: \t', jsonRequest)
    # print('Pull Request ID: \t', jsonRequest["pull_request"]["id"])
    # print('Pull Request ID (variable): \t', pullRequestId)
    # print('any PR statuses url: \t', baseStatusUrl)

    completeStatusUrl = jsonRequest["pull_request"]["statuses_url"]
    commitNumber = jsonRequest["pull_request"]["commits"]


    responseObject = requests.post(url=completeStatusUrl, json=buildPending(), auth=authentication)

    # commitListUrl = requests.get('https://api.github.com/repos/crhodes2/platform-samples/pulls/21/commits', data={'key': 'value'})
    # ''.join()

    print("Response Object ->", responseObject)
    # print("Response Object ->", commitListUrl)
    print("List of Commits ->", commitNumber)


    return "done"

@app.route('/responseAPI', methods=['POST'])
def responseAPI():
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