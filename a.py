import boto3
from botocore.exceptions import NoCredentialsError

def create_s3_bucket(bucket_name, region):
    s3 = boto3.client('s3', region_name=region)

    try:
        # Create S3 bucket
        s3.create_bucket(Bucket=bucket_name)
        print(f'S3 bucket {bucket_name} created successfully.')

        # Create three folders in the S3 bucket
        folders = ['anki.site1', 'anki.site2', 'anki.site3']
        for folder in folders:
            s3.put_object(Bucket=bucket_name, Key=f'{folder}/')

        print('Folders created successfully.')
    except NoCredentialsError:
        print('Credentials not available.')
    except s3.exceptions.BucketAlreadyExists:
        print(f'The bucket {bucket_name} already exists.')
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f'The bucket {bucket_name} is already owned by you.')

if __name__ == "__main__":
    bucket_name = 'anki12'  # Replace with your desired bucket name
    region = 'us-east-1'  # Remove any extra spaces before or after the region code

    create_s3_bucket(bucket_name, region)
