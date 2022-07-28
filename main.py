# Introduction
# This project is worked by Chenjia Li and Shuorong Zhu
# TA:Liam Schramm


# import part
import random


# function
def randomS(l):
    lnt = len(l)
    rn = random.randint(1, lnt)
    return l[rn - 1]


def sortL(l):
    if l == []:
        return l
    count = 0
    for i in l:
        l[count] = int(i)
        count = count + 1
    l.sort()
    count = 0
    for i in l:
        l[count] = str(i)
        count = count + 1
    return l


# class part
class graph:

    def __init__(self):
        self.graph = {}

    def addNode(self, k):
        # neighbours,target,agent
        self.graph[str(k)] = [[], 0, 0]  # 0 means not at the this Node

    def addEdge(self, k, val):
        if len(self.graph[str(k)][0]) == 3:
            # False, not able to add any more edges because it has reached maximal degree
            return 0
        else:
            list_temp = self.graph[str(k)][0]
            list_temp.append(str(val))
            self.graph[str(k)][0] = list_temp
            return 1

    def printNb(self):
        for p1, p2 in self.graph.items():
            if len(p2[0]) == 0:
                print("Node " + p1 + " has no edge.")
            if len(p2[0]) == 1:
                print("The Node " + p1 + " is connected to Node " + p2[0][0] + ".")
            if len(p2[0]) == 2:
                print("The Node " + p1 + " is connected to Nodes " + p2[0][0] + " and " + p2[0][1] + ".")
            if len(p2[0]) == 3:
                print("The Node " + p1 + " is connected to Nodes " + p2[0][0] + ", " + p2[0][1] + ", and " + p2[0][
                    2] + ".")

    def EvnSet(self, numN):
        for i in range(1, numN + 1):
            g.addNode(i)
            if i == numN:
                self.addEdge(i, i - 1)
                self.addEdge(i, 1)
            elif i == 1:
                self.addEdge(i, i + 1)
                self.addEdge(i, numN)
            else:
                self.addEdge(i, i - 1)
                self.addEdge(i, i + 1)
        newEcount = 0
        while not newEcount == 10:
            n1 = randomS(list(self.graph))
            if len(self.graph[n1][0]) == 3:
                continue
            n2 = n1
            while n2 == n1 or n2 in self.graph[n1][0] or len(self.graph[n2][0]) == 3:
                n2 = randomS(list(self.graph))
            self.addEdge(n1, n2)
            self.addEdge(n2, n1)
            newEcount = newEcount + 1
        for i in range(1, numN + 1):
            self.graph[str(i)][0] = sortL(self.graph[str(i)][0])

    def setA(self, pos):
        self.graph[str(pos)][1] = 1

    def setT(self, pos):
        self.graph[str(pos)][2] = 1

    def printT(self):
        for i in list(self.graph):
            if self.graph[i][1] == 1:
                print("Target is currently located at Node " + i + ".")
                return i

    def printA(self):
        for i in list(self.graph):
            if self.graph[i][2] == 1:
                print("Agent is currently located at Node " + i + ".")
                return i

    def clearAT(self):
        # function for set all the agent and target as 0
        pass

    def agent0(self):
        start_pos_a = randomS(list(self.graph))
        self.graph[start_pos_a][2] = 1

    def target_move_agent0(self):
        cur_pos = self.printT()
        self.graph[cur_pos][1] = 0
        nb_list = self.graph[cur_pos][0]
        next_pos = randomS(nb_list)
        self.graph[next_pos][1] = 1

    def bfs(self):
        target = self.printT()
        cur_pos = self.printA()
        q = [cur_pos]
        visited = set()
        visited.add(cur_pos)
        while q:
            node = q.pop()
            if node == target:
                return True
            for item in self.graph[node][0]:
                if item not in visited:
                    q.append(item)
                    visited.add(item)
        return False



# test part

g = graph()
g.EvnSet(40)
g.printNb()
g.setA(12)
g.setT(5)
print(g.bfs())
print("--------------------------------------------------")
g.printA()
print("--------------------------------------------------")
g.printT()