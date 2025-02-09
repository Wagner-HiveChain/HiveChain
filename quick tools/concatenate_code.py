import os

def get_all_files(root_dir, extensions=('.py', '.json')):
    """
    Recursively collects all files ending with the specified extensions from the root_dir,
    excluding hidden directories.
    
    Args:
        root_dir (str): The root directory to search.
        extensions (tuple): File extensions to include.
        
    Returns:
        list: A list of full file paths.
    """
    all_files = []
    for subdir, dirs, files in os.walk(root_dir):
        # Exclude hidden directories (those that start with a dot)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith(extensions):
                all_files.append(os.path.join(subdir, file))
    return all_files

def main():
    # Set the project root to the directory containing this script
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Define the output file in the docs directory (create docs if needed)
    output_dir = os.path.join(project_root, "docs")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "combined_code.txt")
    
    # Get all .py and .json files from the project root recursively.
    files = get_all_files(project_root, ('.py', '.json'))
    
    combined_text = ""
    for file_path in files:
        rel_path = os.path.relpath(file_path, project_root)
        combined_text += f"\n\n# File: {rel_path}\n\n"
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                combined_text += f.read()
        except Exception as e:
            combined_text += f"\n# Error reading file: {e}\n"
    
    # Write the combined text to the output file.
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write(combined_text)
    
    print(f"Combined code has been written to:\n{output_file}")

if __name__ == "__main__":
    main()
