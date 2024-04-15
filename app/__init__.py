from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Import routes module to ensure routes are registered with the application
from app import routes
