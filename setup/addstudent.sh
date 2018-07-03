#!/bin/bash

# -------------------------------------------------------------------

# File: addstudent.sh
# Author: Harrison Inocencio
# Date: 07-02-2018
# Purpose: Creates a new student user on the local machine and unpacks 
#		   the workshop materials to their home directory

# Usage: Called via the setup.sh script. Only called after it is copied over
#		 to it's target machine.

# Notes:
# 1. Contains the workshop materials path.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. Make setup_complete record script progress, maybe to read from later 
# 2.
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

set -e

user="$1"
pass="$2"
host="$3"

workshop_materials_path="/usr/local/share/workshop-materials.tar.gz"

# Cancel setup if user already exists
egrep "^$user" /etc/passwd > /dev/null && exit 1

# Create User
useradd -s /bin/bash -m "$user"

# Set Password
#--- --- ---
# Bash Specific Method
#chpasswd <<<"$user:$pass"

# SH Method (For multi lines)
chpasswd <<EOF
${user}:$pass
EOF
#--- --- ---

# Unpack Workshop Materials
#sudo -u "$user" sh -c "cd /home/$user"; tar -xzf "$workshop_materials_path"
#runuser -l "$user" -c "sh -c "cd /home/${user}; tar -xzf $workshop_materials_path""
cd /home/"$user"
tar -xzf "$workshop_materials_path"
chown -R "${user}:$user" *

# Touch completion file
touch "/home/ubuntu/setup_complete"
