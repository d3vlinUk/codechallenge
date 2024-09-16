
from flask import app


@app.route('/getUsers')
def get_users_noncompliant():
    import ldap
    from flask import request
    username = request.args['username']
    filter_string = '(uid=' + username + ')'
    ldap_conn = ldap.initialize('ldaps://ldap.amazon.com:636')
    result = ldap_conn.search_s('o=amazon.com',
                                ldap.SCOPE_SUBTREE,
                                filter_string)
    return result