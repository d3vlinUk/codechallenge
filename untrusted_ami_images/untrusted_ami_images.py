
def image_filter_non_compliant():
    import boto3
    ec2 = boto3.resource('ec2')
    image_name = 'The name of the AMI (provided during image creation)'
    filters = [{'Name': 'name', 'Values': [image_name]}]
    images = ec2.images.filter(Filters=filters)
