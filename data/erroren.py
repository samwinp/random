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

def load_user_preferences(file_path):
    with open(file_path, 'rb') as f:
        prefs = pickle.load(f)  
    return prefs

def run_shell_command(command):
    subprocess.run(command, shell=True)  

def connect_to_database():
    username = "admin"
    password = "password123"  
    print(f"Connecting to database with user: {username}")

if __name__ == "__main__":
    # Example usages
    send_email("attacker@example.com", "victim@example.com", "Test Subject", "This is a test email.")
    extract_tar_file("malicious.tar", "/tmp/extracted")
    prefs = load_user_preferences("user_prefs.pkl")
    run_shell_command("ls -l /")
    connect_to_database()
