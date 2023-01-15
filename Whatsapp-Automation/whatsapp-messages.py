"""
Open a terminal or command prompt
If you want to create a virtual environment (recommended), run the following commands:
Copy code
pip install virtualenv
virtualenv my_env
source my_env/bin/activate
Install the required libraries by running the following commands:
Copy code
pip install pywhatkit
pip install PyAutoGUI
pip install pynput
pip install emoji
Open WhatsApp in your default browser (https://web.whatsapp.com/) and scan the QR code with your phone to log in.
Run the script and allow the keyboard library to access your keyboard when prompted.
Note: These instructions assume that you have Python and pip installed on your system. If not, you will need to install those first.

"""


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

phoneNumber = "+1609202***"

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
