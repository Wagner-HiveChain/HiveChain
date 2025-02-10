#!/usr/bin/env python3
"""
HiveChain Codebase HTML Generator (Refined Version)

This script scans the project directory, collects all relevant code files,
and generates a structured HTML file (`docs/codebase.html`) with proper formatting
for display on GitHub Pages. It ensures clear separation between files,
syntax highlighting via Prism.js, and easy navigation.
"""

from pathlib import Path
from html import escape
from datetime import datetime

# ------------------------------------------------
# STEP 1: DEFINE DIRECTORIES & SETTINGS
# ------------------------------------------------
PROJECT_ROOT = Path("c:/projects/hivechain")
DOCS_DIR = PROJECT_ROOT / "docs"
DOCS_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = DOCS_DIR / "codebase.html"

# Expanded lists of directories and files to exclude
EXCLUDED_DIRS = {
    "__pycache__", "tests", "migrations", "node_modules",
    ".git", ".vscode", ".idea", "__MACOSX"
}
EXCLUDED_FILES = {
    ".env", ".DS_Store", "Thumbs.db", "codebase.html", "combined_code.log"
}

# Only gather files with these extensions
VALID_EXTENSIONS = {".py", ".json", ".md", ".yaml", ".html", ".css"}

# Mapping file extensions to Prism syntax classes
EXT_TO_PRISM = {
    ".py": "language-python",
    ".json": "language-json",
    ".md": "language-markdown",
    ".yaml": "language-yaml",
    ".html": "language-html",
    ".css": "language-css",
}

# ------------------------------------------------
# STEP 2: COLLECT RELEVANT FILES
# ------------------------------------------------
def collect_files(root_dir: Path):
    """
    Recursively collect valid files while ignoring excluded directories and files.
    Sorted by path for consistent ordering in the output.
    """
    all_files = root_dir.rglob("*")
    
    # Filter out directories and files we don't want
    relevant_files = []
    for f in sorted(all_files, key=lambda p: p.as_posix()):
        # Skip if it's not a file
        if not f.is_file():
            continue
        
        # Skip if file extension is not in VALID_EXTENSIONS
        if f.suffix.lower() not in VALID_EXTENSIONS:
            continue
        
        # Skip if file name is in EXCLUDED_FILES
        if f.name in EXCLUDED_FILES:
            continue
        
        # Skip if any part of the path is in EXCLUDED_DIRS
        if any(ex_dir in f.parts for ex_dir in EXCLUDED_DIRS):
            continue
        
        # Also skip if this is the output file
        if f.name == OUTPUT_FILE.name:
            continue
        
        relevant_files.append(f)
    
    return relevant_files

# ------------------------------------------------
# STEP 3: PROCESS FILE CONTENTS
# ------------------------------------------------
def process_files(file_list):
    """
    Read and process each file to store its escaped content and syntax class.
    """
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

# ------------------------------------------------
# STEP 4: GENERATE HTML OUTPUT
# ------------------------------------------------
def generate_html(file_data):
    """
    Generate structured HTML with a Table of Contents, collapsible sections,
    syntax highlighting, and navigation links.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "  <head>",
        "    <meta charset='UTF-8'>",
        "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
        "    <title>HiveChain Codebase</title>",
        "    <!-- Prism.js theme -->",
        "    <link href='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css' rel='stylesheet' />",
        "  </head>",
        "  <body>",
        "    <a id='top'></a>",
        "    <h1>HiveChain Codebase</h1>",
        f"    <p>Last updated: {timestamp}</p>",
        "    <h2>Table of Contents</h2>",
        "    <ul>",
    ]
    
    # Build the Table of Contents
    for i, fdata in enumerate(file_data):
        file_id = f"file-{i}"
        html_parts.append(f"      <li><a href='#{file_id}'>{fdata['name']}</a></li>")
    html_parts.append("    </ul>")
    
    # Build the collapsible code sections
    for i, fdata in enumerate(file_data):
        file_id = f"file-{i}"
        html_parts.append("    <hr>")
        html_parts.append(f"    <h2 id='{file_id}'>{fdata['name']}</h2>")
        
        # Use a <details> section to make the code collapsible
        html_parts.append("    <details open>")
        html_parts.append("      <summary>Show/Hide Code</summary>")
        html_parts.append("      <br>")
        
        # Syntax-highlighted code block
        html_parts.append(
            f"      <pre><code class='{fdata['syntax_class']}'>{fdata['content']}</code></pre>"
        )
        html_parts.append("    </details>")
        
        # Back to top link
        html_parts.append("    <p><a href='#top'>Back to Top</a></p>")
    
    # Include the Prism.js scripts
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-markdown.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-yaml.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-css.min.js'></script>")
    html_parts.append("    <script src='https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-markup.min.js'></script>")
    
    # Initialize Prism after loading the language components
    html_parts.append("    <script>")
    html_parts.append("      document.addEventListener('DOMContentLoaded', function() {")
    html_parts.append("          Prism.highlightAll();")
    html_parts.append("      });")
    html_parts.append("    </script>")
    
    html_parts.append("  </body>")
    html_parts.append("</html>")
    
    return "\n".join(html_parts)

# ------------------------------------------------
# STEP 5: WRITE TO OUTPUT FILE
# ------------------------------------------------
def write_output(html_result):
    """
    Write the generated HTML to docs/codebase.html.
    """
    OUTPUT_FILE.write_text(html_result, encoding="utf-8")

# ------------------------------------------------
# STEP 6: PRINT SUCCESS MESSAGE
# ------------------------------------------------
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
