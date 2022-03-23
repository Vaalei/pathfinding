class Kalle():
    def __init__(self, row) -> None:
        self.text = "🟦"


class Matrix():
    def __init__(self) -> None:
        # build matrix
        
        self.matrix = [[Kalle(x) for x in range(10)] for x in range(8)]


        self.matrix[4][1].text="🟥"


    def show(self):
        # show matrix
        [print("".join([obj.text for obj in row])) for row in self.matrix]

m = Matrix()

m.show()