import boto3


aws_access_key_id = 'xxxxxxxxx'
aws_secret_access_key = 'xxxxxxxxxxxxxxxxxx'
aws_session_token = 'xxxxxxxxxxxxxxxxxx'
aws_region = 'SUA_REGIAO'


ec2_client = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)

instance_type = 't2.micro' # instância de teste
key_name = 'SUA_KEY'
security_group_ids = ['SEU_SECURITY_GROUP']  
image_id = 'ami-0fc5d935ebf8bc3bc' # imagem do ubuntu
tags = [
    {'Key': 'Name', 'Value': 'teste-ec2'} 
]


response = ec2_client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[{'ResourceType': 'instance', 'Tags': tags}]
)


instance_id = response['Instances'][0]['InstanceId']

print(f"Nova instância iniciada com ID: {instance_id}")
