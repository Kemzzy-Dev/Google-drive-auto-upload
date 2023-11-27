import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate the google user
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
http = drive.auth.Get_Http_Object()

def upload_directory(directory_path):
    """
    Uploads the contents of a directory to Google Drive.
    Args:
        directory_path (str): The path to the directory to be uploaded.
    Returns:
        None
    Raises:
        None
    """
    # Use the authenticated google user to upload file
    folder_name = os.path.basename(directory_path)

    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload(param={"http": http})

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_metadata = {'title': file, 'parents': [{'id': folder['id']}]}

            drive_file = drive.CreateFile(file_metadata)
            drive_file.SetContentFile(file_path)
            drive_file.Upload(param={"http": http})

    print('Folder Uploaded Successfully....')

def upload_file(file_path):
    """
    Uploads a file to Google Drive.
    Parameters:
        file_path (str): The path to the file to be uploaded.
    Returns:
        None
    """
    file_name = os.path.basename(file_path) # Get the name of the file

    file_metadata = {'title': file_name} # Set the name of the file to be saved in the metadata
 
    drive_file = drive.CreateFile(file_metadata)
    drive_file.SetContentFile(file_path)
    drive_file.Upload(param={"http": http})

    print('File Uploaded Successfully....')



class LoggingEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        """
        Handle the event when a new file or directory is created.
        Args:
            event (FileSystemEvent): The event object representing the created file or directory.
        Returns:
            None
        """
        if event.is_directory:
            abs_path = os.path.abspath(event.src_path)
            upload_directory(abs_path)
        else:
            abs_path = os.path.abspath(event.src_path)
            upload_file(abs_path)

        # print(f"New {file_type} added: {event.src_path}")

if __name__ == "__main__":

    path = '../backup'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
