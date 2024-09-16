def kms_reencrypt():
    import boto3
    import base64
    client = boto3.client('kms')
    plaintext = client.decrypt(
        CiphertextBlob=bytes(base64.b64decode("secret"))
    )
    response = client.encrypt(
        KeyId='string',
        Plaintext=plaintext
    )
    return response