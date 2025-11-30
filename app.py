from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

# 1. Flask App Initialize karna
app = Flask(__name__)

# 2. Config load karna
app.config.from_object(Config)

# 3. Database Initialize karna
db = SQLAlchemy(app)

# --- ROUTES (URL Raste) ---

# Home Page Route
@app.route('/')
def home():
    return "<h1>Hello! Mummy ka Salon Project Start ho gya hai!</h1>"

# --- RUN SERVER ---
if __name__ == '__main__':
    # debug=True ka matlab hai agar error aaya to browser par dikhega (Development ke liye best)
    app.run(debug=True)