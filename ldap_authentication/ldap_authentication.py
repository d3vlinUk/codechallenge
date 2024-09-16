
def authenticate_connection_noncompliant():
    import ldap
    import os
    connect = ldap.initialize('ldap://127.0.0.1:1389')
    connect.set_option(ldap.OPT_REFERRALS, 0)
    connect.simple_bind('cn=root')
