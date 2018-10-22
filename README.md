# EC2-Toolbox

The ec2-toolbox is a collection of command line based tools for creating and managing AWS EC2 instances for the University of Kentucky Next Generation Sequencing Workshop run by Dr. Farman of the UKY Department of Plant Pathology and Dr. Jaromczyk of the UKY Department of Computer Science. Written using the Boto3 software development kit.

Note that this software was both developed, and run on Ubuntu 16.04 & 18.04 and has not been tested on other distributions or operating systems.

## Getting Started

Instructions for installing the awscli software, the boto3 library, and configuring these scripts to work with your ec2 setup.

### Required Prerequisites

* Python3
* awscli
* boto3

Most Ubuntu systems will already have python3 installed, but just in case yours does not, you can install it through the Ubuntu package manager.

```
sudo apt-get install python3
```

Installing awscli is available through the Ubuntu package manager, and can be installed by running the following command.
```
sudo apt-get install awscli
```
Once awscli is successfully installed on your system, you will have to go through the necessary steps to configure it with your aws account. This process is well documented in Amazon's awscli user guide, and a link to instructions on how to configure your awscli software can be found [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

Once you have successfully completed the configuration, (to the point where you have successfully run and filled in all the information required by the "aws configure" command) you are ready to install the boto3 library.

Installing the boto3 library is best done through the python3 package manager, pip3. As in previous examples, you can install pip3 through the Ubuntu package manager.

```
sudo apt-get install python3-pip
```

Once pip3 is installed, you can install boto3 through pip3.

```
sudo -H pip3 install boto3
```

### Installing

To install this software, first clone the GitHub repository if you have not already done so. 

The easiest way to do this is through the git command line interface. You can install git using the Ubuntu package manager, if you have not already done so.

```
sudo apt-get install git
```

Next clone the repository to your current directory using

```
git clone https://github.com/hain222/ec2-toolbox.git
```

The "ec2-toolbox" repository contains a "bin" directory that can be added to your PATH variable, and this is recommended for easy access to the entire tool set. 

You can do this for your current login session by typing
```
export $PATH=PATH:/path/to/repo/ec2-toolbox/bin
```
or permanently by adding that same line to the end of your ~/.bashrc file

Next, a configuration file must be created that can provide ec2-specific information. This can be easily done using the "configure" tool by running,

```
configure
```

and entering the required AMI, instance type, key pair file name (without the .pem), and security group identifier. Any of these values can be  changed later by simply running the command again, typing in new values for what needs to be changed, and pressing enter for values that should remain the same.

From here the installation is complete. Address the usage section for detailed instructions on how to use the individual programs.

**IMPORTANT NOTE!**
The creation script for this tool set is specifically designed to create NGS Workshop instances for student use. As a result, if you do not provide it with one of our official NGS Workshop image AMIs', the create tool WILL NOT WORK AS INTENDED. 

A complete list of our current public workshop AMIs and the region they are available in are located in the resources section.

## Usage

The ec2-toolbox currently consists of the "create", "describe", "configure", and "basic" programs.

#### Create

Used to setup Workshop instances by performing three separate operations
1. Spins up the instance from the official NGS Workshop AMI that you specified
2. Creates a student account on the instance with a randomized password
3. Unpacks the workshop materials into the students home directory

Produces an output file containing import ec2 specific information about each spun instance, as well as the username and password of the student account that was created on that instance.

**SYNOPSIS**
```
create [-h] [-n NAME] [-o OUTPUT] [-f] <USER>
```
**POSITIONAL ARGUMENTS**
```
USER - user name of the student account to be created
```
**OPTIONAL ARGUMENTS**
```
-h, --help - display a help message
-n NAME, --name NAME - optional name tag to attach to the spun instance (if not specified will use the provided username as the name tag)
-o OUTPUT, --output OUTPUT - provide an output file name (if not specified will use a default output name based on system time)
-f, --asfile - if this option is toggled, it will treat the <USER> argument as a file containing a list of newline separated usernames rather than a single username, and will spin an instance for each username located in the file. (Use this if you want to spin up more than one instance)
```

#### Describe

Used to display various information on owned VM's such as it's name tag, public IP, instance id, and instance state.

**SYNOPSIS**
```
describe [-h] [-s STATE] [-a] [-c]
```
**OPTIONAL ARGUMENTS**
```
-h, --help - display a help message
-s STATE, --state STATE - filters output based off of the VM state. Valid states are {pending, running, shutting-down, terminated, stopping, stopped}. (If not specified, will show all 'running' instances by default)
-a, --all - If toggled, will output all owned VM's regardless of their instance state.
-c, --csv - If toggled, will output VM information in a parseable csv format.
```

#### Basic

Encompasses several basic operations common to VM management, including starting, stopping, terminating, and rebooting a VM or VM's.

**SYNOPSIS**
```
basic [-h] [-i] <OPERATION> <INSTANCE ...>
```
**POSITIONAL ARGUMENTS**
```
OPERATION - the name of the desired operation. Available operations are {start, stop, terminate, reboot}.
INSTANCE - Instance name tag, or list of instance name tags to perform the operation on.
```
**OPTIONAL ARGUMENTS**
```
-h, --help - display a help message.
-i, --id - If this option is toggled, the given instances will be treated as instance ids instead of name tags.
```

#### Configure

Simple script for creating or modifying the configuration file. Contains no positional or optional arguments. 

**SYNOPSIS**
```
configure
```

If running this program for the first time it will require you to fill in all fields to create the configuration file. Otherwise, you can modify the attributes that need modification and can press enter to skip past the ones that can remain the same. 

## Resources
References containing supplementary links and important information.

#### Workshop VM Availability
Region "us-east-1" has public AMI "AMI-5a113025"

Region "us-east-2" has public AMI "TBA"

Region "sa-east-1" has public AMI "AMI-015ee737b0f04fcc4"

#### Workshop Links

The "Essentials of Next Generation Sequencing Workshop" home page can be found [here](https://ngs.csr.uky.edu/).

## Authors

* **Harrison Inocencio** - Undergraduate Research Department of Computer Science

## License

TBA

## Acknowledgments

* Dr. Farman Department of Plant Pathology University of Kentucky
* Dr. Jaromczyk Department of Computer Science University of Kentucky
* Dr. Moore Department of Computer Science University of Kentucky

