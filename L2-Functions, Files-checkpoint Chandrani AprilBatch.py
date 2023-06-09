#!/usr/bin/env python
# coding: utf-8

# # Functions
# - Write solution of each question in the cell given below the corresponsing question.
# - Function taking input refers to input as a parameter / argument being passed.

# #### 1. Create a function that takes a list of numbers as input and returns the median.

# In[1]:


def return_median(L):#User defined function to calculate median
    import numpy as np#importing numpy library to perform mathematical operations
    md=np.median(L)#Calculating median of the given list of numbers using median() function
    return(md)
l=map(int,input("Enter a list of numbers seperated by commas :").split(","))#Getting a list of numbers from user
l=list(l)
med=return_median(l)#Function Call
print("Median=",med)#Displaying median of the given numbers


# In[ ]:





# #### 2. Create a function that takes a list of numbers as input and returns the mean.

# In[4]:


def return_mean(L):#User defined function to calculate mean
    import numpy#importing numpy library to perform mathematical operations
    mn=numpy.average(L)#Calculating mean of the given list of numbers using average() function
    return(mn)
l=map(int,input("Enter a list of numbers seperated by commas :").split(","))#Getting a list of numbers from user
l=list(l)
l=list(l)
av=return_mean(l)#Function Call
print("Average=",av)#Displaying mean of the given numbers


# In[ ]:





# #### 3. Create a function that takes a list of numbers as input and returns the standard deviation.

# In[5]:


def return_standarddeviation(L):#User defined function to calculate standard deviation
    import numpy#importing numpy library to perform mathematical operations
    s=numpy.std(L)#Calculating standard deviation of the given list of numbers using std() function
    return(s)
l=map(int,input("Enter a list of numbers seperated by commas :").split(","))#Getting a list of numbers from user
l=list(l)
std=return_standarddeviation(l)#Function Call
print("Standard Deviation=",std)#Displaying standard deviation of the given numbers


# In[ ]:





# #### 4. Create a function that takes a number as input and return True if the number is prime , False if not.

# In[6]:


def primeornot(n):#User defined functi80on to check if a number is prime or not
    for j in range(2,n):#Using for loop to check if the given number is divisble by any number b/w 2 and the given number
        if n%j==0:#If divisible by any number then return False as the number is composite and then break out from loop
            return(False)
            break
        else:
            return(True)#If not divisible by any number then return True as the number is prime
n=int(input("Enter a number :"))#Entering a number from user
res=primeornot(n)#Function Call
print(res)#Displaying the result


# #### 5. Create a function that takes a list of numbers as input and returns the variance.

# In[7]:


def return_variance(L):#User defined function to calculate variance
    import numpy#importing numpy library to perform mathematical operations
    mn=numpy.var(L)#Calculating standard deviation of the given list of numbers using var() function
    return(mn)
l=map(int,input("Enter a list of numbers seperated by commas :").split(","))#Getting a list of numbers from user
l=list(l)
av=return_variance(l)#Function Call
print("Variance=",av)#Displaying variance of the given numbers


# #### 6. Create a function that takes a number as input and returns the factorial.

# In[9]:


def factorial(n):#User defined function to find factorial of a given number
    fact=1
    for i in range(1,n+1):#if the given number=5 then i takes values 1,2,3,4,5 in each iteration
        fact=fact*i#Successive values of i is multiplied into fact which will then have value 1*2*3*4*5=120 which is 5!
    return(fact)
n=int(input("Enter a number"))#Getting a number from the user
f=factorial(n)#Function Call
print("Factorial=",f)#Displaying Result


# #### 7. Create a function that takes two lists of same length as input and returns a list consisting of larger element at each position after comparing the corresponding elements in the given lists.

# In[10]:


