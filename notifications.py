from datetime import datetime, timedelta
import time
import smtplib
from email.mime.text import MIMEText

class NotificationManager:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_sleep_alert(self):
        msg = MIMEText("It's time to sleep! Try to get some rest for better health.")
        msg['Subject'] = 'Sleep Alert'
        msg['From'] = self.email
        msg['To'] = self.email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)

    def schedule_sleep_alert(self):
        while True:
            current_time = datetime.now()
            alert_time = current_time.replace(hour=23, minute=30, second=0, microsecond=0)

            if current_time >= alert_time and current_time < alert_time + timedelta(minutes=1):
                self.send_sleep_alert()
                time.sleep(60)  # Wait a minute before checking again
            time.sleep(30)  # Check every 30 seconds

# Example usage:
# notification_manager = NotificationManager('your_email@gmail.com', 'your_password')
# notification_manager.schedule_sleep_alert()