from __future__ import print_function
import time
from flask import Flask, render_template

app = Flask(__name__)

def show():
    test_data = open("templates/test.txt", "r")
    contents = test_data.read()
    test_data.close()
    return contents

@app.route("/")
def main():
    s = show()
    return render_template("index.html", s=s)

if __name__ == "__main__":
    print('on hello')
    app.run(host="127.0.0.1", port=5000)
