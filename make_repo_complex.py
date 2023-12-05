import os
import random
import string
import subprocess

def random_string(length=80):
    """Generate a random string of fixed length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def pregenerate_lines(num_lines=1000):
    """Pre-generate a list of random lines."""
    return [random_string() for _ in range(num_lines)]

def modify_and_rename_file(file_path, pregenerated_lines, is_large_file=False):
    """Modify the file based on its size and rename it, skipping certain paths."""
    if '.git' in file_path or 'make_repo_complex' in file_path:
        return

    new_file_path = file_path.rsplit('.', 1)[0] + '.scn.yaml'

    lines_to_insert = 1000 if is_large_file else 10000  # 10 MB of text, assuming ~10 chars per line
    lines = []

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

    for _ in range(lines_to_insert):
        random_line = random.choice(pregenerated_lines)
        insert_position = random.randint(0, len(lines)) if lines else 0
        lines.insert(insert_position, random_line + '\n')

    if is_large_file and len(lines) > 1000:
        for _ in range(1000):
            if lines:
                lines.pop(random.randint(0, len(lines) - 1))

    with open(new_file_path, 'w') as file:
        file.writelines(lines)

    os.remove(file_path)
    print(f"Modified {new_file_path}")

def create_new_files(repo_path, pregenerated_lines, num_files=10):
    """Create new files with random content."""
    for i in range(num_files):
        file_path = os.path.join(repo_path, f'new_file_{i}.txt')
        modify_and_rename_file(file_path, pregenerated_lines)

def git_commit_and_push(repo_path, iteration, push_interval=100):
    """Perform git add, commit, and push at specified intervals."""
    subprocess.run(["git", "add", "-A"], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", f"Commit {iteration}"], cwd=repo_path)

    if iteration % push_interval == 0:
        subprocess.run(["git", "push"], cwd=repo_path)

def process_repository(repo_path, iterations=100):
    pregenerated_lines = pregenerate_lines()
    all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(repo_path) for f in filenames if os.path.isfile(os.path.join(dp, f))]

    for iteration in range(iterations):
        print(f"Iteration {iteration + 1}/{iterations}")
        selected_files = random.sample(all_files, min(100, len(all_files)))

        for file in selected_files:
            file_size = os.path.getsize(file)
            try:
                modify_and_rename_file(file, pregenerated_lines, is_large_file=(file_size > 40 * 1024 * 1024))
            except:
                continue

        create_new_files(repo_path, pregenerated_lines)
        git_commit_and_push(repo_path, iteration + 1)

# Set your repository path here
repo_path = '.'
process_repository(repo_path)

