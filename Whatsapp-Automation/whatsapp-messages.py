import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

theMessage = random.choice(['Hi, How are you?',
             'How is your day?',
             emoji.emojize('I love you :sparkling_heart:'),
             emoji.emojize(':red_heart:"'),
             emoji.emojize(':beating_heart:'),
             emoji.emojize(':smiling_face_with_heart-eyes:')])
print(theMessage)

phoneNumber = "+16092024224"

result = time.localtime(time.time())
print("tm_hour:", result.tm_hour)
print("tm_min",result.tm_min+1)

try:
    pywhatkit.sendwhatmsg(phoneNumber, theMessage, result.tm_hour,result.tm_min+1)
    time.sleep(5)
    pyautogui.click()
    time.sleep(1)
    Controller().press(Key.enter)
    Controller().release(Key.enter)
    time.sleep(1)
    print("Message sent!")
except Exception as e:
    print(str(e))
