from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time
from datetime import datetime


def day_converter():
    now = datetime.now()
    day = now.day

    if day >= 17:
        return website(day)
    else:
        day = 25
        return website(day)


def website(day):
    """
    uses selenium to open the webpage
    """
    driver = webdriver.Chrome('./chromedriver')  # initializes the browser that is being used
    driver.get('https://ucsc.crimegraphics.com/2013/default.aspx')  # goes to this specific url
    time.sleep(6)
    daily_crime = driver.find_element(By.XPATH, '//*[@id="CLERYMenu"]')
    close = driver.find_element(By.XPATH, '//*[@id="cmdCloseMessage"]')
    close.click()
    daily_crime.click()
    time.sleep(2)
    cases = driver.find_elements(By.CLASS_NAME, 'ob_gCc2')
    digit_pattern = re.compile("^[0-9]+")
    letter_pattern = re.compile("^[A-Z]")
    letter_pattern2 = re.compile("[a-zA-z]") # searches if the string has a letter
    noChar_pattern = re.compile("^$")
    filter = ['Report', 'Suspended', 'Assisted', 'Pending', 'Information',
                     'Log', 'Cleared', 'Arrival', 'Advised', 'Arrest']  # unnecessary information
    data = []
    # now = datetime.now()
    # current_month = now.month
    # day = now.day-7
    # with open('crime_data', 'a') as f:
    for case in range(len(cases)):
        if case == 0:  # first element will be appended to data
            data.append(cases[case].text)
            # f.write(cases[case].text + '\n')
        if noChar_pattern.search(cases[case].text):
            continue
        if any(word in cases[case].text for word in filter):  # filters out the word, if word is found in filter for loop continues
            continue
        if digit_pattern.search(cases[case - 1].text):  # skips the occured time since some cases do not have an occured time
            if letter_pattern.search(cases[case].text):
                data.append(cases[case].text)
                # f.write(cases[case].text + '\n')
            else:
                continue
        else:
            if case == 0:
                continue
            else:
                if digit_pattern.search(cases[case].text):
                    if '/' not in (cases[case].text[2:4]):  # if reported day is more than a week old function breaks
                        if int(cases[case].text[2:4]) > day:
                            break
                        else:
                            data.append(cases[case].text)
                            # f.write(cases[case].text  + '\n')
                    else:
                        data.append(cases[case].text)
                else:
                    data.append(cases[case].text)
                    # f.write(cases[case].text  + '\n')
    data.pop()      
    driver.quit()
    return data


# def table(data):
#     df = pd.DataFrame(columns=['Crime', 'Report Time', 'Location'])
#     for i in data:
#         new_row = [data[0],data[1],data[2]]
#         df.loc[len(df)] = new_row
#         data.pop(0)
#         data.pop(0)
#         data.pop(0)
#     return file(df.iloc[0])


def comparison(data):
    x = data[0]
    y = data[1]
    z = data[2]
    with open('log.txt', 'r') as f:
        for r in f:
            if r == x:
                continue
            elif r == y:
                continue
            elif r == z:
                continue
            else:
                with open('log.txt', 'w') as t:
                    t.write(x + '\n')
                    t.write(y + '\n')
                    t.write(z + '\n')


day = day_converter()
comparison(day)
# table(day)





# if __name__ == '__main__':
#     while True:
#         try:
#             website()
#             table(data)
#         except Exception as e:
#             print("Error occurred:", e)
#         time.sleep(300)            
