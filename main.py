import smtplib
import datetime as dt
import random
import pandas as pd

# Define the file path
csv_file_path = "birthdays.csv"

# Read the CSV file
birthdays = pd.read_csv(csv_file_path)

# Your email credentials
my_email = "mananshah2047@gmail.com"
password = "mfuf otcj iios cwbx"

# Get today's date
now = dt.datetime.now()
today_tuple = (now.month, now.day)

# Check if today matches a birthday in the birthdays.csv
birthday_person = birthdays[(birthdays['month'] == today_tuple[0]) & (birthdays['day'] == today_tuple[1])]

if not birthday_person.empty:
    # Pick a random letter template
    letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    chosen_letter = random.choice(letter_templates)

    with open(chosen_letter) as letter_file:
        letter_content = letter_file.read()

    # Replace the [NAME] placeholder with the actual name and send the email
    for index, person in birthday_person.iterrows():
        personalized_letter = letter_content.replace("[NAME]", person['name'])
        to_email = person['email']

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
            )
        print(f"Sent birthday email to {person['name']} at {to_email}")


# Save the updated data back to the CSV file
birthdays.to_csv(csv_file_path, index=False)
print(f"CSV file updated and saved at {csv_file_path}")

print(f"The email of the last row is: {to_email}")

# Modify the CSV data - Adding a new row

# new_row = pd.DataFrame([{'name': 'Manan Shah', 'email': 'mananshah2047@gmail.com', 'year': 2024, 'month': 7,
# 'day': 31}]) birthdays = pd.concat([birthdays, new_row], ignore_index=True) Update the to_email variable to the
# email of the last row to_email = new_row.iloc[0]['email']

# Remove the last row and save the updated DataFrame back to the CSV file

# birthdays = birthdays[:-1]
# birthdays.to_csv(csv_file_path, index=False)
# print(f"Last row removed and CSV file updated at {csv_file_path}")































