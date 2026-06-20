#!/usr/bin/env python3
"""
Replace all occurrences of "AloneX" with "Amit"
"""

import os

def replace_in_file(file_path, old_str, new_str):
    """Replace old_str with new_str in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str not in content:
            return False
        
        content = content.replace(old_str, new_str)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_directory(directory):
    """Process all files in directory"""
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Skip hidden files and binary files
            if file.startswith('.'):
                continue
            
            file_path = os.path.join(root, file)
            
            # Check if file is text file (skip binary)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    f.read(1024)
            except:
                continue
            
            # Replace in file
            if replace_in_file(file_path, "AloneX", "Amit"):
                count += 1
    return count

if __name__ == "__main__":
    print("Starting replacement...")
    main_dir = os.path.dirname(os.path.abspath(__file__))
    amit_dir = os.path.join(main_dir, "Amit")
    
    count = process_directory(amit_dir)
    print(f"\nReplaced in {count} files!")
    
    # Also update test_xbit_integration.py
    test_file = os.path.join(main_dir, "test_xbit_integration.py")
    if os.path.exists(test_file):
        replace_in_file(test_file, "AloneX", "Amit")
