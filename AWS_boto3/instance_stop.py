import boto3

ids = ['i-032307d91e9437d7e']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop()