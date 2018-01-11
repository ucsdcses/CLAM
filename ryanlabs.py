import pexpect
import tempfile
from multiprocessing import Pool

#exact seat layout
seat_numbers = [
		[42, 41, 40, 39, 38, 37],
		[31, 32, 33, 34, 35, 36],
		[30, 29, 28, 27, 26, 25],
		[19, 20, 21, 22, 23, 24],
		[18, 17, 16, 15, 14, 13],
		[7, 8, 9, 10, 11, 12],
		[6, 5, 4, 3, 2, 1]
		]

def ssh(host, cmd, user, password, timeout=3):
	"""SSH'es to a host using the supplied credentials and executes a command.
	Throws an exception if the command doesn't return 0"""

	fname = tempfile.mktemp()
	fout = open(fname, 'w')

	#options to prevent ssh from asking for authenticity
	options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'

	ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)
	#ssh_cmd = 'ssh %s@%s %s' % (user, host, options)
	child = pexpect.spawn(ssh_cmd, timeout=timeout)

	#accept any response, send password, record response
	child.expect('[\s\S]*') 
	child.sendline(password) 
	child.logfile = fout 
	child.expect(pexpect.EOF)
	child.close() 
	fout.close() 

	#extract ssh response
	fin = open(fname, 'r')
	stdout = fin.read()
	fin.close()

	if 0 != child.exitstatus:
		raise Exception(stdout)

	#response processing and analysis
	res = stdout.strip()
	#TODO: fix processing of res, currently does not match response of ssh
	#needs to align with printLab if printLab is to be used
	if res == '(unknown)':
		return "free"
	else:
		print host + ": " + res
		return "taken by " + res.split(' ')[0]

def test(i):
	"""tests 1 specific computer for usage, returns string describing availability"""

	#generate lab string
	i = ("0" + str(i)) if (i < 10) else str(i)
	#TODO: lab hardcoded here, should be changed to input parameter
	comp = "its-cseb240-" + i + ".ucsd.edu"

	try:
		return ssh(comp, "users", "ryh002", "L5xmj1!R")

	#error cases, basically just checks for time out
	except Exception as e:
		if type(e) == pexpect.EOF:
			return "EOF file"
		if type(e) == pexpect.TIMEOUT: 
			return "timed out"

		#catchall
		return type(e)



def printLab(lab):
	"""prints a character representation of a lab.
	0 -> free
	T -> timed out
	X -> taken"""

	labstr = ""

	#uses seat layout to print the lab
	for row in seat_numbers:
		for seat in row:
			stat = lab[seat-1]
			if stat == "free":
				labstr += "O"
			elif stat == "timed out":
				labstr += "T"
			else:
				labstr += "X"

		labstr += "\n"

	print labstr



if __name__ == '__main__':
	#use pool of processes to handle each availability check
	p = Pool(processes=42)
	#creates array of size 42 where each array location corresponds to a computer
	res = p.map(test, range(1, 43))
	printLab(res)
	p.terminate()





