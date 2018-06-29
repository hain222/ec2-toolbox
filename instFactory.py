# File: instFactory.py
# Author: Harrison Inocencio
# Date: 06-19-18
# Purpose: Provides functions for generating WSInst objects from boto3
#		   struct's depending on certain attributes

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. Make this class capable of spinning up its own instances
# 2. 
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

import gconsts
import boto3
from instWrapper import instWrapper

# instFactory class
# Generates lists of instWrapper objects based on certain attributes
class instFactory:
	# Initialize ec2 client
	client = boto3.client('ec2')	

	# __wsinsts_from_response func
	# Builds instWrapper objects from the describe response struct
	def __wsinsts_from_response(self, response):
		inst_list = []
		for reservation in response['Reservations']:
			for inst in reservation['Instances']:
				ws_inst = instWrapper(inst['InstanceId'])
				inst_list.append(ws_inst)

		return inst_list

	# get_all func
	# Get all instances
	# returns list of instWrappers
	def get_all(self):
		response = self.client.describe_instances()
		insts = self.__wsinsts_from_response(response)

		return insts

	# get_by_state func
	# Get all instances according to a provided state
	# returns list of instWrappers
	def get_by_state(self, state):
		response = self.client.describe_instances(
			Filters = [
				{
					'Name' : 'instance-state-name',
					'Values' : [ state ]
				}
			]
		)
		insts = self.__wsinsts_from_response(response)

		return insts

	# get_by_id func
	# Get instances according to a provided list of instance ids
	# returns list of instWrappers (Provided list of ids MUST be a list!)
	def get_by_id(self, id_list):
		response = self.client.describe_instances(
			InstanceIds=id_list
		)
		insts = self.__wsinsts_from_response(response)

		return insts

	# get_by_nametag function
	# Get all instances according to provided instance name(s)
	# provided names MUST be in a list, returns list of instWrappers
	def get_by_nametag(self, name_list):
		response = self.client.describe_instances(
			Filters = [
				{
					'Name': 'tag:' + gconsts.name_key,
					'Values' : name_list
				}
			]
		)
		insts = self.__wsinsts_from_response(response)

		return insts

	# create_instance func
	# Create an instance assigned the specified name, and the specified
	# config object
	def create_instance(self, nametag, config):
		
		return 0
