#!/bin/bash

# -------------------------------------------------------------------

# File: setup.sh
# Author: Harrison Inocencio
# Date: 07-02-2018
# Purpose: Shell script that initiates a workshop VM user setup process
#		   1. Creates student user on VM
#		   2. Unpacks materials to the student directory

# Usage: Called by the ws_user_setup func in the instWrapper class
#		 CALL SYNOPSIS: ./setup/setup.sh <user> <ip> <pem_path>

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1.
# 2.
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

# Parse parameters
user="$1"
host="$2"
pem_path="$3"
pass=$(pwgen -n 12 1)
addstudent="addstudent.sh"
max_count=6

# Echo parameters to stdout for recording
echo $user
echo $host
echo $pass

(
	# BaseBall Bat Method
	# Keep attempting to open an ssh connection until successful
	# Timeout after set number of loops
	count=0

	until ssh -q -i "$pem_path" -o StrictHostKeyChecking=no -l ubuntu "$host" > "/dev/null"; do
		sleep 5

		if [ "$count" >= "$max_count" ]; then
			exit 1
		fi
	
		((count+=1))

	done

	# Copy over addstudent script
	scp -q -i "$pem_path" -o StrictHostKeyChecking=no "$(dirname $0)/$addstudent" ubuntu@"$host:~" &&\
	ssh -q -i "$pem_path" -o StrictHostKeyChecking=no -l ubuntu "$host" "sudo ./$addstudent '$user' '$pass' '$host'"

) >/dev/null 2>&1 &
