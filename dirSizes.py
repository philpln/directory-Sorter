import os

def bytes_to_gb(size_in_bytes):
    return size_in_bytes / (1024 ** 3)

def directorySizes():
    # Initialize local variables to avoid global state issues
    files_by_directory = {}
    directory_sizes = {}

    try:
        # Walk through the directory structure
        for dirpath, dirnames, filenames in os.walk("."):
            if filenames:  # Check if there are files to avoid unnecessary processing
                files_by_directory[dirpath] = [os.path.join(dirpath, filename) for filename in filenames]
                if dirpath not in directory_sizes:
                    directory_sizes[dirpath] = 0

        # Calculate sizes for each directory
        for dirpath, filepaths in files_by_directory.items():
            for filepath in filepaths:
                directory_sizes[dirpath] += bytes_to_gb(os.path.getsize(filepath))

        return directory_sizes

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
