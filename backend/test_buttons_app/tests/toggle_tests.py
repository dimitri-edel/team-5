import os

def rename_test_files():
    # Get the current working directory
    base_dir = os.getcwd()

    # Walk through all subdirectories
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            # If the filename begins with 'test_', insert '_' at the beginning of the filename
            if file.startswith('test_'):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, f'_{file}')
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')
            # Else if the filename begins with '_test_', remove '_' from the beginning of the filename
            elif file.startswith('_test_'):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file[1:])
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')

if __name__ == "__main__":
    rename_test_files()
