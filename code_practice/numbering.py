list1 = [65, 67, "four", 4]
for i, value in enumerate(list1):
    print(i)


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []

for i, value in enumerate(list2):  # creates a new list adding the values in an original list
    item = 0
    for j in range(i+1):
        item += list2[j]
    new_list.append(item)

print(new_list)       

# function to run the fizzbuzz test



def fizzBuzz(self, n: int):
        result = []
        for i in range(1, n + 1):
            print(i)
            if i % 3 and n % 5 == 0:
                word = "FizzBuzz"
            elif i % 3 == 0:
                word = "Fizz"
            elif i % 5 == 0:
                word = "Buzz"
            else:
                word = str(i)
            print(word)    
            result.append(word)
        return result      

#same but with comprehension


test = [ "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 16)]
print(test)


















if __name__ == "__main__":
    pass





