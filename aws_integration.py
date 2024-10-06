import boto3
import joblib
import json

# Initialize AWS services
s3 = boto3.client('s3')
sagemaker = boto3.client('sagemaker')
lambda_client = boto3.client('lambda')

# Upload models to S3
bucket_name = 'your-bucket-name'
s3.upload_file('approval_model.joblib', bucket_name, 'models/approval_model.joblib')
s3.upload_file('interest_model.joblib', bucket_name, 'models/interest_model.joblib')
s3.upload_file('term_model.joblib', bucket_name, 'models/term_model.joblib')

# Create a SageMaker endpoint for real-time inference
# Note: This is a simplified example. In practice, you'd need to create a SageMaker model and endpoint configuration.
endpoint_name = 'loan-recommendation-endpoint'
sagemaker.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName='your-endpoint-config-name'
)

# Create a Lambda function for generating recommendations
lambda_function_name = 'loan-recommendation-function'
lambda_client.create_function(
    FunctionName=lambda_function_name,
    Runtime='python3.8',
    Role='your-lambda-execution-role-arn',
    Handler='lambda_function.lambda_handler',
    Code={
        'ZipFile': open('lambda_function.zip', 'rb').read()
    },
    Environment={
        'Variables': {
            'ENDPOINT_NAME': endpoint_name
        }
    }
)

print("AWS integration completed.")