def compare(l1,l2):#User defined function to compare elements of two lists
    l=[]#Initialising an empty list
    if len(l1)!=len(l2):#Checking if two lists are of equal length
        print("Enter lists of same length")
    else:
        for i in range(len(l1)):#Using for loop to compare the two lists
            if l1[i]>l2[i]:#Checking if an element of list1 is greater than the corresponding element of list2
                l.append(l1[i])#If yes then append list1 element to the list l
            else:
                l.append(l2[i])#If not then append list2 element to list l
    return(l)
#Entering two lists from user
a=map(int,input("Enter list 1 seperated by commas :").split(","))
b=map(int,input("Enter list 2 seperated by commas :").split(","))
a=list(a)
b=list(b)
d=compare(a,b)#Function Call 

#Displaying Result
print("The larger elements from both lists are :")
print(d)


# #### 8. Create a function that takes a string and returns a string after joining the words that are having even lengths.

# In[11]:


def evenstr(st):#User defined function to find the even lettered words of a string
    c=[]#Initialising an empty list
    l=str(st).split(" ")#Splitting the given string into a list based on blank spaces
    ln=len(l)
    for i in range(ln):#Using for loop to check the length of each word
        if len(l[i])%2==0:#if length is even then append the word into the list c
            c.append(l[i])
    st=" "
    return(st.join(c))#Joining the list to create a string and returning that string
st=str(input("Enter a string :"))#Entering a string from the user
st1=evenstr(st)#Function call
print("The even lettered words are :")#Displaying the result
print(st1)


# #### 9. Create a function that takes a string and a character as input and returns a list after splitting the string based on the given character. By Default split based on whitespace. (Create a function similar to the inbuilt split function without using it).

# In[12]:


def split_string(st,ch):#User defined function split a string based on a given character
    l=[]#Initialising an empty list
    
    #Using for loop and if condition to append each letter of the string follwed by character into the empty list
    for i in range(len(st)-1):
        if st[i]!=" ":
            l.append(st[i])
            if st[i+1]!=" ":
                l.append(ch)
    l.append(st[len(st)-1])        
    return(l)
        
st=str(input("Enter a string :"))#Entering a string from user
ch=str(input("Enter a character :"))#Entering a character from the user
l=split_string(st,ch)#Function Call
print("The result is :")#Displaying the result
print(l)


# #### 10. Create a function which takes a 2-D list of shape m * n where m is number of elements in the original list and where each element is a list having n integers (A list of m lists having n numbers each, a matrix). The function returns the largest element in the given list.

# In[13]:


def two_dim_array(matrix,r,c):#Function to find largest element of a matrix
    mx=matrix[0][0]#initialising the variable mx with the 1st element of the matrix
    #Using for loop and if statement to check if any element is greater than mx
    for i in range(r):
        for j in range(c):
            if matrix[i][j]>mx:#If yes then update the value of mx
                mx=matrix[i][j]
    return(mx)
import numpy as np#Importing numpy library to create a 2D Matrix
#Entering the number of rows and columns from the user
r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))

#Entering the elements of the matrix from the user
print("Enter the elements of the matrix(total",r*c,")","seperated by space :")
entries=list(map(int,input().split(" ")))

#Using reshape() function to create a 2D Matrix
matrix=np.array(entries).reshape(r,c)

#Displaying the 2D Matrix
print("The 2D matrix is :")
print(matrix)

#Function Call
mx=two_dim_array(matrix,r,c)

#Displaying the result
print("Maximum Value=",mx)


# #### 11. Create a function which takes a 2-D list of shape m * n where m is number of elements in the original list and where each element is a list having n integers (A list of m lists having n numbers each). The function also takes a number x as input and returns True is x is in the given 2D list.

# In[36]:


def find_ele(matrix,r,c,x):#Function to check if the given number present in matrix
    flag=0#Initialising Flag variable as zero
    #Using for loop to check if given number present
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==x:#If present return true, update flag variable and break out from loop
                return(True)
                flag=1
                break
    if flag==0:#if flag=0 return false
        return(False)
            
           
     
            
    
import numpy as np#Importing numpy library to create a 2D Matrix
#Entering the number of rows and columns from the user
r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))

