from __future__ import print_function
import time
from flask import Flask, render_template, request, Response, make_response

app = Flask(__name__)

@app.route("/")
def main():
    p = time.time()
    return render_template("index.html", p=p)

@app.route("/result", methods=['GET', 'POST'])
def result():
    datas = request.form
    result = ""
    for data in datas.values():
        content = open(data, "r", encoding="utf-8_sig")
        result += content.read()
        content.close()
    return Response(result, mimetype='')

@app.route("/save", methods=['GET', 'POST'])
def save():
    datas = request.form
    result = ""
    for data in datas.values():
        content = open(data, "r", encoding="utf-8_sig")
        result += content.read()
        content.close()
    response = make_response()
    response.data = result
    response.headers['Content-Type'] = 'application/force-download'
    response.headers['Content-Disposition'] = u'attachment; filename=index.html'
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
