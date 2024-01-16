import cv2
from pyzbar.pyzbar import decode
import time
import mysql.connector

cam = cv2.VideoCapture(0)
cam.set(4, 640)
cam.set(6, 480)

camera = True




while camera == True:
    success, frame = cam.read()

    for i in decode(frame):
        f = open("demofile2.txt", "w")
        print(i.type)
        print(i.data.decode('utf-8'))
        f.write(i.data.decode('utf-8'))
        f.write("\n")
        f.close()
        time.sleep(6)
    
        conn = mysql.connector.connect(
        user='root', password='darshan@4924', host='127.0.0.1', database='Project') 

#Creating a cursor object using the cursor() method
        cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
        sql = 'INSERT INTO data(QR_CODE)VALUES (%s)' 
        f2= open("demofile2.txt", "r")
        values= (f2.readline(),)
        print(values)
        cursor.execute(sql,values)
        conn.commit()
        print("Data inserted")
        conn.close()
        

    cv2.imshow("OurQr_code_Scanner", frame)
    cv2.waitKey(1)
   
   
    