import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WIDGET_PATTERN = re.compile(r'st\.checkbox\(["\']Show Debug Info["\']\)')

def scan_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        try:
            code = f.read()
        except Exception as e:
            return (path, f"❌ Error reading file: {e}")
        
        if WIDGET_PATTERN.search(code):
            return (path, "❌ Found: duplicate checkbox with no key")
        return (path, "✅ Clean")

def walk_and_check():
    issues = []
    print("\n🔍 Scanning all .py files for unsafe Streamlit widget usage...\n")
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".py"):
                result = scan_file(Path(root) / file)
                issues.append(result)
                print(f"{result[1]} → {result[0].relative_to(ROOT)}")

    flagged = [r for r in issues if "❌" in r[1]]
    if not flagged:
        print("\n✅✅✅ All clear! No duplicate checkbox IDs found.")
    else:
        print(f"\n🚨 {len(flagged)} issues found. Please fix all duplicate checkbox widgets.")

if __name__ == "__main__":
    walk_and_check()