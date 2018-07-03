# File: instWrapper.py
# Author: Harrison Inocencio
# Date: 06-21-18
# Purpose: Contains the instWrapper class, which is a wrapper for the aws
#		   instance class

# Notes:
# 1. 
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. Put attributes into dict?
# 2. Create cache function that stores important attributes
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

import io
import gconsts
import boto3
import subprocess

# instWrapper class
# See 'Purpose'
class instWrapper:
	# Initialize ec2 resource
	rsc = boto3.resource('ec2')
	
	#__get_name func
	# grab the instance nametag, return None if not found
	def __get_name(self, inst):
		for tag in inst.tags:
			if tag['Key'] == gconsts.name_key:
				return tag['Value']

		return None

	# __init__ func
	# Creates instance obj, and caches important information
	def __init__(self, inst_id):
		# Create AWS instance obj
		self.inst_obj = self.rsc.Instance(inst_id)
		# Cache important attributes
		self.inst_name = self.__get_name(self.inst_obj)
		self.inst_id = self.inst_obj.instance_id
		self.pub_ip = self.inst_obj.public_ip_address
		self.state = self.inst_obj.state['Name']

	# terminate func
	# Causes the wrapper to terminate the instance it is wrapping
	# Does not check the previous state
	def terminate(self):
		self.inst_obj.terminate()

	# start func
	# Causes the wrapper to start the instance it is wrapping
	# Does not check the previous state
	def start(self):
		self.inst_obj.start()

	# stop func
	# Causes the wrapper to stop the instance it is wrapping
	# Does not check the previous state
	def stop(self):
		self.inst_obj.stop()

	# reboot func
	# Causes the wrapper to reboot the instance it is wrapping
	# Does not check the previous state
	def reboot(self):
		self.inst_obj.reboot()

	# tprint func
	# Prints all cached attributes, mostly for testing
	def tprint(self):
		print(self.inst_name)
		print(self.inst_id)
		print(self.pub_ip)
		print(self.state)

	# ws_user_setup func
	# initiates the workshop user setup process,
	# 1. Creates user on the instance
	# 2. Unpacks workshop materials to their home directory
	# Will return a list containing the username, host, and password
	# respectively
	def ws_user_setup(self, user):
		ret = subprocess.run(['./'+gconsts.setup_path, user, self.pub_ip, gconsts.pem_path], stdout=subprocess.PIPE, universal_newlines=True)
		if ret.returncode != 0:
			raise(RuntimeError(gconsts.subprocess_error))

		sret = ret.stdout.split('\n')
		while '' in sret:
			sret.remove('')

		return sret
