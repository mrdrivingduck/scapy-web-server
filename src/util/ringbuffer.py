"""
    @author - mrdrivingduck
    @version - 2019.1.1
    @function - 
        A thread-safe ring queue.
"""

import threading


class RingBuffer(object):

    """
        @param size - Initial size of buffer
    """
    def __init__(self, size=100):
        if not isinstance(size, int):
            raise TypeError("Buffer size must be an integer")
        self.__buf_size = size
        self.__buff = [None] * size
        self.__head = 0
        self.__tail = 0
        self.__lock = threading.Lock()

    def empty(self):
        if self.__head == self.__tail:
            return True
        else:
            return False
    
    def full(self):
        if (self.__tail + 1) % self.__buf_size == self.__head:
            return True
        else:
            return False

    def length(self):
        return (self.__tail - self.__head + self.__buf_size) % self.__buf_size

    '''
        @return - element poped (None if buffer is empty)
    '''
    def pop(self):
        self.__lock.acquire()
        try:
            if self.empty():
                return None
            head = self.__buff[self.__head]
            self.__head = (self.__head + 1) % self.__buf_size
            return head
        finally:
            self.__lock.release()

    '''
        @param obj - element to be pushed
        @return - element poped if overflow
    '''
    def push(self, obj):
        self.__lock.acquire()
        try:
            overflow = None
            if self.full():
                overflow = self.pop()
            self.__buff[self.__tail] = obj
            self.__tail = (self.__tail + 1) % self.__buf_size
            return overflow
        finally:
            self.__lock.release()
