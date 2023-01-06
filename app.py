from flask import Flask, redirect, render_template
from dashboard import dashboard
from api import api

app = Flask(__name__)
app.register_blueprint(dashboard, url_prefix="/dashboard")
app.register_blueprint(api, url_prefix="/api")

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def dashboard():
    return redirect("/dashboard")

@app.route("/review")
def review():
    return render_template("review.html")

if __name__ == "__main__":
    app.run(debug=False, port=3847)
    print("Server is online\nhttp://localhost:3847/")
