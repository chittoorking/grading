#!/usr/bin/env python
# coding: utf-8

# # Assessment - 5 Gradable
# 
# - Each question carries 5 or 4 marks
# - Marks will be assigned in terms of:
#     
#     **1. Expected output**
#     
#     **2. Quality and Explainability of code**
# 
#     ***Go back through the script and type a comment above each line explaining in English what it does.***
# 
#     **3. Copied code, if found, will result in 0 marks for that question. To avoid this make as much comments in the code to explain the approach**

# ### 1. 
# 
# Create a function ``lets_find_88`` Given a list of ints, return True if the array contains a 8 next to a 8 somewhere.
# - lets_find_88([1, 8, 8]) → True
# - lets_find_88([1, 8, 1, 8]) → False
# - lets_find_88([8, 1, 8]) → False

# In[1]:


#CREATING A FUNCTION TO FIND ADJACENT 8s
def lets_find_88(Lst):
    
    l=len(Lst)
    for i in range(0,l):
        if Lst[i]==8:
            if Lst[i]==Lst[i+1]:
                return(True)
            else:
                return(False)
            
#ENTERING A LIST OF NUMBERS FROM USER       
a=map(int,input("Enter a list of numbers:").split(","))
a=list(a)

#CALLING FUNCTION
c=lets_find_88(a)

#PRINTING RESULT
print(c)


# ### 2. 
# 
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter and returns False if both words begin with different letter
# - animal_crackers('Levelheaded Lion') --> True
# - animal_crackers('Cute Kangaroo') --> False

# In[4]:


def animal_crackers(text):
    wordlist = text.split() #split the text to words
    return wordlist[0][0] == wordlist[1][0] #compare first letter of first word with first letter of 2nd word and return true or false
result = animal_crackers('line lain')
print(result)


# ### 3. 
# 
# Write a function ``how_many_primes`` that returns the number of prime numbers that exist up to and including a given number
# 
# - how_many_primes(100) --> 25

# In[3]:


def how_many_prime(n):#.........User Defined Function to check the number of primes
    c=0#........................Initialising Count Variable as zero
    for num in range(1,n):#.......Using for loop to check if the number of primes upto n
        if num==1:#.............as 1 is neither prime nor composite we use continue statement
            continue
        for i in range(2,num):#........checking if n the given value of i is divisible by any other numbers
            if(num%i)==0:#.............if divisible then it is not prime and we break out from loop
                break
        else:
            c+=1#....................if not divisible by any number then update the count variable by 1
    return c
n=int(input("Enter a number :"))#.............Entering limit from user
print("Number of prime numbers upto",n,"=",how_many_prime(n))#......Function call and displaying the number of primes upto n


# ### 4. 
# 
# b = open("assignment.txt")
# 
# Consider the code given above and write the answers to the following :
# 
# - Identify the name of the file : 
# - Identify the name of the function used above : 
# - What is 'b' in above code :
# - The above statement will  ____________ file in ___________ mode.

# In[ ]:


#Name of the file is assignment
#open() is used here, it is used to open a file and return file object and it can take two parameters: 1.Path to the file and 2. File mode(read,write,append)
#b in the above code is known as file handle also known as fileobjectname and it is a reference instance to a file in disk,data may be written or read from file using it
#above statement will open the text file in read mode as the mode is not specified and default is read


# ### 5.
# 
# Accept five hobbies from the user and write in a file 'hobby.txt'. Then Read the file to list out all the 5 hobbies from the user.

# In[2]:


#Entering 5 hobbies from the user
h1=str(input("Enter hobby 1 :"))
h2=str(input("Enter hobby 2 :"))
h3=str(input("Enter hobby 3 :"))
h4=str(input("Enter hobby 4 :"))
h5=str(input("Enter hobby 5 :"))
#Opening a text file'hobby' in write mode
f=open("hobby.txt","w")
#Writing each hobby one by one into the file
f.write("The hobbies are\n")
f.write(h1)
f.write("\n")
f.write(h2)
f.write("\n")
f.write(h3)
f.write("\n")
f.write(h4)
f.write("\n")
f.write(h5)
#Closing the file
f.close()
#Opening the same file in read mode
f=open("hobby.txt","r")
#Reading the contents of the file
print(f.read())
f.close()


# In[ ]:




