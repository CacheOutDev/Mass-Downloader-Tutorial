import requests
import re
import certifi
import os

# Lines 7 - 14: opens input.txt and adds each link to the "files" list as individual strings
with open("input.txt", "r") as textFile:
    lines = textFile.readlines()

files = []

for line in lines:
    file = line.strip()
    files.append(file)

for file in files:

    # Requests get() method sends a GET request to each file link
    # Certifi provides a list of trusted certificates which allows Requests to securely connect via HTTPS communication
    response = requests.get(file, verify=certifi.where())

    # Lines 23 - 27: Removes the link address from the file name to improve readability
    link_address = "https://www.website.com/file/path/"
    file = file.replace(link_address, "")

    file = re.sub(r"\d+|/", "", file)
    file = file.replace("-", "")

    # Lines 30 - 37: If the link returns a 200 status code, then the file is renamed to include the file path to the Downloads folder and is downloaded to said folder
    if response.status_code == 200:

        file_path = "/Users/username/Downloads"
        file = os.path.join(file_path, file)

        open(file, "wb").write(response.content)

        print("Downloaded: " + str(file))

    # If the link returns a 404 error, then the file is not downloaded and the message below gets printed
    elif response.status_code == 404:
        print("404 Error: " + file)

    # If the link returns a status code other than 200 or 404, then the file is not downlaoded and the message below gets printed
    else:
       print(response.status_code + ": " + file)
