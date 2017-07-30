# Checking permissions for Google Cloud Storage buckets

This contains a script that lists the projects the authenticated user running it  has access to. It also provides a way to list the permissions granted to the  Google Cloud Storage  buckets in a project set in the GOOGLE_CLOUD_STORAGE environment variable

## Setup
### Authentication
To run the scripts you must have permissions to use GCP and need to be Authenticated via the  Application Default Credentials

Requires caller to have the  storage.buckets.getIamPolicy permission on the project containing the buckets whose permissions you wish to check. 


### Install Dependencies
This has only been tested with Python 2.7.10
1. Use virtualenv. 
2. Install the dependencies needed to run the samples. 
3. `$ pip install -r requirements.txt`

### Running the sample

1. Set the environment variable GOOGLE_CLOUD_PROJECT to one of your projects ProjectID ( the script will give you the names and ID's  for all the projects you have access to ) 
2. If GOOGLE_CLOUD_PROJECT is NULL the script will not run the bucket IAM check against any projects and the script will exit
3. `$ python mybuckets.py`
