#from .tasks import longtime_add
#import time
#if __name__ == '__main__':
#    url = ['http://www.guimp.com/'] # change them to your ur list.
#    for i in url:
#        result = longtime_add.delay(i)
#

from .tasks import longtime_add
import time
if __name__ == '__main__':
    for _ in xrange(10):
        result = longtime_add(1,2)
       # print 'Task finished?',result.ready()
        print 'Task result:',result
        time.sleep(1)
        #print 'Task finished"',result.ready()
        print 'Task result:',result