'''
    @author - mrdrivingduck
    @version - 2018.12.30
    @function - 
        A thread-safe ring queue.
'''

import threading

class RingBuffer():

    '''
        @param size - Initial size of buffer
    '''
    def __init__(self, size=100):
        if not isinstance(size, int):
            raise TypeError("Buffer size must be an integer")
        self.__bufsize = size
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
        if (self.__tail + 1) % self.__bufsize == self.__head:
            return True
        else:
            return False

    '''
        @return - element poped (None if buffer is empty)
    '''
    def pop(self):
        if self.empty():
            return None
        self.__lock.acquire()
        try:
            head = self.__buff[self.__head]
            self.__head = (self.__head + 1) % self.__bufsize
        finally:
            self.__lock.release()
        return head

    '''
        @param obj - element to be pushed
        @return - element poped if overflow
    '''
    def push(self, obj):
        overflow = None
        if self.full():
            overflow = self.pop()
        self.__lock.acquire()
        try:
            self.__buff[self.__tail] = obj
            self.__tail = (self.__tail + 1) % self.__bufsize
        finally:
            self.__lock.release()
        return overflow
        