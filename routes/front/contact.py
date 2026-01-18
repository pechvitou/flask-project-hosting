from app import app
from flask import render_template
# Home page
@app.route('/contact')
def contact():
    return render_template('contact.html')