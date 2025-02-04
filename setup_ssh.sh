#!/bin/bash

# Start the SSH agent
eval "$(ssh-agent -s)"

# Write the SSH key to a temporary file
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAACIIKMd8vJrRSgvWgszZpn3loz7wD7FGCnoav7mYczaucW vm.slic3r@pm.me" > ~/.ssh/temp_key

# Set the correct permissions for the key
chmod 600 ~/.ssh/temp_key

# Add the key to the SSH agent
ssh-add ~/.ssh/temp_key

# Test the connection to GitHub
ssh -T git@github.com

# Optional: Clean up the temporary key file (comment out if you want to keep it)
rm ~/.ssh/temp_key