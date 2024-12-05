import random
import smtplib
import pandas
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()


# Email credentials
my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

# Fetching birthday months and days
data = pandas.read_csv("birthdays.csv")
month_list = data["month"].to_list()
day_list = data["day"].to_list()

# Fetching today's date and month
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Using pandas dataframe filtering to select specific rows based on a condition (data.day == day)
# Filter the dataframe to get the row(s) where the "day" matches today's date
chosen_row = data[data.day == today_day]
print(chosen_row)

directory = "./letter_templates"

# os.listdir will create a list of every file or folder present in a letter_template directory
letter_list = os.listdir(directory)
template_file = random.choice(letter_list)

with open(f"./letter_templates/{template_file}", "r") as temp:
    content = temp.read()
    for index, row in chosen_row.iterrows():
        letter = content.replace("[NAME]", str(row["name"]))

if today_month in month_list and today_day in day_list:
    with smtplib.SMTP("smtp.gmail.com") as con:
        con.starttls()
        con.login(user=my_email, password=password)

        con.sendmail(from_addr=my_email, to_addrs=chosen_row["email"],
                     msg=f"Subject: HAPPY BIRTHDAY!\n\n {letter}")
