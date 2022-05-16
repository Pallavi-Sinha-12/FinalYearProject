from flask import Blueprint, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from flask import Flask
from werkzeug.utils import secure_filename
from bson.binary import Binary
from PIL import Image
import io
import base64
from email.message import EmailMessage
import smtplib

from flask_pymongo import PyMongo
mongo = PyMongo()

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.akvcd.mongodb.net/My_Database?retryWrites=true&w=majority'
mongo.init_app(app)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/main')
def main():
    mobile_users_collection = mongo.db.MobilePhoneUsers
    users = mobile_users_collection.find()
    imgs = []
    number_plates = []
    times = []
    ids = []
    for user in users:
        encoded_img_data = user['image']
        data = encoded_img_data.decode('utf-8')
        imgs.append(data)
        number_plates.append(user['number_plate'])
        times.append(user['time'])
        ids.append(user['_id'])
    return render_template('main.html', imgs = imgs, number_plates = number_plates , times = times, ids = ids)



@app.route('/login', methods = ['POST'])
def login():
    users = mongo.db.AuthorizedUsersDatabase
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if request.form['password'] == login_user['password']:
            #return render_template('main.html')
            return redirect(url_for('main'))
            

    return redirect(url_for('index'))


@app.route('/main/sendNotification/<id>')
def sendNotification(id):
    mobile_users_collection = mongo.db.MobilePhoneUsers
    registered_users_contact_collection = mongo.db.RegisteredUsersContacts
    user = mobile_users_collection.find_one({'_id':ObjectId(id)})
    number_plate = user['number_plate']
    body = "You have been found to use mobile phone in the vehicle with number plate " + number_plate + " at time" + str(user['time']) + ". Please submit 1000 rupees fine at police station"
    subject = "Notice for fine submission"
    contact = registered_users_contact_collection.find_one({'number_plate' : number_plate})
    to = contact['email_id']
    email_alert(subject, body, to)
    mobile_users_collection.delete_one({'_id' : ObjectId(id)})
    return redirect(url_for('main'))

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "pythonprojectemailalerts@gmail.com"
    msg['from'] = user
    password = "zzbhaopsjbqsehyt"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()



if __name__ == '__main__':
    app.run(debug = True)
