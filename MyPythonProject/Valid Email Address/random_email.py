"""
For making random Emails
"""


import random
import string


def generate_valid_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    domain = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
    extension = random.choice(['com', 'net', 'org', 'edu'])
    return f"{username}@{domain}.{extension}"


def generate_invalid_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15))) + '@invalid.com'


def generate_emails(valid_ratio):
    emails = []
    valid_count = int(valid_ratio * 1000)
    invalid_count = 1000 - valid_count
    for _ in range(valid_count):
        emails.append(generate_valid_email())
    for _ in range(invalid_count):
        emails.append(generate_invalid_email())
    random.shuffle(emails)
    return emails


def write_emails_to_file(emails, filename):
    with open(filename, 'w') as file:
        for email in emails:
            file.write(email + '\n')


if __name__ == "__main__":
    valid_ratio = 0.7  # Adjust this ratio as needed
    emails = generate_emails(valid_ratio)
    write_emails_to_file(emails, 'emails.txt')
