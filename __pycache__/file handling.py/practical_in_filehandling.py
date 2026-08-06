#Create a text file and write your name into it.
with open("name.txt","w") as file:
    file.write("safvana")
#Write 3 favorite movies to a file and read them back.
with open("movie.txt","r+")as file:
    file.write("vazha,spiderman,blackkman")
    file.seek(0)
    moive=file.readline()
    print(moive)
#Create a file, write a poem line by line using writelines.
poem = [
    "Twinkle, twinkle, little star,\n",
    "How I wonder what you are!\n",
    "Up above the world so high,\n",
    "Like a diamond in the sky.\n"
]
with open("poem.txt", "w") as file:
    file.writelines(poem)
with open("poem.txt", "r") as file:
    print(file.read())
#Read only the first line of a file.
with open("poem.txt","r")as file:
    fristline=file.readline()
    print(fristline)
#Append your daily tasks to "todotxt".
with open("todo1.txt","a")as file:
    file.write("my daily task\n")
    file.write("Wake up early\n")
    file.write("Study Python\n")
    file.write("Complete homework\n")
    file.write("Exercise\n")
    file.write("Read a book\n")
print("Daily tasks appended successfully.")
#Count how many lines exist in a file.
with open("poem.txt","r")as file:
    lines=file.readline()
    print("numbers of lines:",len(lines))
#Read a file and display the longest word
with open("movie.txt","r")as file:
    text=file.read()
word=text.split()
longest=max(word,key=len)
print("longest word:",longest)
#Try opening a non-existing file — handle FileNotFoundError.
try:
    with open("demo.txt","r")as file:
        print (file.read())
except FileNotFoundError:
    print("Error file donot exist")
#Copy contents from one file to another.
with open("poem.txt", "r") as file:
    content = file.read()

with open("destination.txt", "w") as file:
    file.write(content)

print("File copied successfully.")

#Delete the file after confirmation using os.remove().
import os

filename = "source.txt"

choice = input("Do you want to delete the file? (yes/no): ")

if choice.lower() == "yes":
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File does not exist.")
else:
    print("File was not deleted.")
 



    