import os
from pathlib import Path

def create_uploads_directory():
    """Ensure the uploads directory exists on the desktop."""
    try:
        desktop = Path.home() / 'Desktop'
        uploads_dir = desktop / 'uploads'
        if not uploads_dir.exists():
            uploads_dir.mkdir(parents=True)
            print(f"Created uploads directory on desktop: {uploads_dir}")
        else:
            print(f"Uploads directory already exists on desktop: {uploads_dir}")
    except Exception as e:
        print(f"Failed to create uploads directory: {e}")

if __name__ == "__main__":
    create_uploads_directory()
