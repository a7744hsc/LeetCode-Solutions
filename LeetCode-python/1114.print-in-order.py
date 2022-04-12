#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
from threading import Lock,Condition
class Foo:
    def __init__(self):
        self.first_is_called=False
        self.second_is_called=False
        self.condition = Condition(Lock())


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.condition:
            self.first_is_called=True
            printFirst()
            self.condition.notify_all()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:
            while not self.first_is_called:
                self.condition.wait()
            self.second_is_called=True
            printSecond()
            self.condition.notify_all()
        # printSecond() outputs "second". Do not change or remove this line.


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:
            while not self.second_is_called:
                self.condition.wait()
            printThird()
            # printThird() outputs "third". Do not change or remove this line.
# @lc code=end

