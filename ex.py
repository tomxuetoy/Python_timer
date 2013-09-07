import functools
import threading
import time
 
def hello(name):  
    print 'hello world, i am %s, Current time: %s' % (name, time.time())  
       
#hello = functools.partial(hello, 'guo')
t = threading.Timer(3, hello('xue'))
t.start()
