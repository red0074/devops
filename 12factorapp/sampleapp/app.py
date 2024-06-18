from flask import Flask

app=Flask(__name__)

visit=0

@app.route('/')
def welcome():
    global visit
    visit+=1
    return "welcome to codebase"+str(visit)

@app.route('/nothing')
def notihing():
    return "<h1>flask is simpler than it looks</h1>"


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

