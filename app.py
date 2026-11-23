import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/ping")
def ping():
    # Deliberately unsafe: a request value reaches the shell, so code scanning has an alert to report.
    return str(os.system("ping -c 1 " + request.args.get("host", "localhost")))
