# Getting Started: Downloading Data from the Cloud & PyTorch Custom Datasets, Transforms, and DataLoader
## Firstname Lastname
TODO - Update your name in this readme

TODO - Add a badge to github actions here (see references for documentation).

## Assignment Overview
In this assignment we will:
1. Write data utility functions using [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) Amazon Web Services (AWS) SDK for Python that allows you to interact with data stored on the cloud.
2. Partition the available training data into a train and validation set by subsetting `meta.csv`.

## Setting Up Your Project Environment
To make sure you download all the requirements to begin this homework assignment enter `pip install -r requirements.txt` into your terminal.


## Retrieving Public Dataset Using AWS SDK
The BPS dataset is a public data repository hosted in an S3 AWS bucket which is a cloud-based storage service provided by Amazon. It allows users to store and retrieve data from anywhere at any time. S3 stands for Simple Storage Service, and it provides a scalable and reliable way to store data in the cloud. AWS S3 buckets can store any type of object or file, such as documents, images, videos, and other types of data, and can be accessed through APIs, web interfaces, or command-line interfaces. In this assignment you will be interacting with this API using `boto3`, an AWS package that allows you to use Python code to interact with data stored in the S3 bucket.

### AWS boto3 API
`boto3` is a python library that allows you to interact with AWS services using python code. To get started, we need to initialize the boto3 client with the s3 service and the signature_version set to UNSIGNED to allow for public access to the data:

`s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))`

To download the data from cloud to our local machine, we use the `download_file` method from the boto3 client. Alternatively, we can use the `get_object` method from the boto3 client to get the data as a stream without having to save files locally. In either case, in order to retrieve data, the bucket name and s3 path to the data are required. In this assignment we will do both. 

1. We will retrieve `meta.csv` as a stream in order to select a subset of the data based on the attributes `dose_Gy` and `hr_post_exposure` and save this into a new metadata csv file.
2. Using the new metadata csv file, we will selectively download image files of interest from the s3 bucket.

## File to Work On
- `data_utils_boto3/data_utils.py`

## Running Tests
There are two ways to run unit tests:
1. Run them directly from `tests/test_data_utils.py`
2. Run them with GitHub Actions CI/CD Tools.

## NOTE
- It is required that you add your name and github actions workflow badge to your readme.
- Check the logs from github actions to verify the correctness of your program.
- The initial code will not work. You will have to write the necessary code and fill in the gaps.
- Commit all changes as you develop the code in your individual private repo. Please provide descriptive commit messages and push from local to your repository. If you do not stage, commit, and push git classroom will not receive your code at all.
- Make sure your last push is before the deadline. Your last push will be considered as your final submission.
- There is no partial credit for code that does not run.
- If you need to be considered for partial grade for any reason (failing tests on github actions,etc). Then message the staff on discord before the deadline. Late requests may not be considered.

## References
[GH Badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)

## Authors
- @nadia-eecs Nadia Ahmed
- @campjake Jacob Campbell