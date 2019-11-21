from __future__ import print_function
import time
from flask import Flask, render_template, request, Response, make_response
import csv
import json

app = Flask(__name__)

@app.route("/")
def main():
    p = time.time()
    return render_template("index.html", p=p)

@app.route("/adfo")
def adfo():
    p = time.time()
    return render_template("adfo.html", p=p)

@app.route("/csv")
def csvinput():
    p = time.time()
    return render_template("csv.html", p=p)

@app.route("/csvresponce", methods=['POST'])
def csvresponce():
    path = request.json['path']
    csv_file = open(path, "r", encoding="utf-8", errors="", newline="")
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    list = [e for e in f]
    return json.dumps(list[0])

@app.route("/csvtohtml", methods=['GET', 'POST'])
def csvoutput():
    if request.form:
        tags = request.form.getlist('tags')
        tags = ['div' if '' == s else s for s in tags]
        attrnames = request.form.getlist('attrname')
        attrnames = ['class' if '' == s else s for s in attrnames]
        path = request.form['path']
        csv_file = open(path, "r", encoding="utf-8", errors="", newline="")
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="", quotechar='"', skipinitialspace=True)
        if request.form['target'] == "vuedata":
            html = csvtovue(f)
        else :
            html = csvtohtml(f, attrnames, tags)
        return Response(html, mimetype='text/plain')
    else:
        return Response("NO DATA", mimetype='text/plain')

def csvtohtml(f, attrnames, tags):
    html = ""
    header = next(f)
    for row in f:
        attrs = {
            attrnames[0]: row[0]
        }
        html += wraphtml("", tags[0], attrs, "open")
        for index, cell in enumerate(row):
            if(index <= 0):
                continue
            elif cell == "":
                continue
            attrname = attrnames[index]
            head = header[index]
            tag = tags[index]
            attrs = {
                attrname: head
            }
            cell = cell.replace('\r\n', '<br>')
            cell = cell.replace('\n','<br>')
            html += wraphtml(cell, tag, attrs)
        html += wraphtml ("", tags[0], "", "close")
    return html

def csvtovue(f):
    html = ""
    header = next(f)
    for row in f:
        html += "{\r\n"
        for index, cell in enumerate(row):
            if cell == "":
                continue
            head = header[index]
            cell = cell.replace('\r\n','<br>')
            cell = cell.replace('\n','<br>')
            html += '   '+head+': "'+cell+'",\r\n'
        html += "},\r\n"
    return html

def wraphtml(html="", tag="p", attrs="", part=False):
    attr = " "
    if attrs:
        for name, value in attrs.items():
            attr += name+'="'+value+'" '
    if not part:
        wrapped = '\r\n    <'+tag+attr+'>'+html+'</'+tag+'>'
    elif part=='open':
        wrapped = '<'+tag+attr+'>'+html
    elif part=='close':
        wrapped = '\r\n</'+tag+'>\r\n'
    return wrapped


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
