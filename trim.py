with open("wordlist_lawler.txt") as file:
    for line in file:
    	if(len(line.rstrip()) == 5 ):
        	print(line.rstrip())