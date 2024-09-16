from flask import app


@app.route('/redirect')
def redirect_url():
    from flask import request, redirect
    endpoint = request.args['url']
    return redirect(endpoint)

