#Create a list of squares for numbers '1 to 10 using list comprehension.
squares=[x ** 2 for x in range(1,10)]
print(squares)

#Generate a list of even numbers between 1 and 20 using list comprehension.
even_numbers=[x for x in range(1,20)if x % 2== 0]
print(even_numbers)

#From the string "programming", make a list of unique letters using set comprehension.
word="programming"
unique_letters={letters for letters in word}
print(unique_letters)

#Make a dictionary where keys are numbers 1 to 5 and values are their cubes using dictionary comprehension.
cubes={x: x ** 2 for x in range(1,6)}
print(cubes)

#Convert a list of words ["apple", "banana", "cherry"] into a list of their lengths using list comprehension.
fruits = ["apple", "banana", "cherry"]
lengths = [len(fruits) for fruits in fruits]
print(lengths)

#Use set comprehension to create a set of even squares from [1, 2, 3, 4, 5, 6].
numbers=[1,2,3,4,5,6]
unique_squares=[x **2 for x in numbers]
print(unique_squares)

#Make a dictionary that stores each character and its ASCII value for the word "hello".
word = "hello"
ascii_dict = {char: ord(char) for char in word}
print(ascii_dict)

#Create a list of numbers from 1-30 that are divisible by both 2 and 3 using list comprehension.
numbers=[x for x in range(1,31)if x%2==0 and x%3==0]
print(numbers)

#Flatten the nested list [[1, 2], [3, 4], [5, 6]] using a nested list comprehension.
metrix=[[1,2],[3,4],[5,6]]
flat=[nums for row in metrix for nums in row]
print(flat)

#Convert the tuple (1, 2, 3, 4, 5) into a generator that yields each number squared, then convert it to a tuple and print it.
numbers=(1,2,3,4,5)
squares=(num **2 for num in numbers)
print(tuple(squares))