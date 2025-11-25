from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "farris" and password == "admin#123":
        return render_template("dashboard.html")
        
if __name__ == '__main__':
    app.run(debug=True)
