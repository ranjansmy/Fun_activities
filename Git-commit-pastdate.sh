#!/bin/bash

# Set the date you want to commit the repos on
commit_date="2022-07-15"

# Set the directory where your Git repos are located
repo_dir="/path/to/repos"

# Change to the repo directory
cd $repo_dir

# Loop through all subdirectories in the repo directory
for dir in $(find . -type d -maxdepth 1); do
    # Check if the current directory is a Git repository
    if [ -d "$dir/.git" ]; then
        # Change to the current repo's directory
        cd $dir
        # Set the date of the last commit to the specified date
        git commit --amend --no-edit --date="$commit_date"
        # Change back to the repo directory
        cd $repo_dir
    fi
done

echo "All repos in $repo_dir have been committed on $commit_date"
