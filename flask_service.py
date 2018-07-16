from flask import Flask, request, render_template
import os, sys, json, importlib
import requests
app = Flask(__name__)

#import git_http_request


#########################################################
#                   GET AND POST
#                  REQUEST METHOD


@app.route('/', methods=['GET', 'POST'])
def index():
    # # if request.method == 'GET':
    # #     return "test"
    # # else:
    #     #Get a POST Request:: locate the weblink to the object
    #
    #
    jsonRequest = request.json
    #
    #
    #
    if request.method == 'POST':


        #Get a POST Request:: locates the weblink to the object
        print('Get a POST Request!: \t', request)

        #request.json:: extract the json object from that weblink
        print('request.json: \t', jsonRequest)

        # Manipulate the POST Request received
        # print("Manipulate the POST request!: \t", request)
        modJsonRequest = jsonRequest
        print('Pull Request ID: \t', modJsonRequest["pull_request"]["id"])








    #     modJsonRequest[1]["first"] = "Fancy"
    #     print(modJsonRequest)
    #
    #     POST_Req = ''.join(map(str, modJsonRequest))
    #
    #     # print('form_data: ', request.form.get('api_source_code'))
    #
    #     return POST_Req
    #
    # else:
    #     #open the json file to be manipulated
    #     with open("randomApi.txt", "r") as file:
    #         jsonObject = json.load(file)
    #     return json.dumps(jsonObject)
    return "test"


@app.route('/anotherAPI', methods=['GET', 'POST'])
def randomAPI():
    with open("anotherAPI.txt", "r") as file:
        jsonObject = json.load(file)
    return json.dumps(jsonObject)

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