import functools
import threading
import time
 
def hello(name):  
    global t  
    t = threading.Timer(3, hello)  
    t.start()  
    print 'hello world, i am %s, Current time: %s' % (name, time.time())  
    
hello = functools.partial(hello, 'Tom')    
t = threading.Timer(3, hello)  
t.start()  
