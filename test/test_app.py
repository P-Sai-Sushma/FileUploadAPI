import pytest
from flask import Flask
from pathlib import Path
import os
import tempfile

from fileuploadapi.app import app, UPLOADS_DIR  # Adjust this import according to your module structure

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        # Create necessary directories for the test
        if not UPLOADS_DIR.exists():
            UPLOADS_DIR.mkdir(parents=True)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index(client):
    """Test the index page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Welcome' in rv.data

def test_upload_page(client):
    """Test the upload page."""
    rv = client.get('/upload')
    assert rv.status_code == 200
    assert b'Upload' in rv.data

def test_upload_file_success(client):
    """Test uploading a file successfully."""
    data = {
        'file': (tempfile.NamedTemporaryFile(delete=False, suffix='.txt'), 'test.txt')
    }
    rv = client.post('/uploadFile', data=data, content_type='multipart/form-data')
    assert rv.status_code == 200
    assert b'File uploaded successfully' in rv.data
    # Check if file is saved in the uploads directory
    assert (UPLOADS_DIR / 'test.txt').exists()
    # Clean up
    os.remove(UPLOADS_DIR / 'test.txt')

def test_upload_file_no_file(client):
    """Test uploading without selecting a file."""
    rv = client.post('/uploadFile', data={}, content_type='multipart/form-data')
    assert rv.status_code == 400
    assert b'Please select a file' in rv.data

def test_upload_file_empty_filename(client):
    """Test uploading a file with an empty filename."""
    data = {
        'file': (tempfile.NamedTemporaryFile(delete=False, suffix=''), '')
    }
    rv = client.post('/uploadFile', data=data, content_type='multipart/form-data')
    assert rv.status_code == 400
    assert b'File not selected' in rv.data

def test_upload_file_too_large(client):
    """Test uploading a file that is too large."""
    # Create a temporary large file
    large_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    large_file.write(b'a' * (1048577))  # Write 1MB + 1 byte
    large_file.seek(0)

    data = {
        'file': (large_file, 'largefile.txt')
    }
    rv = client.post('/uploadFile', data=data, content_type='multipart/form-data')
    large_file.close()
    os.remove(large_file.name)  # Clean up the file
    assert rv.status_code == 400
    assert b'File size is too big. Upload file smaller in size' in rv.data

def test_internal_server_error(client, mocker):
    """Test internal server error during file upload."""
    data = {
        'file': (tempfile.NamedTemporaryFile(delete=False, suffix='.txt'), 'test.txt')
    }
    mocker.patch('fileuploadapi.app.create_uploads_directory', side_effect=Exception('Test exception'))
    rv = client.post('/uploadFile', data=data, content_type='multipart/form-data')
    assert rv.status_code == 500
    assert b'Internal Server Error' in rv.data
