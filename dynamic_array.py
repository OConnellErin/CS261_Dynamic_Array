# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Erin O'Connell

import numpy as np

class DynamicArray:
    def __init__(self):
        self.capacity = 10
        self.next_index = 0
        self.data = np.empty(self.capacity,dtype=np.object)

    def is_empty(self):
        if self.next_index == 0:
            return True
        else:
            return False
    
    def __len__(self):
        return self.next_index

    def __getitem__(self, i):
        if i<0:
            raise IndexError
        if i>=self.next_index:
            raise IndexError
        return self.data[i]

    def append(self,i):
        self.data[self.next_index]=i
        self.next_index += 1

    def clear(self):
        self.data = np.empty(self.capacity,dtype=np.object)
        self.next_index = 0    

    def pop(self):
        self.next_index -= 1
        if self.next_index <= 0:
            raise IndexError
        return self.data[self.next_index]

    def delete(self,i):
        if self.next_index<=0:
            raise IndexError
        elif i >= self.next_index or i < 0:
            raise IndexError
        for i in range(i,self.next_index):
            self.data[i] = self.data[i+1]    
        self.next_index -=1  
        self.data[self.next_index] = None  

    def insert(self,number, value):
        # if self.next_index >= self.capacity: 
        #    raise IndexError   
        if number > self.next_index or number < 0:
            raise IndexError     
        for i in reversed(range(number+1,self.next_index,)):
            self.data[i] = self.data[i-1]
        self.data[number] = value    
        self.next_index +=1 