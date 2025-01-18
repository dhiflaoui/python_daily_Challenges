#read book.txt file
#count the word in book
#print the word and count
print("*********Count the word in book*******")
word_count = input("Enter the word you want to count: ")
count = 0
with open("book.txt") as book:
    for line in book:
        words = line.split()
        count += words.count(word_count)

print(f"The word '{word_count}' appears {count} times in the file '{book.name}' ")