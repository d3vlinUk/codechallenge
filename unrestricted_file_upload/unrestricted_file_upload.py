
from flask import app


@app.route('/', methods=['GET', 'POST'])
def file_upload_non_compliant():
    import os
    from flask import request
    upload_file = request.files['file']
    upload_file.save(os.path.join('/path/to/the/uploads',
                                upload_file.filename))
