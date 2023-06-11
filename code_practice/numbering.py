list1 = [65, 67, "four", 4]
for i, value in enumerate(list1):
    print(i)


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []

for i, value in enumerate(list2):
    item = 0
    for j in range(i+1):
        item += list2[j]
    new_list.append(item)

print(new_list)       

def fizzBuzz(self, n: int) -> List[str]:
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