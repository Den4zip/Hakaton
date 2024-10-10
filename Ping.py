import subprocess
import os
import re
import pyautogui
def host(hostname):
    try:
        response = subprocess.check_output(
            ['ping', '-n', '5', hostname],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        print(response)
        pattern = u"\d{0,}\%"
        lost = int(re.findall(pattern, response)[0].replace("%", ''))
        print(f"Lost {lost}%")
        if lost < 60:
            return (host)
        else:
            os.system(u'c:/watchdog/k.bat'), pyautogui.press('F10')
    except Exception as err:
        print(f"Something went wrong. Error is {err}")
