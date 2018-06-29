# File: args.py
# Author: Harrison Inocencio
# Date: 06-19-18
# Purpose: Contains the argument parsing and constants for basic.py

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

import argparse

# Argparse constants
operation_help = 'The name of the operation needed'
instance_help = 'instance nametag, or list of instance nametags, for the operation to be performed on'
id_help = 'If this option set, the given instances will be treated as instance ids'
op_choices = ['start','stop','terminate','reboot']

# Operation constants
valid_start_states = ['stopped']
valid_stop_states = ['running']
valid_reboot_states = ['running']
valid_terminate_states = ['stopped', 'running']

# parse function
# > handles user parameters and returns arg dict
def parse():
	parser = argparse.ArgumentParser()
	parser.add_argument('operation', help=operation_help, choices=op_choices)
	parser.add_argument('instance', nargs='*', help=instance_help)
	parser.add_argument('-i', '--id',  action='store_true', help=id_help)
	args = parser.parse_args()

	return args
