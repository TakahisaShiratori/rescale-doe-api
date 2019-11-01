import json
import os
import requests

api_token = os.environ["RESCALE_API_KEY"]
api_token_in_header = "Token " + api_token
platform = os.environ["RESCALE_PLATFORM"]

new_job_name = "OpenFOAM DOE submitted with API"
new_input_filename = "airfoil2D_DOE.zip"
new_doesetting_filename = "freestreamvalue.csv"
new_template_filename = "utemplate"
job_config_filename = "doe_job_config.json"

# Upload an input file
print("# Uploading an input file")
url = "https://" + platform + "/api/v2/files/contents/"
raw_reply = requests.post(
  url,
  headers={'Authorization': api_token_in_header},
  files={"file": open(new_input_filename, "rb")}
)
uploaded_input_file = json.loads(raw_reply.text)
print("- " + uploaded_input_file["name"] + " have been uploaded as File ID " + uploaded_input_file["id"])

# Upload a DOE setting file
print("# Uploading a DOE setting file")
url = "https://" + platform + "/api/v2/files/contents/"
raw_reply = requests.post(
  url,
  headers={'Authorization': api_token_in_header},
  files={"file": open(new_doesetting_filename, "rb")}
)
uploaded_doesetting_file = json.loads(raw_reply.text)
print("- " + uploaded_doesetting_file["name"] + " have been uploaded as File ID " + uploaded_doesetting_file["id"])

# Upload a template file
print("# Upload a template file")
url = "https://" + platform + "/api/v2/files/contents/"
raw_reply = requests.post(
  url,
  headers={'Authorization': api_token_in_header},
  files={"file": open(new_template_filename, "rb")}
)
uploaded_template_filename = json.loads(raw_reply.text)
print("- " + uploaded_template_filename["name"] + " have been uploaded as File ID " + uploaded_template_filename["id"])

# Read job configuration
print("# Reading job configuration")
with open(job_config_filename) as f:
  job_config = json.load(f)

# Modify job configuration
print("# Modifying job configuration")
job_config["name"] = new_job_name
job_config["jobanalyses"][0]["inputFiles"] = [{"id": uploaded_input_file["id"]}]
job_config["paramFile"] = {"id": uploaded_doesetting_file["id"]}
job_config["jobanalyses"][0]["templateTasks"][0]["templateFile"] = {"id": uploaded_template_filename["id"]}

# Create a job
print("# Creating a job")
url = "https://" + platform + "/api/v2/jobs/"
raw_reply = requests.post(
  url,
  headers={'Authorization': api_token_in_header},
  json=job_config
)
created_job = json.loads(raw_reply.text)
print("## Created Job")
print("- Job ID: " + created_job["id"])
print("- Job Name: " + created_job["name"])

# Submit the job
print("# Submitting the job")
url = "https://" + platform + "/api/v2/jobs/" + created_job["id"] + "/submit/"
requests.post(
  url,
  headers={'Authorization': api_token_in_header}
)

# Get a status of the submitted job
url = "https://" + platform + "/api/v2/jobs/" + created_job["id"]
raw_reply = requests.get(
  url,
  headers={'Authorization': api_token_in_header}
)
submitted_job = json.loads(raw_reply.text)
print("## Submitted Job")
print("- Job ID: " + submitted_job["id"])
print("- Job Name: " + submitted_job["name"])
