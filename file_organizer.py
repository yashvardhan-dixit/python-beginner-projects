import os
import shutil

# 💾 Change this to your Downloads folder path
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# 📁 Folder categories
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh"]
}

def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Ignore if it's a folder
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        # Find matching folder
        moved = False
        for folder, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                dest_folder = os.path.join(DOWNLOADS_FOLDER, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"📁 Moved '{filename}' to {folder}/")
                moved = True
                break

        if not moved:
            print(f"❓ Unrecognized file type: {filename}")

if __name__ == "__main__":
    print("🚀 Organizing your Downloads folder...")
    organize_files()
    print("✅ Done!")
# This script organizes files in the Downloads folder into categorized subfolders based on their file extensions.
# It creates folders for images, documents, videos, music, archives, and scripts, moving files accordingly.
# Unrecognized file types are reported but not moved.
# Make sure to run this script in an environment where you have permission to modify the Downloads folder
# and that you have Python installed.
# You can run this script periodically to keep your Downloads folder organized. 