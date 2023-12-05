import os
import random
import string

def random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def modify_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified = False

    # 20% chance to remove a random line from the file
    if random.random() < 0.20 and lines:
        del lines[random.randint(0, len(lines) - 1)]
        modified = True

    # 20% chance to edit a random line in the file
    if random.random() < 0.20 and lines:
        random_line_index = random.randint(0, len(lines) - 1)
        lines[random_line_index] = lines[random_line_index].strip() + " " + random_string() + "\n"
        modified = True

    # 20% chance to add a new line to the file
    if random.random() < 0.20:
        lines.append(random_string() + "\n")
        modified = True

    if modified:
        print(f"modifying {file_path}")
        with open(file_path, 'w') as file:
            file.writelines(lines)

def process_directory(root_dir):
    for root, dirs, files in os.walk(root_dir): 
        for file in files:
            file_path = os.path.join(root, file)
            if '.git' in file_path:
                continue
            if '.py' in file_path:
                continue
            try:
                modify_file(file_path)
            except:
                continue

# Replace 'path_to_your_directory' with the path of your directory
root_directory = '.'
process_directory(root_directory)

