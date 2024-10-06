import schedule 
from api import get_hadith
import random
from winotify import Notification


random_hadith = get_hadith(random.randint(1,5))
source = random_hadith["source"]
hadith = random_hadith["text"]
message = f'It was narrated by {source} that "{hadith}"'

def send_hadith():
    notif = Notification(app_id="Motivational Hadith",
                        title="Daily Hadith!",
                        msg= message)
    notif.show()

schedule.every().day.at("19:18").do(send_hadith)
send_hadith()




