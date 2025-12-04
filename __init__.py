# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     details = [
#         {'img': 'sample_1.jpg', 'name': 'Classic White Tee', 'description': 'Premium cotton, timeless style for everyday comfort.'},
#         {'img': 'sample_2.jpg', 'name': 'Graphic Tee', 'description': 'Bold designs that make a statement.'},
#         {'img': 'sample_3.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'}
#     ]
#     return details
    
#     return render_template('Home.html')

# home()
# details = [
#         {'img': 'sample_1.jpg', 'name': 'Classic White Tee', 'description': 'Premium cotton, timeless style for everyday comfort.'},
#         {'img': 'sample_2.jpg', 'name': 'Graphic Tee', 'description': 'Bold designs that make a statement.'},
#         {'img': 'sample_3.jpg', 'name': 'V-Neck Tee', 'description': 'Sleek and stylish with a flattering V-neck cut.'}
#     ]

# for i in details:
#     print(i['name'], '-', i['description'])




# if __name__ == '__main__':
#     app.run(debug=True)