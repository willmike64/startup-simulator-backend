import os
import shutil
from pathlib import Path

# Base path where your project is located
PROJECT_ROOT = Path(__file__).resolve().parent
STAGING_DIR = PROJECT_ROOT / "staging"

# Create the staging folder if it doesn't exist
STAGING_DIR.mkdir(exist_ok=True)

# Items to move to staging
items_to_stage = [
    "CEO_Simulation_Bundle",
    "ai_advisor_patch_ceo_cfo.zip",
    "ai_openai_patch.zip",
    "component_debug_patch.zip",
    "final_debug_patch.zip",
    "views_cleaned_ready.zip",
    "startup_simulator_final_live_ready.zip",
    "PushtoGitHub.sh",
    "logs.json",
    "directory.txt"
]

for item in items_to_stage:
    src = PROJECT_ROOT / item
    dst = STAGING_DIR / item
    if src.exists():
        print(f"📦 Moving: {src} → {dst}")
        if src.is_dir():
            shutil.move(str(src), str(dst))
        else:
            shutil.move(str(src), str(dst))
    else:
        print(f"⚠️ Not found: {item}")

print("\n✅ Cleanup complete. Your project is now lean and clean.")