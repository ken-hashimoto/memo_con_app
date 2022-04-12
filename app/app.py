from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.models import MemoContents,User
from models.database import db_session
from datetime import datetime
# from app import key
import pytz
import os
from hashlib import sha256
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")  #or key.SECRET_KEY
SALT = os.environ.get("SALT")  #or key.SALT
#関数--------------------------------------------
def is_login():
  if 'user' in session:
    return True
  return False
def try_logout():
  session.pop('user',None)
  return True
#------------------------------------------------
#index-------------------------------------------
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def save():
  text = request.form['Text']
  title = request.form['Title']
  if title=="":
    title = "無題"
  if is_login():
    content = MemoContents(session['user'],title,text,datetime.now(pytz.timezone('Asia/Tokyo')))
    db_session.add(content)
    db_session.commit()
    return jsonify({'result':'保存されました'})
  else:
    return jsonify({'result':'ログインしてください'})
#------------------------------------------------
#login-------------------------------------------
@app.route('/login',methods = ['GET','POST'])
def login():
  if request.method == 'GET':
    if is_login():
      return render_template('login.html',status = 'already_logged_in')
    else:
      return render_template('login.html',status = 'not_logged_in')
  if request.method == 'POST':
    userid = request.form.get('UserID','')
    password = request.form.get('pw','')
    user = User.query.filter_by(UserID=userid).first()
    if user:
        hashed_password = sha256((userid + password + SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session['user'] = userid
            return redirect('/')
        else:
            return render_template('login.html',status = 'error')
    else:
        return render_template('login.html',status = 'error')
#------------------------------------------------
#logout------------------------------------------
@app.route('/logout',methods = ['GET'])
def logout():
  if is_login():
    try_logout()
    return render_template('logout.html',status = 'already_logged_in')
  else:
    return render_template('logout.html',status = 'not_logged_in')
#------------------------------------------------
#mypage------------------------------------------
@app.route('/mypage',methods = ['GET','POST'])
def mypage():
  if request.method == 'GET':
    if is_login():
      all_memo = MemoContents.query.filter_by(UserID=session['user'])
      return render_template('mypage.html',all_memo = all_memo)
    else:
      return redirect('/login')
  if request.method == 'POST':
    check_num = list(map(int,request.form['del_num'].split(',')))
    if is_login():
      for num in check_num:
        content = MemoContents.query.get(num)
        db_session.delete(content)
        db_session.commit()
      return jsonify({'result':'削除が完了しました'})
    else:
      return jsonify({'result':'ログインしてください'})

@app.route('/mypage/<num>',methods=['GET'])
def mypage_record_get(num):
  if is_login():
    record = MemoContents.query.get(num)
    return render_template('mypage_record.html',record = record)
  else:
    return redirect('/login')
@app.route('/mypage/<num>',methods=['POST'])
def mypage_record_post(num):
  title= request.form.get('record_title','')
  content= request.form.get('record_content','')
  if is_login():
    record = MemoContents.query.get(num)
    record.Title = title
    record.Memo = content
    db_session.add(record)
    db_session.commit()
    return redirect(url_for('mypage_record_get',num = num))
  else:
    return redirect('/login')
  
@app.route('/mypage/<num>/edit',methods=['GET'])
def record_edit(num):
  if request.method =='GET':
    if is_login():
      record = MemoContents.query.get(num)
      return render_template('mypage_record_edit.html',record=record)
    else:
      return redirect('/login')
#------------------------------------------------
#register----------------------------------------
@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    userid = request.form.get('UserID','')
    password = request.form.get('pw','')
    password_confirm = request.form.get('pw_confirm','')
    user = User.query.filter_by(UserID=userid).first()
    if user:
      return render_template('register.html',status ='exist_user')
    else:
      if password != password_confirm:
        return render_template('register.html',status ='wrong_password')
      hashed_password = sha256((userid + password + SALT).encode("utf-8")).hexdigest()
      user = User(userid, hashed_password)
      db_session.add(user)
      db_session.commit()
      session['user'] = userid
      return redirect('/')
  if request.method == 'GET':
    if is_login():
      return redirect('/mypage')
    else:
      return render_template('register.html')
#------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)