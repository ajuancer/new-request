# This code was written by Juan (https://github.com/ajuancer).
# It's part of the tell me activity status (https://github.com/ajuancer/tell-me-activity-status/).
# The last edit was commited on 8 December, 2019.
# This code is, like the rest of the project, is under the license CC BY-NC 4.0.

# The packages:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# The bot checks for a change in the activity each 5 minutes by default. Change the value of the
# following variable if you preffer another value. Remmeber to write it in seconds.
refreshTime = 300;

# The variable for the login is:
usernameStr = 'YOUR MAIL';

# Send message to me function.
def telegram_bot_sendtext(bot_message):
    bot_token = 'TOKEN'
    bot_chatID = 'ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message;
    response = requests.get(send_text)
    return response.json()

# Open Chrome at the link.
browser = webdriver.Chrome();
browser.get(('https://accounts.google.com/signin/v2/identifier?service=ah&passive=false&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fcodein.withgoogle.com%2Fdashboard%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

# Fill in username and hit the next button
username = browser.find_element_by_id('identifierId');
username.send_keys(usernameStr);
nextButton = browser.find_element_by_id('identifierNext');
nextButton.click();

# Check activity status
WebDriverWait(browser, 20).until(EC.url_to_be("https://codein.withgoogle.com/dashboard/"));
divStatus = browser.find_element_by_xpath("//div[@class='current-task__status']");
strongStatus = divStatus.find_element_by_xpath(".//strong");
currentStatus = strongStatus.text;
print("The current status is " + currentStatus);
test = telegram_bot_sendtext("The current status of your activity is " + currentStatus);

while currentStatus == "Submitted for review":
    time.sleep(refreshTime);
    browser.refresh()
    print("The current status is " + currentStatus);
else:
    test = telegram_bot_sendtext("Your task is marked as done or the mentor has requested more work.");
