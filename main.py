from analyzer import WebAnalyzer
import threading
import datetime
if __name__ == "__main__":
    host_name = input("Введите имя хоста ")
    start = datetime.datetime.now()
    analyzer = WebAnalyzer(host_name)
    lock = threading.Lock()
    isConnected = analyzer.CheckInternetConnection()
    speed = analyzer.CheckDownloadUsingSpeedtest()
    pingcheck = analyzer.host()
    thread1 = threading.Thread(target=isConnected)
    thread2 = threading.Thread(target=speed)
    thread3 = threading.Thread(target=pingcheck)
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    finish = datetime.datetime.now()
    print(str(finish - start))

