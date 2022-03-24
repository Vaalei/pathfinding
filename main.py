import collections
import time


def getColor(color):
    if color == "blue" or color == "wall":
        return "🟦"
    elif color == "red" or color =="path":
        return "🟥"
    elif color == "yellow" or color == "seen":
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
    wall, clear, goal, seen, pathColor = getColor("wall"), getColor("clear"), getColor("goal"), getColor("seen"), getColor("path")

    def __init__(self, width = 13, height = 10, start = (3, 3), goal = (8, 4)) -> None:
        self.width = width
        self.height = height
        self.startPosition = start
        self.goalPosition = goal
        
        self.reset()


    def setStartPosition(self):
        self.setColor(self.startPosition, getColor("start"))


    def setGoalPosition(self):
        self.setColor(self.goalPosition, getColor("goal"))
    

    def setColor(self, position, color):
        if isinstance(position, tuple):
            x, y = position
            self.matrix[y][x].color = color
        elif isinstance(position, list):
            for pos in position:
                x, y = pos
                self.matrix[y][x].color = color


    def show(self, path=False):
        if path:
            self.setColor(path, self.pathColor)
        [print("".join([obj.color for obj in row])) for row in self.matrix]

        if path:
            self.reset()


    def reset(self):
        self.matrix = [[Node() for x in range(self.width)] for x in range(self.height)]

        for i in range(self.width):
            self.setColor((i,0), getColor("wall"))
            self.setColor((i,-1), getColor("wall"))
        for i in range(self.height):
            self.setColor((0,i), getColor("wall"))
            self.setColor((-1,i), getColor("wall"))

        self.setStartPosition()
        self.setGoalPosition()

    
    def createWall(self, start=False, stop=False):
        if start and not stop:
            self.setColor(start, self.wall)
        if start and stop:
            lst = []
            for x in range(start[0],stop[0]+1):
                for y in range(start[1],stop[1]+1):
                    lst.append((x, y))
            self.setColor(lst, self.wall)
        

    def bfs(self, verbose = False, interval=0.25):

        # Startar queue
        queue = collections.deque([[self.startPosition]])

        # Loggar vilka noder man har  varit i
        seen = set([self.startPosition])

        # Kör så länge de finns queue
        while queue:

            # Tar första elementet i queue och sätter path till det
            path = queue.popleft()

            # Delar upp path på x&y 
            # : tar de två sista elementen
            x, y = path[-1]

            # Kollar om den har hittat mål
            if self.matrix[y][x].color == self.goal:
                # Printar ut färdiga pathen om verbose == True
                if verbose:
                    print("\n")
                    self.show(path=path)

                # Skickar ut path till mål
                return path

            # Om man har valt att den ska visa hur den gör
            if verbose:
                print("\n")
                self.show()
                time.sleep(interval)
                if (x, y) != self.startPosition: 
                    self.matrix[y][x].color = self.seen

            # Loopar varje värde runt positionen som är vald
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):

                # Kollar så att den inte träffar vägg eller om programmet redan har varit där
                if self.matrix[y2][x2].color != self.wall and (x2, y2) not in seen:

                    # Lägger till i queue
                    queue.append(path + [(x2, y2)])

                    # Lägger till i vad som har setts
                    seen.add((x2, y2))

                        
m = Matrix(width=50, goal=(36,8))

m.createWall((6,1), (6,7))
m.createWall((10,8))
 
m.createWall((30,5), (46,5))
m.createWall((30,5), (30,8))

m.show()


path = m.bfs(verbose=True, interval=0.05)

#m.show(path=path)
