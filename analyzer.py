import speedtest
import time
import requests


class WebAnalyzer():
    def __init__(self):
        pass

    def CheckDownloadUsingSpeedtest(self):
        test = speedtest.Speedtest()
        upload = test.upload()
        download = test.download()
        return {"upload": upload, "download": download}

    def CheckInternetConnection(self):
        try:
            response = requests.get("https://google.com/")
            return True
        except requests.ConnectionError:
            return False
