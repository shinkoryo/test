# mylib.py
import logging

def set(nnn,info):
    fn = "C:\work\81.python\Work\Test\logtest\log\\" +nnn + ".log"
    logging.basicConfig(filename= fn, format='%(asctime)s %(message)s',datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.INFO)
    
    if info == 'Start':
        logging.info('Start')
    else :
        logging.info('End')