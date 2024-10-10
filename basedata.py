import os
import datetime
if not os.path.isdir('C:/Program Files/webanalizator'):
    os.makedirs('C:/Program Files/webanalizator')
with open('C:/Program Files/webanalizator/dateinter','a') as file:
    file.write(datetime.datetime.now())


