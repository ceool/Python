import boto3

ids = ['i-043c3d5d47457e667']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).terminate()