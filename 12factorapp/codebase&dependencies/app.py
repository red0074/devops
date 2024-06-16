from flask import Flask
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to codebase"

@app.route('/nothing')
def notihing():
    return "<h1>flask is simpler than it looks</h1>"


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

