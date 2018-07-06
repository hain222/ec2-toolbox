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
# 1. Make pem path into an optional variable
# 2. Complete help vars
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

import gconsts
import argparse

# Required Environment Variables
cwd_env = 'cwd'  # name of ev containing cwd

# Head messages
multi_spin_head = 'Multi-Instance Spin Started...'
sing_spin_head = 'Single-Instance Spin Started...'

# Error messages
path_error = 'ERROR: Config not found'
create_error = 'ERROR: Create encountered an error'
length_error = 'ERROR: Non-matching number of names and users'

# Output
def_out_prefix = 'create_run'
def_out_suffix = '.log'
time_fmt = "%Y-%m-%d_%H:%M:%S"
output_header = "# SPIN LOG\n# <time> name-tag:id:host:user:password\n"

# Parser HELPS
user_help = 'user HELP'
nametag_help = 'nametag HELP'
output_help = 'output HELP'
asfile_help = 'asfile HELP'

# parse function
# handles user parameters and returns arg dict
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('user', help=user_help)
	parser.add_argument('-n', '--name', help=nametag_help)
	parser.add_argument('-o', '--output', help=output_help)
	parser.add_argument('-f', '--asfile', action='store_true', help=asfile_help)
	args = parser.parse_args()

	return args
