#!/usr/bin/env python3
"""
HiveChain Codebase HTML Generator (Hybrid Version)

This script scans the project directory, collects all relevant code files,
and generates a structured HTML file (`docs/codebase.html`) with proper formatting
for display on GitHub Pages. It ensures clear separation between files,
syntax highlighting via Prism.js, and easy navigation.
"""

from pathlib import Path
from html import escape
from datetime import datetime

# ----------------------------
# STEP 2: DEFINE DIRECTORIES & SETTINGS
# ----------------------------
PROJECT_ROOT = Path("c:/projects/hivechain")
DOCS_DIR = Path("c:/projects/hivechain/docs")
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = DOCS_DIR / "codebase.html"

EXCLUDED_DIRS = {"__pycache__", "tests", "migrations"}
EXCLUDED_FILES = {".env"}  # Additional exclusions if needed
VALID_EXTENSIONS = {".py", ".json", ".md", ".yaml", ".html", ".css"}

EXT_TO_PRISM = {
    ".py": "language-python",
    ".json": "language-json",
    ".md": "language-markdown",
    ".yaml": "language-yaml",
    ".html": "language-html",
    ".css": "language-css",
}

# ----------------------------
# STEP 3: RECURSIVELY COLLECT RELEVANT FILES
# ----------------------------
def collect_files(root_dir: Path):
    """Recursively collect valid files while ignoring excluded directories, files, and output file."""
    hidden_dirs = {".git", ".vscode", ".idea"}  # Common hidden directories to exclude
    return [
        f for f in sorted(root_dir.rglob("*"), key=lambda p: p.as_posix())
        if f.is_file()
        and f.suffix.lower() in VALID_EXTENSIONS
        and f.name not in EXCLUDED_FILES | {OUTPUT_FILE.name}  # Exclude the generated output file
        and not any(ex_dir in f.parts for ex_dir in EXCLUDED_DIRS | hidden_dirs)
    ]
    """Recursively collect valid files while ignoring excluded directories and files."""
    hidden_dirs = {".git", ".vscode", ".idea"}  # Common hidden directories to exclude
    return [
        f for f in sorted(root_dir.rglob("*"), key=lambda p: p.as_posix())
        if f.is_file()
        and f.suffix.lower() in VALID_EXTENSIONS
        and f.name not in EXCLUDED_FILES
        and not any(ex_dir in f.parts for ex_dir in EXCLUDED_DIRS | hidden_dirs)
    ]
    """Recursively collect valid files while ignoring excluded directories and files."""
    return [
        f for f in root_dir.rglob("*")
        if f.is_file()
        and f.suffix.lower() in VALID_EXTENSIONS
        and f.name not in EXCLUDED_FILES
        and not any(ex_dir in f.parts for ex_dir in EXCLUDED_DIRS)
    ]

# ----------------------------
# STEP 4: PROCESS FILE CONTENTS
# ----------------------------
def process_files(file_list):
    """Read and process each file to store its escaped content and syntax class."""
    file_data = []
    for fpath in file_list:
        try:
            content = fpath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"Warning: Unable to read {fpath} due to encoding issues.")
            continue
        except Exception as e:
            print(f"Warning: Unable to read {fpath}: {e}")
            continue
        
        file_data.append({
            "name": fpath.relative_to(PROJECT_ROOT).as_posix(),
            "syntax_class": EXT_TO_PRISM.get(fpath.suffix.lower(), "language-none"),
            "content": escape(content),
        })
    return file_data
    """Read and escape file contents, map syntax highlighting classes."""
    file_data = []
    for fpath in file_list:
        try:
            content = fpath.read_text(encoding="utf-8")
        except Exception:
            continue  # Skip unreadable files
        file_data.append({
            "name": fpath.relative_to(PROJECT_ROOT).as_posix(),
            "syntax_class": EXT_TO_PRISM.get(fpath.suffix.lower(), "language-none"),
            "content": escape(content),
        })
    return file_data

# ----------------------------
# STEP 5: GENERATE HTML FILE
# ----------------------------
def generate_html(file_data):
    """Generate structured HTML with TOC, syntax highlighting, and navigation."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>HiveChain Codebase</title>",
        "  <link href='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css' rel='stylesheet' />",
        "  <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js'></script>",
        "</head>",
        "<body>",
        "  <a id='top'></a>",
        "  <h1>HiveChain Codebase</h1>",
        f"  <p>Last updated: {timestamp}</p>",
        "  <h2>Table of Contents</h2>",
        "  <ul>",
    ]
    
    for i, fdata in enumerate(file_data):
        file_id = f"file-{i}"
        html_parts.append(f"    <li><a href='#{file_id}'>{fdata['name']}</a></li>")
    html_parts.append("  </ul>")

    for i, fdata in enumerate(file_data):
        file_id = f"file-{i}"
        html_parts.append("  <hr>")
        html_parts.append(f"  <h2 id='{file_id}'>{fdata['name']}</h2>")
        html_parts.append(f"  <pre><code class='{fdata['syntax_class']}'>{fdata['content']}</code></pre>")
        html_parts.append("  <p><a href='#top'>Back to Top</a></p>")
    
    html_parts.append("</body>")
    html_parts.append("</html>")
    return "\n".join(html_parts)

# ----------------------------
# STEP 6: WRITE OUTPUT FILE
# ----------------------------
def write_output(html_result):
    """Write the generated HTML to docs/codebase.html."""
    OUTPUT_FILE.write_text(html_result, encoding="utf-8")

# ----------------------------
# STEP 7: PRINT SUCCESS MESSAGE
# ----------------------------
def main():
    print("Collecting files...")
    files = collect_files(PROJECT_ROOT)
    print("Processing files...")
    processed_data = process_files(files)
    print("Generating HTML content...")
    html_result = generate_html(processed_data)
    print("Writing to output file...")
    write_output(html_result)
    print(f"Success! Codebase HTML generated at: {OUTPUT_FILE}")
    print("Preview of generated HTML:")
    print("-" * 50)
    print(html_result[:500])  # Print first 500 characters for preview
    print("-" * 50)

if __name__ == "__main__":
    main()
