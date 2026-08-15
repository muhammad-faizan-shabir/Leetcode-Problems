#!/usr/bin/env python3
"""
Create a folder with a .txt file and a code file inside it.

Usage:
    python new_solution.py <name> <extension>

Example:
    python new_solution.py two-sum py
    -> creates: two-sum/two-sum.txt
               two-sum/two-sum.py
"""

import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print("Usage: python new_solution.py <name> <extension>")
        print("Example: python new_solution.py two-sum py")
        sys.exit(1)

    name = sys.argv[1]
    extension = sys.argv[2].lstrip(".")  # allow "py" or ".py"

    folder = Path(name)

    if folder.exists():
        print(f"Error: folder '{folder}' already exists.")
        sys.exit(1)

    folder.mkdir(parents=True)

    txt_file = folder / f"{name}.txt"
    code_file = folder / f"{name}.{extension}"

    txt_file.touch()
    code_file.touch()

    print(f"Created folder: {folder}/")
    print(f"  - {txt_file}")
    print(f"  - {code_file}")


if __name__ == "__main__":
    main()