#Entering the elements of the matrix from the user
print("Enter the elements of the matrix(Total",r*c,")seperated by space:")
entries=list(map(int,input().split(" ")))

#Using reshape() function to create a 2D Matrix
matrix=np.array(entries).reshape(r,c)

#Entering the element to search from the user
x=int(input("Enter element to search :"))

#Displaying the 2D Matrix
print("The 2D array is:")
print(matrix)

#Function Call
c=find_ele(matrix,r,c,x)
print("Element present in matrix hence", c)


# #### 12. Create a function which takes a 2-D list of shape m * n where m is number of elements in the original list and where each element is a list having n integers (A list of m lists having n numbers each). The function returns the sum of all rows in the matrix (2 D list).

# In[20]:


def fun(matrix,c):#Fuction to find the sum of all rows of a matrix
    sum=0#Initialising sum as zero
    for i in range(c):#Using for loop to find the sum of each row
        sum+=matrix[i]
    return(sum)
import numpy as np#Importing numpy library to create a 2D Matrix

#Entering the number of rows and columns from the user
r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))

#Entering the elements of the matrix from the user
print("Enter the elements of the matrix( total",r*c,")seperated by space:")
entries=list(map(int,input().split(" ")))

#Using reshape() function to create a 2D Matrix
matrix=np.array(entries).reshape(r,c)

#Displaying the 2D Matrix
print("The 2D matrix is:")
print(matrix)

#Function Call and Displaying Result
for i in range(r):
    d=fun(matrix[i],c)
    print("Sum of row",i+1,"=",d)


# #### 13. Create a function which takes a 2-D list of shape m * n where m is number of elements in the original list and where each element is a list having n integers (A list of m lists having n numbers each). The function also a takes a number x as input and returns a list of all consecutive pairs having sum eaqqual to x.

# In[21]:


def check_sum(m,r,c,x):#Function to find all consecutive pairs having a given sum
    l=[]
    a=[]
    #Converting the 2D martrix into a 1D list
    for i in range(r):
        for j in range(c):
            l.append(m[i][j])
    ln=len(l)
    #Checking if the consecutive pairs of elements have sum equal to x 
    for i in range(ln-1):
        c=[]
        if l[i]+l[i+1]==x:#if yes then append the pair into the list c
            c.append(l[i])
            c.append(l[i+1])
            a.append(c)
    return(a)
import numpy #Importing numpy library to create a 2D Matrix

#Entering the number of rows and columns from the user
r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))

#Entering the elements of the matrix from the user
print("Enter the elements of the matrix(total",r*c,")seperated by blankspace")
entries=list(map(int,input().split(" ")))

#Using reshape function to create matrix
matrix=numpy.array(entries).reshape(r,c)

#Displaying the 2D Matrix
print("The 2D Matrix is :")
print(matrix)

#Entering a number from the user
x=int(input("Enter a number :"))

#Function Call
a=check_sum(matrix,r,c,x)

#Displaying Result
print("List of all consecutive pairs having sum equal to",x,"is :")
print(a)


# #### 14. Create a function that takes a list and a number as input and returns True ifthe number is present in the list otherwise false using Binary search algorithm. (Read about Binary Search).

# In[22]:


#Function to return index where element was found else return None
def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while(start <= end):
        mid = (start + end) // 2
        #if target is smaller ignore right half
        if(lst[mid] > target):
            end = mid - 1
        #if target is greater ignore left half
        elif(lst[mid] < target):
            start = mid + 1
        #if target present at mid
        else:
            return mid
    #if not found
    return None
#Entering list of elements from user
lst=list(map(int,input("Enter elements of the list seperated by commas :").split(",")))
#Entering element to search
target=int(input("Enter element to search:"))
#Function Call
c=binary_search(lst,target)
#Display Result
print("Element found at index :",c)


# #### 15. Create a function which takes a txt filename as input and returns the number of words in that file.

# In[23]:


