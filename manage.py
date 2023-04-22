from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome"

@app.route("/greetings/<holiday>")
def greetings(holiday):
	if holiday == "christmas":
		return "Merry Christmas"
	elif holiday == "newyear":
		return "Happy New Year"

if __name__ == "__main__":
	app.run()
