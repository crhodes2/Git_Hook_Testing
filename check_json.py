from flask import Flask, request
import os, json, time, requests
from requests.auth import HTTPBasicAuth
app = Flask(__name__)


# RECEIVE THE POST REQUEST FROM GITHUB
jsonRequest = request.json  # request payload taken straight from the gitHub repository
commitNumber = jsonRequest["pull_request"]["commits"]
completeStatusUrl = jsonRequest["pull_request"]["statuses_url"]
github_auth_key = str(os.environ['GITHUB_AUTH_KEY'])
authentication = HTTPBasicAuth('crhodes2', github_auth_key)



def buildPending():
    payloadPending = {"state": "pending", "target_url": "http://www.google.com", "description": "build pending", "context": "continuous-integration/jama"}
    return payloadPending

def buildSuccess():
    payloadPending = {"state": "success", "target_url": "http://www.google.com", "description": "build was a success", "context": "continuous-integration/jama"}
    return payloadPending

def buildFailure():
    payloadPending = {"state": "pending", "target_url": "http://www.google.com", "description": "build has failed", "context": "continuous-integration/jama"}
    return payloadPending

def sendJson():
   if commitNumber % 2 == 0:
      # SEND IN STATUS TO POST REQUEST TO GITHUB AS A PENDING BADGE
      evenResponse = requests.post(url=completeStatusUrl, json=buildSuccess(), auth=authentication)
      print("Response Result -->", evenResponse, "Success!")
   else:
      oddResponse = requests.post(url=completeStatusUrl, json=buildFailure(), auth=authentication)
      print("Response Result -->", oddResponse, "Failure!")