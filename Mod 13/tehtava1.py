from flask import Flask, request

app = Flask(__name__)

@app.route('/onko_alkuluku')
def onko_alkuluku():
    args = request.args
    luku = int(args.get("luku1"))



app.run(use_reloader=True, host='127.0.0.1', port=3000)