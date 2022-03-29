#!/usr/bin/python
import cfworker
import time, os

worker = cfworker.cfworker(port=8080)
worker.start()

while True:
	print 'Python on TAP...'
	time.sleep(2)

worker.stop()

