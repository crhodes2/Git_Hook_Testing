from flask import Flask, request, render_template
import json
app = Flask(__name__)


#########################################################
#                GET, POST, AND PUT
#                  REQUEST METHOD


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    jsonRequest = request.json
    if request.method == 'POST':
        print("Got a post request!")
        print(request)
        print("middle!")
        print('request.json: \t', jsonRequest)
        print("end a post request!")

        #g = json.loads(request.json)

        print('form_data: ', request.form.get('api_source_code'))
        # with open("post.json", "w") as f:
        #     f.write(json.dumps(request.json))

        return "You are using POST"

    elif request.method == 'PUT':
        return "Why you using PUT"

    else:
        return "You are probably using GET!"


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