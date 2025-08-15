from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage
import os
app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sitemaps')
def sitemaps():
    return render_template('sitemaps.xml')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects/queensgrove')
def queensgrove():
    return render_template('projects/queensgrove.html')

@app.route('/projects/silverton')
def silverton():
    return render_template('projects/silverton.html')

@app.route('/projects/wricklemarsh')
def wricklemarsh():
    return render_template('projects/wricklemarsh.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = EmailMessage()
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash("Failed to send message.", "danger")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)