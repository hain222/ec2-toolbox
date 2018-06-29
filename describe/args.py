# File: args.py
# Author: Harrison Inocencio
# Date: 06-19-18

# Purpose: Contains the arg parsing and constants for the describe.py script

# ------------------------------------------------------------------------

import gconsts
import argparse

# Default parameters
default_state = 'running'

# Argparse constants
state_help = 'Display VMs based on their instance state attribute, default=running'
all_help = 'Display all VMs'
csv_help = 'Output VM info as a parseable csv format'

# Formatting
table_header = ['INSTANCE_NAME', 'PUBLIC_IP', 'INSTANCE_ID', 'INSTANCE_STATE']
adjust = [20,18,22,15]

# parse function
# > handles user parameters and returns arg dict
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--state', default=default_state, choices=gconsts.state_choices, help=state_help)
	parser.add_argument('-a', '--all', action='store_true', help=all_help)
	parser.add_argument('-c', '--csv', action='store_true', help=csv_help)
	args = parser.parse_args()

	return args
