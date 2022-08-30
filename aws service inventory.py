#AWS Service Inventory

#The list should be empty initially.

aws_service_list = []

#Populate the list using insert or append with the AWS services 
aws_service_list.append('cloud9')
aws_service_list.append('dynamodb')
aws_service_list.append('ec2')
aws_service_list.append('elasticache')
aws_service_list.append('vpc')
aws_service_list.append('sns')
aws_service_list.append('sqs')
aws_service_list.insert(0,'iam')
aws_service_list.insert(4, 'lambda')
aws_service_list.insert(6, 'cloudformation')

#print the list and the length of the list 
print(len(aws_service_list))

#Remove two specific services from the list by name or by index
#[2:4] means 2 and 3 
del aws_service_list[2:4]

#Print the new list and the new length of the list
print(len(aws_service_list))