# Google Drive Backup Tool

In a world where people are constantly engrossed in the pursuit of financial gains and various activities, the importance of backing up files often takes a backseat. Despite Google offering free data storage, many users overlook this opportunity due to the perceived manual effort involved. This application addresses that gap by leveraging the power of Python, automation, and Google's free storage space to create a tool that simplifies the backup process.

## How It Works

The application utilizes your Google account for verification and grants access to store information on Google Drive seamlessly.

## Getting Started

### Installation

- For Windows users: Download the .exe file and double-click to install.
- For Linux users: Clone the repository and run the main.py file using the command `python main.py`.

### Usage

1. Install the application following the appropriate steps above.
2. Create a new folder that you want the application to monitor.
3. Click on "Run" or "Start" to initiate the application.
4. Once the application is running, any new file, document, or folder added to the monitored directory will be automatically uploaded to your Google Drive.
5. Log in to your Google account using any browser of your choice to access your backed-up files.

## Installation Guide

1. Clone the application using Git.
2. Follow the link [here](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf) to obtain authentication for the Google Drive API service.
3. Click on 'Download JSON' on the right side of the Client ID to download `client_secret_<really long ID>.json`.
4. Rename the downloaded file to "client_secrets.json" and place it in your working directory.
5. Run the program using the command `python main.py`.

Now you can enjoy the benefits of automated Google Drive backups without the hassle of manual intervention.
