#
# @lc app=leetcode id=1117 lang=python3
#
# [1117] Building H2O
#

# @lc code=start
from threading import Barrier, Semaphore
class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.hydrogen_semaphore = Semaphore(2)
        self.oxygen_semaphore = Semaphore(1)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.hydrogen_semaphore:
            releaseHydrogen()
            self.barrier.wait()



    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.oxygen_semaphore:
            releaseOxygen()
            self.barrier.wait()
# @lc code=end

