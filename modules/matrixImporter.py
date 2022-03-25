import csv
import numpy


def getMatrix(file):
    f = open(file, "r")
    matrix = []
    for row in f:
        matrix.append(row.split(","))
    
    #[print("".join([obj if obj != "" else " " for obj in row])) for row in matrix]
    return matrix
    

if __name__ == "__main__":
    getMatrix("matrix.csv")
