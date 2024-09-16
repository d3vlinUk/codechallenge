def constructor():
    import hashlib

    text = "ExampleString"
    result = hashlib.new('sha256', text.encode())

    print("The hexadecimal equivalent of SHA256 is : ")
    print(result.hexdigest())
