Python
Array  [sets, lists, tuples, dictionary] //(strlen, push, pop, add to string, delete from string)
    change the value of an index:
      thislist = ["apple", "banana", "cherry"]
       thislist[1] = "blackcurrant"
      print(thislist)

#tuples
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) 

#sets
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)                  #will add orange after cherry

#python class
class user:
    pass
user1=user()
user1.firstname= input ("enter first name")
print (user1.firstname)


#numpy example
        # Std Dev. (std dev p in excel)
a =[0,1,2]
b= np.std(a)
print (b)  #end std numpy array

#mean in numpy
np.mean(a) // puts out the mean

a.range (0,10) -> prints out 0-9 numbers


                                            #Pandas
s = pd.Series([1,2,3])
(online book stopped on page 71)


//showing plot          #showing plot
x=[1,2,3]
y=[1,4,9]
plt.plot(x,y)
plt.show()
