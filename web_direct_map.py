import datetime
import concurrent.futures
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "URL or IP Address here!"
extension = ""
status_codes = [200, 204, 301, 302, 307]
file = open("C:/PATH_TO_WORDLIST")
data = file.read()
file.close()
word_list = data.split("\n")

now = datetime.datetime.now()
print("Scan started at " + str(now.strftime("%X | %x")))

def directory_scanner(word):
    r = requests.get(url + word + extension, verify=False)
    if r.status_code in status_codes:
        now = datetime.datetime.now()
        print(now.strftime("%X | %x") + " | Discovered " + url + word + extension + " [Status: " + str(r.status_code) + "]")
    else:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(directory_scanner, word_list)
