#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#

# @lc code=start
from threading import Condition,Lock,Event
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_event = Event()
        self.foo_event.set()
        self.bar_event = Event()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_event.wait()
            printFoo()
            self.foo_event.clear()
            self.bar_event.set()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_event.wait()
            printBar()
            self.bar_event.clear()
            self.foo_event.set()
            
# @lc code=end

