import subprocess
import os

def run_push():
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "🚀 Push: Full cleanup and staging restructure"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n✅ Successfully pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")

if __name__ == "__main__":
    run_push()