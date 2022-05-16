# FinalYearProject

Description of Files --
1. MobileDetectionTestingCode.pynb - Code for testing users using mobile phone
2. 3000.weights - Object detection algorithm model weights (YOLO V4)
3. ALARM.wav - Alert song
4. obj.names - Names of object(person talking, person texting, person not using phone)
5. yolov4-tiny-obj.cfg - Configuration file of Yolo model (Contains all the layers, windows, filters used in CNN for building object detection algorithm)
6. ProjectWebsite/static/style.css - css file for login.html
7. ProjectWebsite/static/styles.css - css file for main.html
8. ProjectWebsite/templates/login.html - first page of website for login
9. ProjectWebsite/templates/main.html - main page showing records collected of mobile phone use
10. ProjectWebsite/app.py - flask app connecting frontend backend


How to run?

1. Open MobileDetectionTestingCode.pynb
2. Change NUMBER_PLATE accordingly - Pallavi - BR-12345, Ankita - BR-89014, Parimal - WB-234588, Mayank - WB-890012
3. Run all cells
4. To exit the detection window press enter
5. Open command prompt inside ProjectWebsite folder
6. Type - python app.py
7. Enter username and password and login - pallavisinha - 1205, parimalmahata - 0807, ankitagupta - 3456, mayankkumar - 1705
8. The records will be shown on website
9. Click on send notification button to send email
