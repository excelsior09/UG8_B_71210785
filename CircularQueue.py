from Node import Node

class CircularQueue:
       def __init__(self,cap):
              self.head = None
              self.tail = None
              self.size = 0
              self.capacity = cap

       def isEmpty(self):
              return self._size == 0

       def enqueue(self,d):
              if self.size < self.capacity:
                     baru = Node(d)
                     if self.size == 0:
                            self.head = baru
                            self.tail = baru
                     else:
                            self.tail._next = baru
                            self._prev = self.tail
                            self.tail = baru
                     
                     self.size = self.size + 1
              else:
                     print("penuh")

       def denqueue(self):
              if self.size > 0:
                     if self.size == 0:
                            self.head = None
                            self.tail = None
                     else:
                            hapus = self.head
                            self.head = self.head._next
                            hapus._next = None
                            self.head._prev = None
                            return hapus._data
                            del hapus
                     self.size = self.size - 1

       def __len__(self):
              return self.size

       def front(self):
              return self.data[self.front]

       def display(self):
              bantu = self.head
              print("Yang ada pada antrian adalah: ", end="")
              while bantu!=None:
                     print(bantu._data, " ", end="")
                     bantu = bantu._next
              print()

CircularQueue = CircularQueue(5)
CircularQueue.enqueue(14)
CircularQueue.enqueue(22)
CircularQueue.enqueue(13)
CircularQueue.enqueue(-6)
CircularQueue.display()
print("Data yang dihapus adalah:", CircularQueue.denqueue())
print("Data yang dihapus adalah:", CircularQueue.denqueue())
CircularQueue.display()
CircularQueue.enqueue(9)
CircularQueue.enqueue(20)
CircularQueue.enqueue(5)
CircularQueue.display()