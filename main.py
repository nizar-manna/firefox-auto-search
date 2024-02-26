from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import sys
import time
import os
from keyboard import write as kb_write, send as kb_send


def valid_input(input_var_name):
    user_input = ""
    while user_input == "":
        user_input = input(f"Please input a {input_var_name}: ")
        if user_input == "":
            print("error: no input detected")
        else:
            return user_input


def file_opener(file_name):
    try:
        with open(f'firefox-auto-search/{file_name}.txt', 'r') as file:
            file_content = []
            for line in file:
                if line.strip() and not line.startswith("#"):
                    file_content.append(line.strip())
                    
            if len(file_content) == 1:
                return file_content[0]
            else:
                return file_content
    except FileNotFoundError:
        print(F"{file_name} file hasn't been found.")
        sys.exit(1) # should be replaced

keyword_file = "type_keyword_here"
queries_file = "type_queries_here"

keyword, queries = file_opener(keyword_file), file_opener(queries_file)

# Building last modified profile path
appdata = os.getenv('APPDATA')
profiles_path = os.path.join(appdata, "Mozilla", "Firefox", "Profiles")

profiles = [(name, os.path.getmtime(os.path.join(profiles_path, name))) for name in os.listdir(profiles_path)]

sorted_profiles = sorted(profiles, key=lambda x: x[1], reverse=True)

if sorted_profiles:
    latest_profile = sorted_profiles[0][0]
    profile_path = os.path.join(profiles_path, latest_profile)
    print(profile_path)
else:
    print("error: no Firefox profile found.")

ffOptions = Options()

ffOptions.add_argument("-profile")
ffOptions.add_argument(rf'{profile_path}')

driver = webdriver.Firefox(ffOptions)

for query in queries:
    #time.sleep(2)
    #time.sleep(2)

    driver.get('about:home')
    search_form = driver.find_element(By.CLASS_NAME, 'fake-editable')
    #time.sleep(1)
    search_form.click()
    #time.sleep(0.1)

    #time.sleep(3)
    search_form.clear()
    kb_write("aa")
    [kb_send("backspace") for _ in range(3)]

    kb_write(keyword + " " + query)
    kb_send("enter")
    time.sleep(0.1)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
