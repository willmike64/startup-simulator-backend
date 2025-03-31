import os
import shutil
from pathlib import Path
import subprocess

# Set this to the root of your real project
TARGET_PROJECT_ROOT = Path(__file__).resolve().parent

# Path to the unpacked patch directory (to walk through)
SOURCE_PATCH_DIR = TARGET_PROJECT_ROOT / "patch_drop"

# Map simple filename patterns to destination subfolders
DEST_MAP = {
    "views": ["ceo_", "funding_", "onboarding", "staffing", "founder"],
    "components": ["banner", "ticker"],
    "utils": ["session", "logger", "ai"],
    "advisors": ["ai_"]
}

def determine_destination(file_path: Path):
    name = file_path.name.lower()
    for folder, keywords in DEST_MAP.items():
        if any(kw in name for kw in keywords):
            return TARGET_PROJECT_ROOT / folder / file_path.name
    # Fallback for unmatched files
    return TARGET_PROJECT_ROOT / file_path.name

def walk_and_integrate():
    if not SOURCE_PATCH_DIR.exists():
        print(f"❌ Patch folder not found at: {SOURCE_PATCH_DIR}")
        return

    integrated_files = []

    for root, dirs, files in os.walk(SOURCE_PATCH_DIR):
        for file in files:
            if file.startswith(".") or file.endswith((".log", ".zip", ".DS_Store")):
                continue

            source_file = Path(root) / file
            target_file = determine_destination(source_file)

            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, target_file)
            integrated_files.append(str(target_file.relative_to(TARGET_PROJECT_ROOT)))
            print(f"✅ Integrated: {file} → {target_file}")

    if integrated_files:
        print("\n🔧 Staging changes for Git...")
        subprocess.run(["git", "add"] + integrated_files)

        # Optional auto-commit
        commit_msg = "🤖 Auto-integrated patch files"
        subprocess.run(["git", "commit", "-m", commit_msg])
        print("✅ Changes committed.")

        # Uncomment to auto-push (optional)
        # subprocess.run(["git", "push", "origin", "main"])
    else:
        print("⚠️ No valid files integrated.")

if __name__ == "__main__":
    walk_and_integrate()