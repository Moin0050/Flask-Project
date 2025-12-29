from flask import Flask, render_template, request
import pywhatkit
import datetime
import time

app = Flask (__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        phone = request.form["phone"]
        message = request.form["message"]
#Get current time + 1 minute
        now = datetime.datetime.now()
        hour = now.hour 
        minute = now.minute + 1
# Adjust minute overflow
        if minute >= 60:
            minute = minute - 60
            hour = hour + 1
        # Send WhatsApp message
        pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=10)
        return "Message scheduled! Check WhatsApp Web."
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)