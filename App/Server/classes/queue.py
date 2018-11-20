# modual of classes to use in code.

# Implementation of a queue
class Queue:
    def __init__(self):
        self.queue = []

    # Dequeue from list, return None if no data
    def dequeue(self):
        if len(self.queue) > 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return None
    
    # Add data to the que
    def enqueue(self,data):
        self.queue.append(data)

    # Return length of queue
    def len(self):
        return len(self.queue)

    # Return true if queue has data
    def isdata(self):
        return self.len() != 0
