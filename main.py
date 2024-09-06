import cohere
from instabot import Bot
import time
from datetime import datetime
import pandas
import os
import shutil  # Import shutil to remove directories
from dotenv import load_dotenv, find_dotenv

os.chdir(r"D:\Divya_coding\PROGRAMS\6.PYTHON\2.PYTHON PROJECTS\RESUME PROJECTS\instagram automatic birthday wisher")

# Path to the directory to delete
directory_path = "config"

# if the directory exists delete
if os.path.isdir(directory_path):
    shutil.rmtree(directory_path)

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

co = cohere.Client(
    api_key=os.getenv('api_key')
)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

bot = Bot()
time.sleep(60)

now = datetime.now()
now_year = now.year
now_date_month = now.strftime("%d-%m")


def get_birthday_message(user_message):
    response = co.generate(
        model='command-r-plus',
        prompt=f'Create an instagram message : \"{user_message}\":',
        max_tokens=300,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text


# excel
dataframe = pandas.read_excel("birthdays.xlsx")
list_of_index = []

for index, item in dataframe.iterrows():
    birth_date = item["BIRTH DATE"].strftime("%d-%m")
    if birth_date == now_date_month:
        # send msg to the one whose birthday is today
        if (birth_date == now_date_month) and str(now_year) not in str(item["YEAR"]):
            # login to the instagram account automatically
            bot.login(username=USERNAME, password=PASSWORD)
            time.sleep(60)
            relation = item["RELATION"]
            name = item["NAME"]
            insta_username = item["USERNAME"]
            msg = get_birthday_message(f"Hi, iam divya write a birthday wishes for my {relation} {name}, add 'many more happy returns of the day' at the end")
            bot.send_message(msg, insta_username)
            time.sleep(60)
            list_of_index.append(index)
            time.sleep(60)
            bot.logout(username=USERNAME)
            time.sleep(60)

if list_of_index:
    for e in list_of_index:
        dataframe.loc[e, "YEAR"] = f"{str(dataframe.loc[e, 'YEAR'])}, {str(now_year)}"
    dataframe.to_excel('birthdays.xlsx', index=False)



