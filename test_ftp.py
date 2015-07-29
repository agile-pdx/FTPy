import pytest
import ftp
import pysftp


USERNAME = "your_username"
PASSWORD = "your_password"
FTP_URL  = "cs.pdx.edu"

def test_list_dir_returns_value():
    sftp = pysftp.Connection(FTP_URL, username=USERNAME, password=PASSWORD)
    output = ftp.list_dir(sftp)
    
    #Output should not be empty
    assert output != None
    
    
def test_get_file_with_invalid_file():
    sftp = pysftp.Connection(FTP_URL, username=USERNAME, password=PASSWORD)
    output = ftp.get_file(sftp, "Non-existent.file")
    
    #Output should not be False
    assert not output
    
    
def test_get_file_with_valid_file():
    sftp = pysftp.Connection(FTP_URL, username=USERNAME, password=PASSWORD)
    output = ftp.get_file(sftp, ".bashrc")
    
    #Output should not be True
    assert output
