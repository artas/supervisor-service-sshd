
import os
from .logger import logging_info


class Service(object):

    def __init__(self):
        self.status_service = os.system('systemctl status sshd')




    def get_status(self):
        logging_info('get status service')
        if self.status_service == 0:
            logging_info('service sshd is started')
        else:
            logging_info('service sshd is stoped')
        return self.status_service

    def service_start(self):
        if self.status_service != 0:
            logging_info('service sshd started')
            os.system('systemctl start sshd')
            self.status_service = os.system('systemctl status sshd')
            return 0
        else:
            return 1
    def service_stop(self):
        if self.status_service == 0:
            logging_info('service sshd stoped')
            os.system('systemctl stop sshd')
            self.status_service = os.system('systemctl status sshd')
            return 0
        else:
            return 1
    def service_restart(self):
        if self.status_service == 0:
            logging_info('service sshd restarted')
            os.system('systemctl restart sshd')
            self.status_service = os.system('systemctl status sshd')
            return 0
        else:
            return 1