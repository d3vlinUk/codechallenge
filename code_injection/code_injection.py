
from flask import app


@app.route('/')
def execute_input():
    from flask import request
    module_version = request.args.get("module_version")
    exec("import urllib%s as urllib" % module_version)
