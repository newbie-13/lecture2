from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hi():
    return render_template('index2.html')

@app.route("/about")
def about():
    name='Inside Python'
    return render_template('about.html',name=name)
