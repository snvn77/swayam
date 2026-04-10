# Automating Message Dispatch on WhatsApp Web Using Selenium

# Background
# Web automation tools are often used to reduce repetitive manual tasks. One common example is interacting with web-based messaging platforms 
# to send reminders, notifications, or test message workflows. WhatsApp Web, being a browser-based interface, can be automated using Selenium 
# to simulate real user actions such as clicking, typing, and pressing keys.
# This case study examines a Python-based Selenium script that automates sending multiple messages to a specific contact on WhatsApp Web.

# Objective
# The goal of the script is to:
# Open WhatsApp Web in a browser
# Allow the user to authenticate manually via QR code
# Search for a specific contact by name
# Open the chat window of that contact
# Send the same message multiple times at fixed intervals
# Close the browser session after completion

# Tools and Technologies Used
# Python
# Selenium WebDriver
# Google Chrome Browser
# ChromeDriver
# WhatsApp Web
# Workflow Explanation

# 1. Browser Initialization
# The script begins by initializing the Chrome WebDriver. This enables Python to control the Chrome browser programmatically.

# Key idea:
# The WebDriver acts as a bridge between Python commands and browser actions.

# 2. Loading WhatsApp Web
# The browser navigates to the WhatsApp Web URL. Since WhatsApp requires authentication, the script pauses implicitly while the user scans the QR code using their mobile WhatsApp application.

# Important observation:
# Automation does not bypass authentication. Human intervention is required at this step.

# 3. Identifying the Target Chat
# The script defines:
# A contact name
# A message string
# It then constructs an XPath expression that locates a chat whose title attribute contains the contact’s name. 
# WebDriverWait is used to ensure the element is loaded before interaction

# Concepts involved:
# XPath-based element selection
# Explicit waits to handle dynamic content

# 4. Opening the Chat
# Once the contact element is located, a click action opens the chat window.
# This simulates a real user selecting a chat from the chat list.

# 5. Locating the Message Input Box
# The script finds the message input field using its class name. This element is where text messages are typed.
# This step relies on understanding the DOM structure of WhatsApp Web.

# 6. Sending Messages in a Loop
# A loop sends the same message multiple times:
# The message text is typed
# The Enter key is pressed to send
# A delay is added between messages

# Why the delay matters:
# Prevents rapid-fire actions
# Reduces the risk of detection or UI failure
# Mimics human behavior

# 7. Closing the Session
# After sending all messages, the browser is closed gracefully using the quit method.
# This ensures system resources are released properly.


# selenium: Automates browser actions
# time: Used for delays (sleep)
# WebDriverWait + expected_conditions: Wait until elements load
# Keys: For keyboard actions (like Enter)
# By: Helps locate elements (XPath, class, etc.)

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('path_to_chromedriver.exe')

driver.get('https://web.whatsapp.com/')
# You need to scan QR code manually after browser opens

recipient_name = 'Naveen Seelam'
message_text = 'Message sent using Python'

xpath = f"//span[contains(@title, '{recipient_name}')]" # Build an XPath to find the chat by name
target = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,xpath))) # Waits up to 10 seconds for it to appear
target.click() # Clicks on it

input_box = driver.find_element(By.CLASS_NAME,"1Plpp")
# Finds the message input field using class name
# WhatsApp class names are dynamic (they change frequently)
# "1Plpp" may not work consistently

for i in range(50):
    input_box.send_keys(message_text) # Enters the message in the input field
    input_box.send_keys(Keys.RETURN) # Presses Enter after each message
    time.sleep(1) # Waits 1 second between sends

driver.quit() # Closes the browser

# Why is WebDriverWait preferred over using a fixed time.sleep() before locating the chat element?
#  It waits only until the required element becomes available, making the script more reliable    (Right Answer)
#  It reduces CPU usage of the Python program
#  It prevents WhatsApp from detecting automation
#  It speeds up QR code scanning



# What is the main limitation of using the contact’s name in the XPath selector?
#  It works only for group chats
#  It may fail if multiple contacts share similar names    (Right Answer)
#  It cannot locate encrypted chats
#  It increases page load time



# Why does the script require manual QR code scanning instead of automating login?
#  Selenium does not support camera access
#  WhatsApp Web blocks JavaScript execution
#  Authentication is tied to a real user session for security   (Right Answer)
#  ChromeDriver cannot load HTTPS websites



# What would most likely happen if the delay between messages (time.sleep(1)) were removed?
#  Messages would not be sent at all
#  The browser would crash immediately
#  Selenium would raise a syntax error
#  The script could trigger UI failures or platform restrictions   (Right Answer)



# Which Selenium feature is primarily responsible for simulating a real user pressing Enter?
#  Keys.RETURN   (Right Answer)
#  By.CLASS_NAME
#  driver.get()
#  WebDriverWait



# Why is automation of messaging platforms considered ethically sensitive?
#  It consumes more internet bandwidth
#  It can lead to misuse such as spamming or harassment    (Right Answer)
#  It requires paid browser drivers
#  It increases system memory usage



# Which design choice makes this script platform-dependent?
#  Use of Python language
#  Reliance on internet connectivity
#  Dependence on WhatsApp Web’s DOM structure   (Right Answer) Since xpath and element are fetched based on classname
#  Use of loops for repetition



# Why is driver.quit() preferred over simply closing the browser window manually?
#  It saves execution time
#  It sends logout signals to WhatsApp
#  It keeps the session active for reuse
#  It properly terminates the WebDriver and releases system resources    (Right Answer)