# Tinder Dislike Bot

This project uses Selenium to automate the login and interaction with Tinder's web interface. The bot logs into Tinder, performs authentication through phone number and email, and simulates user actions on the platform. 

## Features

- **Login with Phone Number**: Automates the login process using a phone number.
- **Phone and Email Verification**: Handles the input of verification codes received via SMS and email.
- **Dislike Automation**: Once logged in, the bot can be extended to perform actions like disliking users or other interactions on Tinder.

## Requirements

- Python 3.6 or higher
- Chrome and ChromeDriver (ensure ChromeDriver matches your Chrome version)
- The following Python libraries:
  - `selenium`

You can install the necessary libraries using pip:

```bash
pip install selenium
```

## Setup

1. **Install Chrome and ChromeDriver**:
   - Download and install [Google Chrome](https://www.google.com/chrome/).
   - Download the matching version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for your Chrome version and add it to your system's PATH.

2. **Edit the Script**:
   - Replace the empty string for `number_input.send_keys("")` with your phone number.
   - When prompted, provide the SMS and email verification codes to complete the login process.

3. **Run the Script**:
   - After setup, run the script:

   ```bash
   python main.py
   ```

   The bot will:
   1. Open Tinder's website.
   2. Click the login button and initiate login via phone number.
   3. Wait for you to input the verification codes sent via SMS and email.
   4. Once logged in, it will be ready to interact with Tinder.

## How It Works

1. **Login**: The bot first accesses Tinder's login page, clicks the login button, and selects the login method via phone number.
2. **Phone Number Authentication**: After entering your phone number, it waits for the verification code. You need to manually input the code sent via SMS into the script.
3. **Email Authentication**: Once phone verification is complete, the bot will guide you to enter the verification code sent to your email.
4. **Interaction**: After successfully logging in, the bot is ready to interact with the platform (this part can be extended to include automating likes, dislikes, or other actions).

## Example

```bash
python main.py
```

### Sample Output

```text
Please type the code that they sent you: [Your SMS Code]
Please type the code: [Your Email Code]
```

## Notes

- The bot requires manual interaction for entering verification codes during the login process.
- **Caution**: Automating interactions on Tinder may violate their terms of service, so proceed with caution and be aware of the risks involved in using bots on platforms.

## License

This project does not have a license.

## Contributing

Feel free to fork this repository, submit issues, or contribute pull requests for improvements or bug fixes.
