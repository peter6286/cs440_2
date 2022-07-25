import random
class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def append(self, obj):  # 尾插法
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s


    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return '<<' + ','.join(map(str, self)) + '>>'


class HashTable:
    def __init__(self, size = 40):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def newhash(self):
        degree_in = random.randint(1, 40)
        degree_out = random.randint(1, 40)
        #print(degree_in,degree_out)
        #print(abs(degree_in-degree_out))
        if degree_in==degree_out or abs(degree_in-degree_out)==1:
            self.newhash()
        return degree_in,degree_out



    def insert(self, k):
        #for i in range(k):
        i = 0
        while i < k:
            degree_in,degree_out = self.newhash()
            if self.T[degree_in] == 3:
                print("already full")
                continue
            print(degree_in,degree_out)
            self.T[degree_in].append(degree_out)    #刚好错开一位才是在我们现在的node上
            i += 1



    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

def inithash(ht,size):
    for i in range(size-1):
        ht.T[i].append(i + 1)
    ht.T[size-1].append(1)
    return ht

ht = HashTable()
print(inithash(ht,40))

ht.insert(10)
print(ht.T)



