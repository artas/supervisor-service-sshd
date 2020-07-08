
import logging.handlers

logger = logging.getLogger('supervisor-service')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log', facility="local0")

logger.addHandler(handler)


def logging_info(log):
    logger.info(log)
