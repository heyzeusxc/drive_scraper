# drive_scraper

Written in Python

Requirements: A Google Service Account
https://cloud.google.com/iam/docs/service-accounts

More info - https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/#h2_6

After getting your Google Service Account credentials JSON file, place it in the 'drive_scraper' folder with the name 'google_key.json' or another name which can be changed in 'config.py'

This scrapes a selected folder or drive to compile a CSV of all the files in it and calculates how much space on the drive they take up percentage wise.
A CSV named 'drive_info.csv' is created in the selected drive or folder.

A Google Sheet file is also created or updated with an option to filter out smaller files and then shared with all the emails listed in the 'share_emails' variable in 'config.py'

May need to 'pip install gspread' if it doesn't install correctly.
