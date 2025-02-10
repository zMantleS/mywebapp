from flask import Flask

app = Flask("myflaskapp")

@app.route("/")
def index():
	return "<h1>Hello this is a basic flask app</h1>"



app.run(host="0.0.0.0", port=5000, debug=True)
