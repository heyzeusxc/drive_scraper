print("*" * 21)

import csv, math, os, shutil, sys
import pandas as pd
import gspread

from config import google_auth
from helpers.file_search import find_files
from helpers.set_fstrength import set_filter_strength

cwd = input("Enter Drive Or Folder To Scan: ")

while os.path.isdir(cwd) is not True:
    cwd = input("Not A Drive Or Folder, Try Again: ")
else:
    print("OK")
    print("")

print("Scanning: " + cwd)
print("")

files = []
total_file_size = 0

total_drive_size, used_drive_size, free_drive_size = shutil.disk_usage(cwd)

firstRow = ["Drive", "Total Size", "Free Size"]
secondRow = ["File", "Size", "%"]


def convert_bytes(bytes_to_convert):
    if bytes_to_convert == 0:
        return 0
    size_name = ("B", "KB", "MB", "GB", "TB", "PB")
    i = int(math.floor(math.log(bytes_to_convert, 1024)))
    p = math.pow(1024, i)
    s = round(bytes_to_convert / p, 2)
    return "%s %s" % (s, size_name[i])


drive = find_files(cwd)

print(str(len(drive)) + " files found")
print("")

for x in drive:
    total_file_size += x[1]

actual_free_size = total_drive_size - total_file_size

print("Writing CSV")
print(cwd + "drive_info.csv)")
print("")

with open(cwd + "/drive_info.csv", "w") as f:
    typer = csv.writer(f)
    typer.writerow(firstRow)
    typer.writerow(
        [cwd, convert_bytes(total_drive_size), convert_bytes(actual_free_size)]
    )
    typer.writerow(secondRow)
    for x in drive:
        typer.writerow(
            [
                x[0],
                convert_bytes(x[1]),
                str(round((x[1] / total_drive_size) * 100, 3)) + " %",
            ]
        )
    f.close()

print("Finished Writing CSV")
print("")

file_paths = ["Free Space - " + str(convert_bytes(actual_free_size))]
file_sizes = [actual_free_size]
file_percentages = [round((actual_free_size / total_drive_size) * 100, 5)]

for x in drive:
    file_paths.append(x[0] + " - " + str(convert_bytes(x[1])))
    file_sizes.append(convert_bytes(x[1]))
    file_percentages.append(round((x[1] / total_drive_size) * 100, 5))

df = pd.DataFrame({"File": file_paths, "Size": file_sizes, "Percent": file_percentages})

fs = set_filter_strength()

filtered_df = df.query(fs)

plot = (
    filtered_df.groupby(["File"])
    .sum()
    .plot(
        kind="pie",
        y="Percent",
        legend=False,
        figsize=(100, 100),
        autopct="%.2f%%",
        pctdistance=0.75,
        fontsize=24,
        radius=0.25,
        rotatelabels=180,
    )
)

plot.set_ylabel("")

img = plot.get_figure()
img.savefig(cwd + "/drive_info.png")

print("Graphs Generated")
print("")

print(cwd + "/drive_info.png")
print("")

print("*" * 21)
