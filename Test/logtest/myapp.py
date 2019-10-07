# myapp.py
import os
import mylib


filename = os.path.basename(__file__)
mylib.set(filename,'Start')

test = 'a'
print(test)

mylib.set(filename,'End')
    
"""
def main():
    logging.basicConfig(filename='C:\work\81.python\Work\Test\logtest\log\myapp.log', format='%(asctime)s %(message)s',datefmt='%Y/%m/%d %I:%M:%S %p', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
"""