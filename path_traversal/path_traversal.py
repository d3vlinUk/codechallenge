
def verify_file_path_noncompliant():
    from flask import request
    file_path = request.args["file"]
    file = open(file_path)
    file.close()