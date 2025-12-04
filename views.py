from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import sqlite3
# from Kruviz_Pac.auth import authenticate_user, register_user


app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    products = [
        {'img': 'sample_1.jpg', 'name': 'Classic White Tee', 'description': 'Premium cotton, timeless style for everyday comfort.'},
        {'img': 'sample_1.jpg', 'name': 'Graphic Tee', 'description': 'Bold designs that make a statement.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_1.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'}
    ]
    return render_template('Home.html', products=products)

#New_lanunch dynamic content loading
@app.route('/new_lanunch')
def new_lanunch():
    # You can also fetch this data from a database, file, etc.
    new_lanunch_details = [
        {'img': 'sample_2.jpg', 'name': 'Classic White Tee', 'description': 'Premium cotton, timeless style for everyday comfort.'},
        {'img': 'sample_2.jpg', 'name': 'Graphic Tee', 'description': 'Bold designs that make a statement.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'}
    ]
    return jsonify(new_lanunch_details)

#New_Arrival dynamic content loading
@app.route('/get_content')
def get_content():
    # You can also fetch this data from a database, file, etc.
    get_content_details = [
        {'img': 'sample_2.jpg', 'name': 'Classic White Tee', 'description': 'Premium cotton, timeless style for everyday comfort.'},
        {'img': 'sample_2.jpg', 'name': 'Graphic Tee', 'description': 'Bold designs that make a statement.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'},
        {'img': 'sample_2.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'}
    ]
    return jsonify(get_content_details)


#Best_Seller dynamic content loading
# @app.route('/get_content')
# def get_content():
#     # You can also fetch this data from a database, file, etc.
#     new_content = {
#         "title": "Flask Dynamic Content",
#         "message": "This content was loaded from the server without reloading the page!"
#     }
#     return jsonify(new_content)


# @app.route('/get_content')
# def get_content():
#     # You can also fetch this data from a database, file, etc.
#     new_content = {
#         "title": "Flask Dynamic Content",
#         "message": "This content was loaded from the server without reloading the page!"
#     }
#     return jsonify(new_content)





@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('cart'))
        else:
            return render_template('sign in .html', error='Invalid credentials')
    return render_template('sign in .html')

# @app.route('/cart')
# def cart():
#     if 'username' not in session:
#         return redirect(url_for('signin'))
#     username = session['username']
#     conn = sqlite3.connect('kruviz.db')
#     c = conn.cursor()
#     c.execute('SELECT id FROM users WHERE username = ?', (username,))
#     user = c.fetchone()
#     cart_items = []
#     if user:
#         user_id = user[0]
#         c.execute('SELECT item, quantity FROM cart WHERE user_id = ?', (user_id,))
#         cart_items = c.fetchall()
#     conn.close()
#     return render_template('cart.html', cart_items=cart_items, username=username)

if __name__ == '__main__':
    app.run(debug=True)
