#!/usr/bin/python
import cfworker
import time, os

worker = cfworker.cfworker()
worker.start()

while True:
	print 'Python on TAP...'
	time.sleep(2)

worker.stop()

