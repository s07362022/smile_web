from enum import unique
from operator import index
import os
from re import template 
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, session, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import  Migrate
from flask_mail import Mail
from threading import Thread
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import jsonify
from datetime import datetime


#  取得啟動文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
###############SQL####################
app.config['SECRET_KEY'] = 's07362022'

app.config['SQLALCHEMY_DATABASE_URI'] =\
    "mysql+pymysql://root:0000@localhost:3306/ncku_w" 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  #減少 memory 的消耗
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)   #指到 sqllist
###############SQL####################
migrate = Migrate(app,db)
boostrap = Bootstrap(app=app)
ISOTIMEFORMAT = '%H%M%S'
###### SQL #########
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='0000',
                                    database='ncku_w')

cursor = connection.cursor()
username_list=[]#get_sql1()
id_list =[]#get_sql2()
def get_sql1():
    #with cursor  as cursor1:
    # 查詢資料SQL語法
    command = "SELECT `username` FROM ncku_w  "
    # 執行指令
    cursor.execute(command)
    # 取得所有資料
    result = cursor.fetchall()
    #print(type(result))
    for i in range(len(result)):
        username_list.append(result[i][0])
    #print(len(username_list))
    #print(username_list)
    return username_list

def get_sql2():
    #with cursor  as cursor1:
    # 查詢資料SQL語法
    command = "SELECT `id` FROM ncku_w  "
    # 執行指令
    cursor.execute(command)
    # 取得所有資料
    result = cursor.fetchall()
    for i in range(len(result)):
        id_list.append(result[i][0])
    #print(len(password2_list))
    #print(password2_list)
    return id_list

def web_img(img_local_path):
    import base64
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()
        #print(img_stream)
    return img_stream
img_local_path = "F:\\nuck\\web\\static\\image\\one1.png"
img_local_path2 = "F:\\nuck\\web\\static\\image\\two.png"
img_local_path3 = "F:\\nuck\\web\\static\\image\\tgr.png"

###### SQL ######


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/page1', methods=['GET', 'POST'])
def page1():
    pic1 = web_img(img_local_path)
    pic2 = web_img(img_local_path2 )
    # if request.method == 'POST':
    #     print("ss")
    #     return redirect(url_for('page2'))
    return render_template('pag1.html',pic1=pic1,pic2=pic2)

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    
    return render_template('page2.html')

@app.route('/page4', methods=['GET', 'POST'])
def page4():
    pic3 = web_img(img_local_path3)
    return render_template('page4.html',pic3=pic3)

@app.route('/out', methods=['GET', 'POST'])
def out():
    from form import FormRegister
    from model import UserReister   
    form =FormRegister()
    if form.validate_on_submit():
        user = UserReister(
            username = form.username.data,
            id = form.id.data,
            hpname = form.hpname.data,
            time_  = str( datetime.now().strftime(ISOTIMEFORMAT))
            #email = form.email.data,
            #password2 = form.password.data
        )
        print('id:',form.id.data,' name: ',form.username.data,'hpname: ',form.hpname.name)
        db.session.add(user)
        db.session.commit()
        return 'Success Thank You'
        #return redirect(url_for('login'))#'Success Thank You'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=8087,debug=True) #use_reloader=True
    