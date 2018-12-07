#!/usr/bin/env python3
import logging
import logging.handlers

#
# Setup logging to local syslog
#
# erik@juju-dev:~/allcode/snap-pyapp$ tail -n 2 /var/log/syslog   
# Dec  6 19:18:10 juju-dev app.hello: this is debug
# Dec  6 19:18:10 juju-dev app.hello: this is critical

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


def syslogging():
	log.debug('this is a debug syslog message')
	log.critical('this is a critical syslog message')

if __name__ == '__main__':
	syslogging()
        print("Hello there. I syslogged.")

