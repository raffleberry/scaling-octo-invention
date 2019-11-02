from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html", test=5)
	
@app.route("/search")
def salvador():
	return "No Search results found"

if __name__ == "__main__":
	app.run(debug=True)
