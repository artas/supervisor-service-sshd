import os

from .logger import logging_info

dir = './tmp'
filename = '/status_service.txt'


def get_status_chekbox():
    if not os.path.exists(dir):
        os.mkdir(dir)
    if not os.path.isfile(dir + filename):
        file = open(dir + filename, 'tw')
        file.write('False')
        file.close()
        logging_info('service supervisor is stoped')
        return False
    else:
        file = open(dir + filename)
        chek_stat = file.read()
        if chek_stat == 'True':
            logging_info('service supervisor is started')
        else:
            logging_info('service supervisor is stoped')
        return chek_stat


def save_status(status):
    file = open(dir + filename, 'w')
    file.write(str(status))
    file.close()
    if status:
        logging_info('service supervisor started')
    else:
        logging_info('service supervisor stoped')
