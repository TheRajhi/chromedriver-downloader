import requests
import os
import requests_html
import colorama
from colorama import Fore

cwd = os.getcwd()

# user inputed version
cver = input('what is your chrome version? (first 3 digits): ')

print(Fore.CYAN, "Gathering data...")
# get the list of all versions
session = requests_html.HTMLSession()
r = session.get('https://chromedriver.storage.googleapis.com/index.html')
r.html.render(sleep=5, timeout=8)
for item in r.html.xpath("/html/body/table/tbody"):
    data = item.text
print(Fore.GREEN, "All data gathered!")

# write it in a txt file for easier parsing
with open(rf"{cwd}\temp.txt", 'w') as f:
    f.write(data)

# read it and assort it on a list
with open(rf"{cwd}\\temp.txt") as f:
    sources = f.read().splitlines()
print(Fore.CYAN, "Data sorted")

# get all mini-versions of main version
versions = []
for i in sources:
    if i.startswith(cver):
        versions.append(i)
print(Fore.CYAN, f"Getting the latest of version {cver}")

# get the last of the mini-versions
lg = len(versions)
ver = versions[lg-1]
print(Fore.CYAN, f"Downloading version {ver} of the chromedriver...")
print(Fore.CYAN, "doesn't need to match perfectly, just the first 3 digits...")

# download the chromedriver
request = requests.get(f'https://chromedriver.storage.googleapis.com/{ver}/chromedriver_win32.zip')
open(rf"{cwd}\\chromedriver_win32.zip", 'wb').write(request.content)
print(Fore.GREEN, "Chromedriver downloaded!")

input('press ENTER to close')
quit()



