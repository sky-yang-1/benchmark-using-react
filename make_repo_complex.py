import os
import random
import string
import subprocess
def random_string(length=800):
    """Generate a random string of fixed length."""
    
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)) 

def random_name(length=800):
    """Generate a random string of fixed length."""
    
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)) 
def pregenerate_lines(num_lines=1000):
    """Pre-generate a list of random lines."""
    return [random_string() + '\n' for _ in range(num_lines)]

def modify_and_rename_file(file_path, pregenerated_lines, is_large_file=False, is_new_file=False):
    """Modify the file based on its size and rename it, skipping certain paths."""
    if '.git' in file_path or 'make_repo_complex' in file_path:
        return

    if '.scn.yaml' in file_path:
        new_file_path = file_path
    else:
        new_file_path = file_path.rsplit('.', 1)[0] + '.scn.yaml'

    lines_to_insert = 1000 if is_large_file else 1000  # 10 MB of text, assuming ~10 chars per line
    lines = []

    if not is_new_file and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

    for i in range(lines_to_insert):
        random_line = pregenerated_lines[i%1000]
        lines.append(random_line)

    if is_large_file and len(lines) > 1000:
        for _ in range(1000):
            if lines:
                lines.pop(random.randint(0, len(lines) - 1))

    with open(new_file_path, 'w') as file:
        if is_new_file:
            print(f'Creating {new_file_path}')
        file.writelines(lines)

    if not is_new_file:
        os.remove(file_path)

    print(f"Modified {new_file_path}")

def create_random_filename(prefix='', suffix='.scn.yaml', length=10):
    """Create a random filename."""

    return prefix + random_string(length) + suffix

def choose_new_folder(cwd):
    all_files = os.listdir(cwd) 
    if len(all_files) < 1000 and cwd != '.':
        return cwd
    new_folder = random.random() > 0.5 

    directories = [d for d in os.listdir(cwd) ]

    if (new_folder or len(directories) == 0) and cwd != '.' :
        folder_name = 'dir_' + random_string(10)
        folder_path = os.path.join(cwd,folder_name)
        os.mkdir(folder_path)
        return folder_path
    else:
        random_directory = random.choice(directories)
        return choose_new_folder(os.path.join(cwd, random_directory))

    

def create_new_files(repo_path, pregenerated_lines, num_files=10):
    """Create new files with random content."""
    new_folder = choose_new_folder(repo_path)
    print(f"chosen {new_folder} to put in the new file")

    for _ in range(num_files):
        file_name = create_random_filename(suffix='.scn.yaml')
        file_path = os.path.join(new_folder, file_name)
        modify_and_rename_file(file_path, pregenerated_lines, is_new_file=True)

def git_commit_and_push(repo_path, iteration, push_interval=100):
    """Perform git add, commit, and push at specified intervals."""
    subprocess.run(["git", "add", "-A"], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", f"Commit {iteration}"], cwd=repo_path)

    if iteration % push_interval == 0:
        subprocess.run(["git", "push"], cwd=repo_path)

def process_repository(repo_path, iterations=10000):
    pregenerated_lines = pregenerate_lines()
    all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(repo_path) for f in filenames if os.path.isfile(os.path.join(dp, f))]

    for iteration in range(iterations):
        print(f"Iteration {iteration + 1}/{iterations}")
        selected_files = random.sample(all_files, min(100, len(all_files)))

        for file in selected_files:
            try:

                file_size = os.path.getsize(file)
                modify_and_rename_file(file, pregenerated_lines, is_large_file=(file_size > 40 * 1024 * 1024))
            except:
                continue

        create_new_files(repo_path, pregenerated_lines)
        git_commit_and_push(repo_path, iteration + 1)

# Set your repository path here
repo_path = '.'
process_repository(repo_path)

