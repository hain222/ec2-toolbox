# File: describe.py
# Author: Harrison Inocencio
# Date: 06-19-18
# Purpose: 'describe' tool for aws vms. Depending on the provided parameters
#		   it will produce formatted output listing important information
#		   about the VM's

# Usage: Use the shell script 'describe' located in 'bin' to call this
#		 script

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. +++Should draw its main functions from a library/class
# 2. Replace 'Nones' with '-'
# 3. +++csv option for output
# 4. consider implementing using the boto3 'instances' class rather than
#	 'describe_instances'
# 5. Eventually want to fix hard coding in the tab_print section
# 6. Add try except loop (KeyboardInterrupts etc...)
# 7. Shift hard coded messages to args

# -------------------------------------------------------------------

import gconsts
import describe.args as args
from instFactory import instFactory

# get_row func
# Generates an output row from the given inst
def get_row(inst):
	inst_name = inst.inst_name
	pub_ip = inst.pub_ip
	inst_id = inst.inst_id
	state = inst.state

	if inst_name == None:
		inst_name = '-'
	if pub_ip == None:
		pub_ip = '-'

	return [inst_name, pub_ip, inst_id, state]

# tab_print func
# Prints given instances list in a formatted table
def tab_print(insts):

	headers = args.table_header
	for idx in range(len(headers)):
		print(headers[idx].rjust(args.adjust[idx]), end=' ')
	print()
	for inst in insts:
		row = get_row(inst)
		for idx in range(len(row)):
			print(row[idx].rjust(args.adjust[idx]), end=' ')
		print()
		
# csv_print func
# Prints given instances list in csv format
def csv_print(insts):
	for inst in insts:
		row = get_row(inst)
		for idx in range(len(row)-1):
			print('%s,' % (row[idx]), end='')
		print(row[len(row)-1])

# main func
# Parses args, retrieves instances
def main():
	
	arg_dict = args.parse()
	state = arg_dict.state
	
	factory = instFactory()
	
	if arg_dict.all:
		insts = factory.get_all()
	else:
		insts = factory.get_by_state(state)

	if len(insts) == 0:
		print('No matching instances found...')
		exit(1)

	if arg_dict.csv:
		csv_print(insts)
	else:
		tab_print(insts)

main()
