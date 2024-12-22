import os
import subprocess
import pickle

def send_email(sender, recipient, subject, body):
    command = f"sendmail -t {recipient}"
    email_message = f"From: {sender}\nTo: {recipient}\nSubject: {subject}\n\n{body}"
    os.system(command + " << EOF\n" + email_message + "\nEOF")

import tarfile

def extract_tar_file(file_path, extract_to):
    with tarfile.open(file_path) as tar:
        tar.extractall(path=extract_to)  


def connect_to_database():
    username = "admin"
    password = "password123"  
    print(f"Connecting to database with user: {username}")


