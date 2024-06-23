import os
from flask import Flask
from redis import Redis

app=Flask(__name__)
# redisDb=Redis(host='localhost',port=6381)
host=os.getenv('HOST')
port=os.getenv('PORT')
redisDb=Redis(host=host,port=port)
@app.route("/")
def process():
    redisDb.incr('visitorcount')
    visitorcount=str(redisDb.get('visitorcount'),'utf-8')
    return "welcome to process with external service"+visitorcount


visit=0


@app.route('/processbasicexample')
def welcome():
    global visit
    visit+=1
    return "welcome to codebase"+str(visit)

@app.route('/nothing')
def notihing():
    return "<h1>flask is simpler than it looks</h1>"


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)

