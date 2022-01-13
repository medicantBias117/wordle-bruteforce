## generates the frequency for each letter. Approach is to combine all the words in a single massive string.
## And then, run a frequency count

wordslist = [];
with open("words_lawl.txt") as file:
    for line in file:
    	wordslist.append(line.rstrip());
currentString = "".join((wordslist))
  
# using set() + count() to get count 
# of each element in string 
res = {i : currentString.count(i) for i in set(currentString)}
# printing result 
print (str(res))
