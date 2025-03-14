import os
import hashlib

def menu():
    """Displays a menu for user interaction."""
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            directory = input("Enter the directory path: ")
            if os.path.isdir(directory):
                find_duplicates(directory)
            else:
                print("Invalid directory. Please try again.")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def find_duplicates(directory):
    """Recursively searches for duplicate files based on content (SHA-256)."""
    file_hashes = {}  # Dictionary to store hash values and file paths

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_checksum(file_path)

            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_path)
            else:
                file_hashes[file_hash] = [file_path]

    # Print duplicate files
    print("\n--- Duplicate Files Found ---")
    duplicates_found = False
    for paths in file_hashes.values():
        if len(paths) > 1:  # If more than one file has the same hash, it's a duplicate
            duplicates_found = True
            print("\nDuplicate files:")
            for path in paths:
                print(f"  - {path}")

    if not duplicates_found:
        print("No duplicate files found.")

def get_checksum(file_path):
    """Computes SHA-256 checksum of a file."""
    hash_obj = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Read in chunks to handle large files
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

if __name__ == "__main__":
    menu()
