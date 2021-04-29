# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
#!venv/bin/python
import pexpect
import sys
import time

#   set up the connection
child = pexpect.spawn('telnet 10.20.172.64')
child.logfile = sys.stdout.buffer
print(child.before)
# Login
child.expect('User Name : ')
child.send('apc'+'\r')

child.expect('Password  : ')
child.send('apc'+'\r')

#child.expect('communication established')
child.expect('apc>')

