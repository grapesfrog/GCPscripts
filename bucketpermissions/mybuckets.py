# Copyright 2017 Grace Mollison

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import argparse
import httplib2
import re
from dateutil.parser import parse
import httplib2
from google.cloud import resource_manager
from google.cloud import storage

filename = "bucketpermissions.txt"
# GOOGLE_CLOUD_PROJECT <- set this to project id to pick up new project
# If doing programatically Then need to spawn a sub process whch seems overkill :-(


def create_file():
   # delete file if it already exists
  if os.path.exists(filename):
    os.remove(filename)
    print("Deleting existing file & creating file %s" % filename)
    f= open(filename,"a+")
  else:
    print("File  %s does not exist will create empty file." % filename)
    f= open(filename,"a+")
    f.close() 

def List_projects():
    
    crm = resource_manager.Client()
    for project in crm.list_projects():
    # while projects is not None: 
      print(project)  
    # split to get projectid
    # Format of project object :  <Project: u'projectname' (u'projectid')>
      projectstring = str(project)
      projectstring = projectstring.split("(u'") 
      projectid = projectstring[1]
      projectid = projectid[:-3]
      print(projectid)
       

def List_bucket():
    GOOGLE_CLOUD_PROJECT = os.getenv('GOOGLE_CLOUD_PROJECT')
    
    if GOOGLE_CLOUD_PROJECT is None:
      print( "Google_Cloud_project is set to %s Exiting application"  % GOOGLE_CLOUD_PROJECT)
      exit()
    storage_crm = storage.Client()
    for bucket in storage_crm.list_buckets():
        print(bucket)
       # Caller requires storage.buckets.getIamPolicy access on buckets
        policy = bucket.get_iam_policy()
        for role in policy:
         members = policy[role]
         print('Role: {}, Members: {}'.format(role, members)) 
         mystring = ('Role: {}, Members: {}'.format(role, members)) 
         with open(filename, "a+") as bucket_permissions_file:
          # For this example i"m just writing toa text file you may wish to write to CloudSQl or BQ
          bucket_permissions_file.write("{0} : " .format(bucket))
          bucket_permissions_file.write("{0} \n".format(mystring))

        
         

def main():
        
    create_file()
    List_projects()
    List_bucket()
	 

if __name__ == '__main__':
  main()


