import boto3;

dynamodb = boto3.client('dynamodb');

response = dynamodb.create_table(
AttributeDefinitions=[
{	'AttributeName' : 'string',
	'AttributeType' : 'S'},
],
TableName='Halloo',
KeySchema=[
{	'AttributeName' : 'string',
	'KeyType' : 'HASH'},
},
],
ProvisionedThroughput={
	'ReadCapacityUnits':1,
	'WriteCapacityUnits':2
}
);
	

