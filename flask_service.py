from flask import Flask, request, render_template
import os, sys, json, importlib, time, requests, urllib3, urllib.request
from requests.auth import HTTPBasicAuth
from threading import Thread
app = Flask(__name__)


#########################################################
#                   GET AND POST
#                  REQUEST METHOD
#########################################################


github_auth_key = str(os.environ['GITHUB_AUTH_KEY'])
authentication = HTTPBasicAuth('crhodes2', github_auth_key)
with open("responseAPI_Success.json", "r") as file:
    success = json.load(file)
with open("responseAPI_Failure.json", "r") as file:
    failure = json.load(file)
with open("responseAPI_Pending.json", "r") as file:
    pending = json.load(file)

def buildPending():
    payloadPending = {"state":"pending", "target_url":"http://www.google.com", "description":"build pending", "context":"continuous-integration/jama" }
    return payloadPending

def buildSuccess():
    payloadPending = {"state":"success", "target_url":"http://www.google.com", "description":"build was a success", "context":"continuous-integration/jama" }
    return payloadPending

def buildFailure():
    payloadPending = {"state":"pending", "target_url":"http://www.google.com", "description":"build has failed", "context":"continuous-integration/jama" }
    return payloadPending

@app.route('/', methods=['GET', 'POST'])
def index():

    # RECEIVE THE POST REQUEST FROM GITHUB
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
    commitUrl = jsonRequest["pull_request"]["commits_url"]

    listofCommits = requests.get(url=commitUrl)
    print("# commit links? --> " + str(listofCommits))

    # SEND IN STATUS TO POST REQUEST TO GITHUB AS A PENDING BADGE
    responseObject = requests.post(url=completeStatusUrl, json=buildPending(), auth=authentication)

    print("Receiving PR from GitHub... ...please wait")
    time.sleep(5)
    print("Response Result ->", responseObject)
    print("Getting Commits Count... ...please wait")
    time.sleep(5)
    print("Commits Count in PR: ", commitNumber, " commit(s) found in PR!")


    if commitNumber % 2 == 0:
        # SEND IN STATUS TO POST REQUEST TO GITHUB AS A PENDING BADGE
        evenResponse = requests.post(url=completeStatusUrl, json=buildSuccess(), auth=authentication)
        print("Response Result -->", evenResponse, "Success!")
    else:
        oddResponse = requests.post(url=completeStatusUrl, json=buildFailure(), auth=authentication)
        print("Response Result -->", oddResponse, "Failure!")


    #TODO: EXTRACT JSON FILE FROM THE LIST OF COMMITS API LINK to display all the messsages available
    # with urllib.request.urlopen(str(listofCommits)) as url:
    #     data = json.loads(url.read().decode())
    #     print(data)

    return "done"

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