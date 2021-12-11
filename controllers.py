from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM itemstable")
    items = mycursor.fetchall()
    return render_template('index.html', items = items)



@app.route('/admin')
def admin():
    mycursor.execute("SELECT * FROM itemstable")
    items = mycursor.fetchall()
    return render_template('seller.html', items = items)





@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if request.method == 'GET':
        return render_template('post_form.html')
    if request.method == 'POST':
        _itemname = request.form['itemname']
        _price = request.form['price']
        _seller = request.form['seller']
        sql = 'INSERT INTO itemstable (itmename, price, seller) VALUES (%s, %s, %s)'
        val = (_itemname, _price, _seller)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM itemstable")
        items = mycursor.fetchall()
        return render_template('index.html', items = items)


@app.route('/getitems')
def getitems():
    mycursor.execute("SELECT * FROM itemstable")
    items = mycursor.fetchall()
    return render_template('index.html', items = items)





@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM itemstable WHERE ID={id}')
        items = mycursor.fetchone()
        return render_template('edit.html', item = items)
    if request.method == 'POST':
        _itemname = request.form['itemname']
        _price = request.form['price']
        _seller = request.form['seller']
        sql = f'UPDATE itemstable SET itmename = %s, price = %s, seller=%s WHERE ID = %s'
        values = (_itemname, _price, _seller, id)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.execute("SELECT * FROM itemstable")
        items = mycursor.fetchall()
        return render_template('index.html', items = items)


@app.route('/delete/<int:id>')
def delete_item(id):
    sql = f'DELETE FROM itemstable WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM itemstable")
    items = mycursor.fetchall()
    return render_template('index.html', items = items)




@app.route('/details/<int:id>')
def customer_details(id):
    mycursor.execute(f'SELECT * FROM customers WHERE ID={id}')
    customer = mycursor.fetchone()
    return render_template('customer_detail.html', customer = customer)



if __name__ == '__main__':
    app.run()