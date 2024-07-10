# Bulk Email Sender with CC, BCC and Email Validation

This Python script allows you to send bulk emails to a list of HR contacts, including yourself as a BCC recipient. It also includes basic email validation using the `validate_email` library.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed
- The required Python libraries: `pandas`, `smtplib`, `email`, and `validate_email`
- A Gmail account with "Less secure app access" enabled or an app-specific password generated

## Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/bulkemailsender.git
   cd bulk-email-sender


### Additional Notes:
- **CSV File Structure:** Ensure your `hr_contacts.csv` file has at least the columns `email` and `first_name`.

