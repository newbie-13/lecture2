from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def index():
    names=["Alice","Bob","Cherry","Don"]
    return render_template("index4.html",names=names)
