import speedtest
import requests
import subprocess
import re

class WebAnalyzer():
    def __init__(self,hostname):
        self.upload = 0
        self.download = 0
        self.connection = ''
        self.response = ''
        self.lost = ''
        self.hostname = hostname

    def CheckDownloadUsingSpeedtest(self):
        test = speedtest.Speedtest()
        self.upload = test.upload()
        self.download = test.download()


    def CheckInternetConnection(self):
        try:
            response = requests.get("https://google.com/")
            self.connection = "Connected to the Internet"
        except requests.ConnectionError:
            self.connection = "No connection"
    def host(self):
        try:
            self.response = subprocess.check_output(
                ['ping', '-n', '5', self.hostname],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            pattern = u"\d{0,}\%"
            self.lost = int(re.findall(pattern, self.response)[0].replace("%", ''))
            if self.lost < 60:
                return (self.host)
        except Exception as err:
            print(f"Something went wrong. Error is {err}")
