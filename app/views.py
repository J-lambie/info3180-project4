from app import app,db
from flask import Flask, abort, request, jsonify, g, url_for, render_template,session
import requests
from image_getter import image_dem
from models import User,Wishlist

@app.route('/')
def home():
    return app.send_static_file("base.html")

@app.route('/api/thumbnails/process', methods=['POST'])
def thumbnails():
    if request.method == 'POST' :
        url=request.form['url']
        r=requests.get(url)
        if r.status_code==200:
            thumbnails=image_dem(url)
            obj={'error': 'null','data':{'Thumbnail':thumbnails},'message':'success'}
            json=jsonify(obj)
            return json
        json=jsonify({'error':"1",'data':{},'message':'failure'})
        return json
    else:
        return "There is no get request"

@app.route('/api/user/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(email=email,name=name,password=password)
        db.session.add(new_user)
        db.session.commit()
        obj={'error':'null','data':{'token':'blank','expires':'time','user':{'id':new_user.get_id(),'email':new_user.email,'name':new_user.name},},'message':'Success'}
        return jsonify(obj)
    return render_template("register.html")

@app.route('/api/user/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        user=User.query.filter(User.email==email).first()
        if not user:
            obj={'error':'1','data':{},'message':'Bad username or password'}
            return jsonify(obj)
        if password==user.password:
            obj={'error':'null','data':{'token':'blank for now','expires':'time','user':{'id':user.user_id,'email':user.email,'name':user.name},},'message':'Sucess'}
            return jsonify(obj)
        else:
            obj={'error':'1','data':{},'message':'Bad username or password'}
            return jsonify(obj)

    return jsonify({'result':'page loaded'});   

@app.route('/api/user/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'logged out success'})
    
@app.route('/api/user/<int:id>/wishlist',methods=['POST','GET'])
def wishlist(id):
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        url=request.form['url']
        thumbnail=request.form['thumbnail']
        obj={'error':'null','data':{'wishes':{'title':title,'description':description,'url':url,'thumbnail':thumbnail},'message':'sucess'},}
        new_wishlist=Wishlist(title,description,url,thumbnail,id)
        db.session.add(new_wishlist)
        db.session.commit()
        return jsonify(obj)
    if request.method =='GET':
        wishlist=Wishlist.query.get(id)
        if wishlist is None:
            obj={'error':'1','data':{},'message':'No such wishlist exist'}
        else:
            obj={'error':'null','data':{'wishes':{'title':wishlist.title,'description':wishlist.description,'url':wishlist.url,'thumbnail':wishlist.thumbnail},'message':'sucess'},}
        return jsonify(obj)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)