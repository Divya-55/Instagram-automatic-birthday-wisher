# Instagram Automatic Birthday Wisher

Automatically send personalized birthday messages to your Instagram contacts based on data from an Excel sheet. This project uses Cohere to generate AI-powered birthday messages and Instabot to automate sending messages on Instagram.

## Description

The **Instagram Automatic Birthday Wisher** automates sending personalized birthday messages to your Instagram contacts. It reads a list of birthdays from an Excel file, generates custom birthday wishes using Cohere's AI, and sends the message via Instagram using Instabot. This project ensures that you never miss wishing a friend or family member on their special day, even when you're busy.

## Features

- Reads birthday data from an Excel file (`birthdays.xlsx`).
- Automatically logs into Instagram using Instabot.
- Uses Cohere's AI to generate custom birthday messages.
- Sends messages directly to the user's Instagram inbox.
- Updates the Excel sheet after sending the message to avoid duplicate wishes in the same year.

## Prerequisites

- Python 3.x
- [Cohere API Key](https://cohere.ai)
- Instagram account credentials
- Instabot for Instagram automation

## Installation

1. **Install dependencies**: Create a virtual environment and install the required packages using `pip`:

    ```bash
    pip install instabot pandas openpyxl python-dotenv cohere
    ```

2. **Configure environment variables**: Create a `.env` file in the root directory with the following variables:

    ```plaintext
    api_key=YOUR_COHERE_API_KEY
    USERNAME=YOUR_INSTAGRAM_USERNAME
    PASSWORD=YOUR_INSTAGRAM_PASSWORD
    ```

3. **Prepare your Excel sheet**: Ensure your `birthdays.xlsx` file has the following columns:
   - **NAME**: The name of the person.
   - **RELATION**: Your relationship to the person (e.g., friend, cousin).
   - **USERNAME**: The Instagram username of the person.
   - **BIRTH DATE**: The date of birth in `dd-mm-yyyy` format.
   - **YEAR**: Tracks the years when birthday messages were sent.

## Usage

1. Ensure that the `birthdays.xlsx` file is populated with the necessary data.
2. Run the `main.py` script:

    ```bash
    python main.py
    ```

3. The script will check for today's birthdays, generate a custom birthday message using Cohere's AI, and send it via Instagram. It will also update the Excel sheet to log the year when the message was sent.

## Acknowledgements

- **Cohere**: For generating AI-powered birthday messages.
- **Instabot**: For automating Instagram interactions.
- **Pandas**: For handling Excel files.
- **Dotenv**: For managing environment variables.
