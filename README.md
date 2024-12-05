# Automatic Birthday Wisher

This is a simple Python script that automatically sends birthday wishes via email to people listed in a CSV file. The script checks if today is anyone’s birthday, picks a random birthday message, and sends it to their email.

## Features

- Checks for birthdays in a `birthdays.csv` file.
- Sends birthday emails using your Gmail account.
- Picks a random birthday message from the `letter_templates` folder.

## Requirements

You’ll need Python 3.x and these libraries:

- `smtplib`
- `pandas`
- `random`
- `os`
- `dotenv`
- `datetime`

### Setup

### 1. Clone the Repository

First, clone this repo to your computer:

```bash
git clone https://github.com/yourusername/automatic-birthday-wisher.git
cd automatic-birthday-wisher
```

### 2. Add Your Birthday Data

Create a `birthdays.csv` file (or use the one provided). It should look like this:

```csv
name,email,month,day
John Doe,johndoe@example.com,12,15
Jane Smith,janesmith@example.com,12,15
```

### 3. Add Your Gmail Credentials

Create a `.env` file in the project directory with your Gmail login details:

```plaintext
GMAIL_USER=your-email@gmail.com
GMAIL_PASSWORD=your-email-password
```

### 4. Add Birthday Message Templates

Put your birthday message templates in the `letter_templates` folder. Use `[NAME]` as a placeholder for the recipient's name.

### 5. Run the Script

To run the script and send birthday wishes, just use:

```bash
python main.py
```
