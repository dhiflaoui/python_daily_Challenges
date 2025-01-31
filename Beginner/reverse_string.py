"""
Project Description
Your task for today is to write some code that reverses any string. There are two fundamentally different ways to accomplish this, 
one using a for-loop and another using string slicing. If you can, write both solutions.

"""
#Using a For-Loop

# text = "Python is fun!"

# reversed_text = ""

# for char in text:
#     reversed_text = char + reversed_text  


# print("Reversed string (using for-loop):", reversed_text)



#Using String Slicing
# Define the string
text = "Python is fun!"

# Reverse the string using slicing
reversed_text = text[::-1]

# Display the reversed string
print("Reversed string (using slicing):", reversed_text)