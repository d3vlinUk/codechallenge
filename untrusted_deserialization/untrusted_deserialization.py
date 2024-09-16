
def untrusted_deserialization_noncompliant():
    import jsonpickle
    userobj = input("user")
    obj = jsonpickle.decode(userobj)
    return obj
