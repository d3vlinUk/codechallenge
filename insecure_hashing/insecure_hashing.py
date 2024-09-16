def hashing_noncompliant():
    import hashlib
    from hashlib import pbkdf2_hmac
    derivedkey = hashlib.pbkdf2_hmac('sha224', password, salt, 100000)
    derivedkey.hex()