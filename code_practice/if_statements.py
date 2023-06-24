# checking use of if statement with comprehension




uno = "tres" if 3 == 0 else "no es tres"
print(uno)


dos = ["tres" if i > 0 else "no es tres" for i in range(4)]
print(dos)

example = [2,3,4,5,1,2,3,7]
tres = [i if i > 3 else "menor a tres" for i in example]
print(tres)








if __name__ == "__main__":
    pass


