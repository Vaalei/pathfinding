import collections
import time
import modules.matrixImporter


# No shit sherlock
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

# En nod med en färgvariabel
class Node():
    def __init__(self) -> None:
        self.color = getColor("empty")

# Class med matrix
class Matrix():

    wall, clear, goal, seen, pathColor = getColor("wall"), getColor("clear"), getColor("goal"), getColor("seen"), getColor("path")

    def __init__(self, width = 13, height = 10, start = (3, 3), goal = (8, 4), showOutput = False) -> None:
        # Lite variabler
        self.width = width
        self.height = height
        self.startPosition = start
        self.goalPosition = goal
        self.importedMatrix = False
        self.generateWalls = True
        self.showOutput = showOutput
        
        # Kallar funktionen reset
        self.reset()


    def setStartPosition(self, pos=False):
        if pos:
            self.startPosition = pos
        self.setColor(self.startPosition, getColor("start"))


    def setGoalPosition(self, pos=False):
        if pos:
            self.goalPosition = pos
        self.setColor(self.goalPosition, getColor("goal"))
    

    def setColor(self, position, color):
        # Om man skickar in en position i funktionen
        if isinstance(position, tuple):
            # Delar upp positionen i x och y
            x, y = position
            
            # Sätter objektet vid position x, y till färgen som skickas in
            self.matrix[y][x].color = color
        elif isinstance(position, list):
            for pos in position:
                x, y = pos
                self.matrix[y][x].color = color


    def show(self, path=False):
        if path:
            self.setColor(path, self.pathColor)
        print("\n")
        [print("".join([obj.color for obj in row])) for row in self.matrix]

        if path:
            self.reset()


    def reset(self):
        if not self.importedMatrix:
            self.matrix = [[Node() for x in range(self.width)] for x in range(self.height)]

            self.setStartPosition()
            self.setGoalPosition()

        if self.importedMatrix:
            matrix = self.importedMatrix
            self.width = len(matrix[0])
            self.height = len(matrix)
            self.matrix = [[Node() for x in range(self.width)] for x in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    current = matrix[y][x]
                    if current == "#": self.createWall((x,y))
                    if current == "s": self.setStartPosition(pos=(x,y))
                    if current == "g": self.setGoalPosition(pos=(x,y))
        if self.generateWalls:
            for i in range(self.width):
                self.createWall((i,0))
                self.createWall((i,-1))
            for i in range(self.height):
                self.createWall((0,i))
                self.createWall((-1,i))

    
    def createWall(self, start=False, stop=False):
        if start and not stop:
            self.setColor(start, self.wall)
        if start and stop:
            lst = []
            for x in range(start[0],stop[0]+1):
                for y in range(start[1],stop[1]+1):
                    lst.append((x, y))
            self.setColor(lst, self.wall)


    def getMatrix(self, file):
        if file:
            self.importedMatrix = modules.matrixImporter.getMatrix(file)
            self.reset()


    def bfs(self, verbose = False, interval=0.3):

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

            # Kollar om den har hittat mål och 
            if self.matrix[y][x].color == self.goal:
                # Printar ut färdiga pathen om verbose == True
                if self.showOutput or verbose:
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

                        
m = Matrix(width=50, goal=(36,8), showOutput=True)

m.getMatrix(file = "matrix.csv")
m.show()

m.bfs(verbose=True, interval=0.05)
