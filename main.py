import collections



def getColor(color):
    if color == "blue" or color == "wall":
        return "🟦"
    elif color == "red" or color =="path":
        return "🟥"
    elif color == "yellow" or color == "checked":
        return "🟨"
    elif color == "green" or color == "goal":
        return "🟩"
    elif color == "white" or color == "start":
        return "⬜"
    elif color == "0" or color == "empty":
        return "⬛"


class Node():
    def __init__(self) -> None:
        self.color = getColor("empty")

class Matrix():
    wall, clear, goal = getColor("wall"), getColor("clear"), getColor("goal")

    def __init__(self, width = 13, height = 10, start = (3, 3), goal = (8, 4)) -> None:
        self.matrix = [[Node() for x in range(width)] for x in range(height)]
        self.width = width
        self.height = height
        self.startPosition = start
        self.goalPosition = goal
        

        self.setStartPosition(start); self.setGoalPosition(goal)

        for i in range(self.width):
            self.setColor((i,0), getColor("wall"))
            self.setColor((i,-1), getColor("wall"))
        for i in range(self.height):
            self.setColor((0,i), getColor("wall"))
            self.setColor((-1,i), getColor("wall"))


    def setStartPosition(self, position):
        self.setColor(position, getColor("start"))


    def setGoalPosition(self, position):
        self.setColor(position, getColor("goal"))
    

    def setColor(self, position, color):
        x, y = position
        self.matrix[y][x].color = color


    def show(self):
        [print("".join([obj.color for obj in row])) for row in self.matrix]


    def bfs(self):
        # Startar queue
        queue = collections.deque([[self.startPosition]])

        # Loggar vilka noder man har  varit i
        seen = set([self.startPosition])

        # Kör så länge de finns queue
        while queue:
            # 
            path = queue.popleft()
            x, y = path[-1]
            if self.matrix[y][x].color == self.goal:
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if self.matrix[y2][x2].color != self.wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        print(path)




m = Matrix()

m.show()
m.bfs()




# 
# width, height = 10, 5
# 
# path = bfs(grid, (5, 2))
# 
# 
# 
# print(path)