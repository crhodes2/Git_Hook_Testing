from flask import Flask, request, render_template
import json
app = Flask(__name__)


#########################################################
#                   GET AND POST
#                  REQUEST METHOD


@app.route('/', methods=['GET', 'POST'])
def index():
    jsonRequest = request.json
    if request.method == 'POST':

        print('Get a POST Request!: \t', request)
        print('request.json: \t', jsonRequest)

        j = json.loads(jsonRequest)

        print("Manipulate the POST request!")

        j[1]["first"] = "Fancy"
        print(j)

        print("END the POST Request!")

        print('form_data: ', request.form.get('api_source_code'))

        return "You are using POST"

    else:
        with open("randomApi.txt","r") as f:
            j = json.load(f)
        return json.dumps(j)


#########################################################
#                   PROFILE

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


#########################################################
#                      ID

@app.route('/post/<int:post_id>')
def show_post(post_id):

    return "<h2> Post ID is %s <h2>" % post_id


#########################################################
#                 MAIN PROGRAM


if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')