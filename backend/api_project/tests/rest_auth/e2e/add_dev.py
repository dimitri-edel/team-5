import os

def rename_files(directory):
    # Change the current working directory to the specified directory
    os.chdir(directory)
    
    # Rename all files in the current directory, by inserting the string "_dev" to the filenames after the beginning string "test"
    for file in os.listdir():
        if file.startswith("test"):
            new_name = file.replace("test", "test_dev", 1)
            os.rename(file, new_name)

if __name__ == "__main__":
    # Specify the directory containing the files to be renamed
    directory = os.path.dirname(os.path.abspath(__file__))
    rename_files(directory)