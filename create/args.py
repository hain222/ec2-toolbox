# File: args.py
# Author: Harrison Inocencio
# Date: 06-25-18
# Purpose: Contains the argument parsing and constants for create.py

# Notes:
# 1. Sample synopsis
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

import argparse

# Error messages
path_error = 'ERROR: Config not found'
create_error = 'ERROR: Create encountered an error'

# parse function
# handles user parameters and returns arg dict
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('nametag', help='nametag HELP')
	parser.add_argument('username', help='username HELP')
	args = parser.parse_args()

	return args
