from flask import Flask, render_template, request, redirect
import dao
from app import app,login
from flask_login import login_user




@app.route('/')
def index():
    kw= request.args.get('kw')
    cates = dao.load_categories()
    product = dao.load_products(kw=kw)

    return render_template('index.html',categories=cates, products=product)
@app.route('/products/<id>')
def details(id):
    return render_template('detail.html')

# @app.route('/admin/login',methods=['post'])
# def login_admin_process():
#     request.form.get('name')
#     request.form.get('passwd')
@app.route('/admin/index',methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['pwd']

    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u)

    return redirect('/admin')


@login.user_loader
def get_user_by_id(id):
    return dao.get_user_by_id(id)

if __name__=='__main__':
    from app import admin
    app.run(debug=True)
