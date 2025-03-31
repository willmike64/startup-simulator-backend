#Push to GitHub
# This script initializes a Git repository, creates placeholder files to track empty directories,
# and pushes the entire directory structure to a remote GitHub repository.
# It also handles the case where the remote repository is not already set.
# Make sure to run this script from the root of your project directory.
# Usage: ./push_to_github.sh

#!/bin/bash

# Exit if anything fails
set -e

# Make sure Git is initialized
git init

# Create placeholder files to ensure directories are tracked
touch views/.keep
touch components/.keep
touch utils/.keep
mkdir -p data/logs
touch data/logs/.keep

# Add everything
git add .

# Commit
git commit -m "🚀 Auto-push full directory structure with .keep files"

# Set remote if not already set
git remote remove origin 2> /dev/null || true
git remote add origin https://github.com/willmike64/startup-sim-alpha.git

# Push to main
git branch -M main
git push -u origin main