import logging, os, sys
path = os.path.abspath(os.path.split(sys.argv[0])[0])

logging.basicConfig(
    format = u'%(levelname)-8s [%(asctime)s] %(message)s',
    level = logging.ERROR,
    filename = '%s/log/log.log' % (path)
)

class Log():
    def error(self, data):
        logging.error(data)

    def info(self, data):
        logging.info(data)
