from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode

browser = Firefox(options=opts)
browser.get('https://www.yahoo.com')  # Going to yahoo.com

# Searching for the tag with signin link
signin_button = browser.find_element_by_id('header-signin-link')
signin_link = signin_button.get_attribute('href')  # Getting the signin link
browser.get(signin_link)  # Sendign a get request to the signin link

username = 'laraib_sidd'  # yahoo username
password = 'yahoo_password'  # yahoo password

# Finding the field where username is supposed to be entered.
username_field = browser.find_element_by_id('login-username')
username_field.send_keys(username)  # Sending the user defined username

# Clicking on the next button
browser.find_element_by_id('login-signin').click()

# Finding the field where password is supposed to be entered.
password_field = browser.find_element_by_id('login-passwd')
password_field.send_keys(password)  # Sending the defined password.

# Clicking on the submit button
browser.find_element_by_id('login-signin').click()

browser.close()  # Closing the browser window.
quit()  # Quitting the program.
