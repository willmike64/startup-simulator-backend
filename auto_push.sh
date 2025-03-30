# Automatically commit and push changes to the repository
# This script is intended to be run in a Git repository
# It stages all changes, commits them with a timestamp, and pushes to the main branch
# Make sure to set the correct remote and branch name if different
# Usage: Save this script as `auto_commit.sh` and run it in your Git repository
# Ensure you have the necessary permissions and SSH keys set up for pushing to the repository
# Make sure to give execute permission to the script: chmod +x auto_commit.sh
# You can also set up a cron job to run this script at regular intervals
# Example cron job to run every hour:
# 0 * * * * /path/to/auto_commit.sh > /dev/null 2>&1
# Note: This script does not handle merge conflicts or other Git errors
# Ensure you have the necessary permissions and SSH keys set up for pushing to the repository
# Make sure to give execute permission to the script: chmod +x auto_commit.sh
# You can also set up a cron job to run this script at regular intervals
# Example cron job to run every hour:
# Note: This script does not handle merge conflicts or other Git errors

#!/bin/bash

set -e

git add .
git commit -m "🔄 Auto-update: $(date +'%Y-%m-%d %H:%M:%S')" || echo "Nothing to commit"
git push origin main