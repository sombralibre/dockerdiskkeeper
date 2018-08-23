import os
import sys

from time import sleep
from helpers import housekeeping


# http or unix
# default: http
scheme = os.environ.get('SCHEME', 'http')


# maximum percentage of used disk
# default: 80%
diskthreshold = os.environ.get('DISKLIMIT', 80)


# run interval
# default: every 5 hours
interval = os.environ.get('INTERVAL', 18000)


def main(argv):
    while True:
        housekeeping(scheme, diskthreshold)
        sleep(int(interval))


if __name__ == "__main__":
    main(sys.argv)
