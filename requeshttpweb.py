#!/usr/bin/python3
import requests

site=$1

site = requests.get("$site")
status = site.status_code

if status == 200:
    print("Página OK!")
else:
    print("Página fora do ar")
