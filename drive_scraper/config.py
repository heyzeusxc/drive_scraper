import json, os

from helpers.file_search import find_files

share_emails = ["email@email.com"]

google_key = "google_key.json"

files = find_files(os.getcwd())

for x in files:
    if google_key in x[0]:
        google_key_path = x[0]

with open(google_key_path, "r") as j:
    google_auth = json.loads(j.read())
