from analyzer import WebAnalyzer
from Ping import host
import threading
if __name__ == "__main__":
    host_name = input("Введите имя хоста ")
    analyzer = WebAnalyzer()
    lock = threading.Lock()
    isConnected = analyzer.CheckInternetConnection()
    speed = analyzer.CheckDownloadUsingSpeedtest()
    thread1 = threading.Thread(target=isConnected)
    thread2 = threading.Thread(target=speed)
    if isConnected:
        print("Connected to the Internet")
    else:
        print("No connection")
    print(str(speed["download"]//(1024*1024))+" MB")
    print(str(speed["upload"]//(1024*1024))+" MB")
    host(host_name)
