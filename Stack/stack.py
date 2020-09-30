class Stack(object):

   def __init__(self):
      self._data = []
      
   def push(self, val):
      if not val:
         raise Exception("Invalid value provided")
      self._data.append(val):
      
    def pop(self):
       if not self._data:
          raise Exception("Stack is empty")
       return self._data.pop()
       
    def peek(self):
       if self._data:
          return self._data[-1]
       return None
       
    def is_empty(self):
       return len(self._data) == 0
