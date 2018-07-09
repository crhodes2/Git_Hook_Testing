from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        print(request.json)
        #g = json.loads(request.json)
        print(request.json.get("action"))
        with open("post.json", "w") as f:
            f.write(json.dumps(request.json))
        return "You are using POST"
    elif request.method == 'PUT':
        return "Why you using PUT"
    else:
        return "You are probably using GET!"

@app.route('/test')
def test():
    if request.method == "POST":
        return "Thank you for testing me!"
    else:
        return "Nothing happens"

@app.route('/pull_request')
def pull_request():
    if request.method == 'POST':
        return "Displaying Pull Request"
    else:
        return "nothing happens"

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/post/<int:post_id>')
def show_post(post_id):

    return "<h2> Post ID is %s <h2>" % post_id

if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')