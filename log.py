# -*- coding: utf-8 -*-
import logging
#'%a, %d %b %Y %H:%M:%S' #Mon, 15 Oct 2018 16:10:25
#"%Y/%m/%d %H:%M:%S %p"  #2018/10/15 16:27:45 PM
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt="%Y/%m/%d %H:%M:%S %p",
                filename='log.log',
                filemode='a')

#logging.debug('This is debug message')
#logging.info('This is info message')
#logging.warning('This is warning message')

def debug(msg):
    logging.debug(msg)

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

if __name__ == '__main__':
    warning('%Y %m %d %H:%M:%S')