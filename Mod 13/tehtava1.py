from flask import Flask, request

app = Flask(__name__)

def onko_alkuluku_funktiona(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


@app.route('/onko_alkuluku')
def onko_alkuluku():
    args = request.args
    luku = int(args.get("luku1"))

    if onko_alkuluku_funktiona(luku):
        return f"{luku} on alkuluku"
    else:
        return f"{luku} ei ole alkuluku"

app.run(use_reloader=True, host='127.0.0.1', port=3001)