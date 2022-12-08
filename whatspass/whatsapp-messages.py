import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

def send_whatsapp_message(phoneNumber, msg, hour, minute):
    try:
        pywhatkit.sendwhatmsg(phoneNumber, msg, hour, minute)
        time.sleep(10)
        pyautogui.click()
        time.sleep(1)
        Controller().press(Key.enter)
        Controller().release(Key.enter)
        time.sleep(1)
        print("Message sent!")
    except Exception as e:
        print(str(e))

theMessage = random.choice(['Hi, How are you?',
             'How is your day?',
             emoji.emojize('I love you :sparkling_heart:'),
             emoji.emojize(':red_heart:", variant="emoji_type'),
             emoji.emojize(':beating_heart:'),
             emoji.emojize(':smiling_face_with_heart-eyes:')])

print(theMessage)
phoneNumber = "+16092024224"
numberOfMessages = 4
startingHour =23
endingHour =24
hour =23 #random.randrange(startingHour, endingHour)

minute =45

print(hour,minute)

seconds = time.time()
result = time.localtime(seconds)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)


pywhatkit.sendwhatmsg(phoneNumber, theMessage, hour, minute)