def countWord(Text):#Function to count words of a file
    f=open("TEXT.txt")#Opening the text file
    s=f.readlines()#Using readlines() to create a list contining each line of file as list item
    l=str(s).split(" ")#Creating a new list by splitting each line word by word
    ln=len(l)#Taking the length of the new list which is the total number of words in the file
    return(ln)


#Opening text file in write mode
f=open("TEXT.txt","w")

#Writing values into file
s=str(input("Enter string 1 :"))
d=str(input("Enter string 2 :"))
f.write(s)
f.write("\n")
f.write(d)
f.close()

#Opening text file in read mode and reading contents of the file and displaying it
f=open("TEXT.txt","r")
print("\nThe Contents of the file are \n")
print(f.read())

#Function call to count number of words
c=countWord("TEXT.txt")
print("\n")
#Printing number of words
print("Number of words in the file=",c)


# #### 16. Create a function which takes a txt filename as input and returns the number of line in the file.

# In[26]:


def line_count(text):#Function to count lines of a file
    f1=open("text.txt")#Opening the text file
    s=f1.readlines()#Using readlines() to create a list contining each line of file as list item
    l=len(s)#Taking the length of the list which is the total number of lines in the file
    return(l)

#Opening text file in write mode
f=open("TEXT.txt","w")

#Writing values into file
L1=str(input("Enter line 1:"))
L2=str(input("Enter line 2:"))
L3=str(input("Enter line 3:"))
L4=str(input("Enter line 4:"))
L5=str(input("Enter line 5:"))
f.write(L1)
f.write("\n")
f.write(L2)
f.write("\n")
f.write(L3)
f.write("\n")
f.write(L4)
f.write("\n")
f.write(L5)
f.write("\n")
f.close()
print("\n")

#Opening text file in read mode and reading contents of the file and displaying it
f=open("TEXT.txt","r")
print("The contents of the file is:")
print(f.read())

#Function call to count number of words
L=line_count("TEXT.txt")
#Displaying the result
print("Number of lines=",L)


# #### 17. Create a function that takes two txt filenames and returns a file after merging the cintents of two given files. (Print the merged content and then return the filename, content of original files should be unchanged).

# In[27]:


def merge_file(text1,text2):#Function to merge contents of two files
    
    #Opening the text files
    f1=open("text1.txt")
    f2=open("text2.txt")
    
    #Using readlines() to create a list contining each line of file as list item
    s1=f1.readlines()
    s2=f2.readlines()
    
    #Combining the two lists to create a single list
    s=s1+s2
    f1.close()
    f2.close()
    
    #Converting the merged list into a string
    st=" ".join(map(str,s))
    
    #Opening a new file and writing the contents into that file
    f3=open("text.txt","w")
    f3.write(st)
    f3.close()
    return("text.txt")

#Opening two text files in write mode and writing content into the file
f1=open("TEXT1.txt","w")
s1=str(input("Enter the text to be written into file 1 : "))
f1.write(s1)
f1.close()
f2=open("TEXT2.txt","w")
s2=str(input("Enter the text to be written into file 2 : "))
print("\n")
f2.write(s2)
f2.close()

#Function Call
f=merge_file("TEXT1.txt","TEXT2.txt")

#Opening the 2 text files in write mode and displaying its contents
f=open("TEXT.txt","r")
f1=open("TEXT1.txt","r")
print("Contents of file 1 :")
print(f1.read())
print("\n")
f2=open("TEXT2.txt","r")
print("Contents of file 2 :")
print(f2.read())
print("\n")

#Displaying contents of the new file
print("Contents in new file :")
print(f.read())


# #### 18. Write a program that takes a string as input and returns a list of all words having even length in that string (Using Map/Filter and Lambda expression).

# In[29]:


st=str(input("Enter a string :"))#Entering string from the user
s=st.split(" ")#Splitting the string into a list
l=list(filter(lambda x:(len(x)%2==0),s)) #Using lambda() and filter to return even lettered words
print(l)#Displaying the result


# In[ ]:




