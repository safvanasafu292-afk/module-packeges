squares=[]
for x in range(1,6):
    squares.append(x ** 2)
print(squares)

#comprehension list
squares_comp=[x ** 2 for x in range(1,6)]

#with conditions
even_number=[x for x in range(10)if x %2 == 0]
print(even_number)

#with string
letters=[ch.upper()for ch in "hello"]
print(letters)

#set comprehension
numbers=[1,2,2,3,4,4,5]
unique_squares={x ** 2 for x in numbers}

#with conditions
even_set={x for x in numbers if x %2 == 0}
print(even_set)

#using range
even_number={x for x in range(10)if x % 2 == 0}
print(even_number)

#dictionary comprehension
squares_dict={x: x ** 2 for x in range(5)}
print(squares_dict)

#with conditions
even_squares_dict={x: x**2 for x in range(10) if x %2 == 0}
print(even_squares_dict)

#generator comprehension(tuple comprehension)
gen=(x ** 2 for x in range(5))
print(gen)
print(tuple(gen))

#using loop
gen=(x ** 2 for x in range(5))
print(gen)
for g in gen:
    print(g)

#nested comprehension(falttern a list of list)
metrix=[[1,2],[3,4],[5,6]]
flat=[num for row in metrix for num in row]
print(flat)

#multipication table pairs
pairs=[(x,y)for x in range(1,4) for y in range (1,4)]
print(pairs)
