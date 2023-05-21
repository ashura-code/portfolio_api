from flask import Flask, render_template

app = Flask(__name__,template_folder="./templates")



@app.route("/")
def hello():
    return render_template('./mainpage.html')


@app.route("/intro")
def drinks():
    return {"name":'Adhitya Nantish',"age":18,"passion":["I like to code","I like to break"]}

