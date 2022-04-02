"""A program for monitoring whether space is full in any ULCS courses."""
import time
import threading
from threading import Event
import smtplib
import signal
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from config import sender_email, sender_password, receiver_email

SENDER_EMAIL = sender_email
SENDER_PASSWORD = sender_password # if using Gmail, check https://support.google.com/accounts/answer/185833
RECEIVER_EMAIL = receiver_email
UPDATE_INTERVAL = 5  # Time to wait between requests in seconds

exit = Event()


class Monitor:
    """A Web page monitor."""

    def monitor_run(self):
        """Run monitor thread."""
        while not exit.is_set():
            url = "https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2410EECS" + \
                self.course_num + "001&termArray=f_22_2410"
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}

            try:
                response = requests.get(url, headers=headers, timeout=10)
                response.encoding = "utf-8"
                page = response.text
            except requests.exceptions.RequestException as e:
                print(e)
                exit.wait(UPDATE_INTERVAL)
                continue

            # parse the page
            soup = BeautifulSoup(page, "html.parser")
            divs = soup.find_all("div", class_="col-md-1")
            seats = []
            for div in divs:
                children = div.find_all("div")
                for child in children:
                    child_str = child.string
                    if child_str == "Open Seats:":
                        for s in div.text.split():
                            if s.isdigit():
                                seats.append(int(s))
            if not seats:
                exit.wait(UPDATE_INTERVAL)
                continue
            # print query result
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(f"{current_time} EECS {self.course_num} has {min(seats)} seats.")
            if min(seats) > 0:
                exit.wait(UPDATE_INTERVAL)
            else:
                print(self.course_num + " is full now!")
                msg = MIMEText("Register EECS " + self.course_num + " now!")
                msg["Subject"] = f"[EECS {self.course_num}] Course Registration Reminder"
                msg["From"] = SENDER_EMAIL
                msg["To"] = RECEIVER_EMAIL
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.login(SENDER_EMAIL, SENDER_PASSWORD)
                s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
                s.quit()
                break

    def __init__(self, course_num):
        self.course_num = str(course_num)
        threading.Thread(target=self.monitor_run).start()


def quit(signo, _frame):
    """Handle interuptions."""
    print(f"Interrupted by {signo}, shutting down")
    exit.set()


def main():
    """Run multiple monitors."""
    # Add your course here.
    Monitor(477)
    Monitor(388)


if __name__ == "__main__":
    for sig in ("TERM", "HUP", "INT"):
        signal.signal(getattr(signal, "SIG"+sig), quit)
    main()
