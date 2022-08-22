from flask import Flask
from views import views

"""
This is the main application logic file. 
"""
app = Flask(__name__)

# Register the Flask Blueprint with views
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    # Running on http://127.0.0.1:8000/
    app.run(debug=True, port=8000)
    