# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
#!venv/bin/python
import pexpect
import sys
import time

#   set up the connection
child = pexpect.spawn('telnet 0.0.0.0')
child.logfile = sys.stdout.buffer
print(child.before)
# Login
child.expect('User Name : ')
child.send('apc'+'\r')

child.expect('Password  : ')
child.send('apc'+'\r')

#child.expect('communication established')
child.expect('apc>')

#System status

child.send('olOff 3'+'\r')
print('turn off outlet 3')
time.sleep(30)
child.send('olOn 3'+'\r')
print('turn on outlet 3')

#print(child.before)
