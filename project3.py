import easyimap as e
from win10toast import ToastNotifier
from plyer import notification
import time
password = "yourpassword"
mail = "youremail@gmail.com"
server = e.connect("imap.gmail.com", mail, password)
server.listids()
email = server.mail(server.listids()[0])
toast = ToastNotifier()
print(email.title)
print(email.from_addr)
print(email.body)
message = f"{email.title, email.from_addr, email.body}"
notification.notify(
        title = "New Email",
        message = message,
        timeout = 6)