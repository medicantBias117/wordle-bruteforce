# Update (20th Jan)
So Marton Trencseni found the 5 words. Check it out here:
https://bytepawn.com/optimal-coverage-for-wordle-with-monte-carlo-methods-part-iii.html#optimal-coverage-for-wordle-with-monte-carlo-methods-part-iii
in no less than 13mins! 

I've gone ahead and thrown up a UI to help find solutions: https://wordle-assistant.herokuapp.com/
And added some explanation & justifications on why this approach works:
https://rkakodker.medium.com/wordle-solutions-using-5-magic-words-9331402842e5

Hope this helps


# Update (older)
I've made some approach changes. The below is the older approach. Here is the new approach: 
https://rkakodker.medium.com/brute-forcing-wordle-solutions-ce4c5f8d1200

# Summary
Wordle is an up & coming word game where you have to 'predict' a 5 letter word by guessing 5 5-letter words.
Each guess gives you a clue on the presence & position of the letter in the final word.
You can find more details here: https://www.powerlanguage.co.uk/wordle/

# Motivation
I'm decently good at words. I know my way around the language. I'm also exploring python & the Way of the Data Scientist™. Hence, I thought, let's throw science at this problem.

# Approach
You have technically, a 5 x 5 matrix where you have to provide 5 legitimate english words. Instead of applying actual science, I made like my ancestors and brute forced the issue. Because we have 5 words to fill out, we have 25 letters to fill, and in my naive mind, that means I can fill up 25/26 alphabets. So, if I asked Python nicely to take all 5 letter words (which I graceously supplied in the first place), and make a 5 words combination of them. 
Then for each combination, I squeezed the words togethers and found unique letters. 

Wherever I found greater than 23 unique letters, I stored. Else I discarded.

# Complexity
It is said, that a man who doesn't know how big (1951)C(5) is, doesn't really know about processing time. I can vouch for that statement.
The total number of combinations is 234,356,702,080,215. That's like a ... a lot. Like trillion lot. And I sort of gave up in the first 2 hours.
And went up only to about 300M.

# The First Optimization
(found in optimized.py)
In order to reduce the complexity, and hoping that there were more than 1 solutions to what I was seeking, it made sense to break the word list down by alphabets.
And then, you can iterate through word combinations like so: 
A B C D E
B C D E F
C D E F G
.
.
.

(I know what you're thinking... has he lost his mind? Wait till we reach optimization 4. Then you'll know, you're the crazy one.)

That ran for a while... with no successful results (I had a used a bad word dictionary that had some really arbitrary words). You can find a snapshot of the results in the Outputs folder: ultimate_file_copy.txt.

# Second, Third Optimization
The dictionary was a bust, so I went and found a better reliable source. The tiny_list.txt was good, but with only 667 entries, it wasn't fooling anyone. The Lawler wordlist proved to semi-useful. It still had some random chars showing up which had to be excluded.
Regardless, the plan was two-folds:
1. Randomize the list and break it into 5 parts
2. Make the 5 words combo from an element in the list
3. (if that didn't work, make the word selection random)

None of that actually worked. You can see the results.

# Final Optimization
This didn't really help, but the idea was that before you evaluate the word combinations, you'd first make sure that they're unique combinations. Somewhere along the way I thought I should remove all words with A & E in them, since:
[Letter Distribution Frequency](https://github.com/medicantBias117/wordle-bruteforce/blob/main/Images/letter_frequency.png)
<img src="https://github.com/medicantBias117/wordle-bruteforce/blob/main/Images/letter_frequency.png">

Not a big help. I also did some other things that should have improved. But alas! it didn't. Check out the code yourself.

# Conclusion
<b>Don't try to brute force complex problems. </b>

# Next Steps
Find another way to do this. Maybe from the clues that you'd have got from your first 2 attempts?
Also, something something area under the curve (letter frequency curve) <- I don't know what it means, but the Data Scientist who said it sounded super smart when she said it. There is probably something there.


# What words can I use?
You're still here? Alright, try these:

Index Lewis Depth Sugar Clock - 19 unique letters. Missing: B, F, J, M, Q, Y,  Z

As you can see, it's pretty shit.

Here is a code you can use to find what you're missing:

```python
x = "IndexLewisDepthSugarClock"
currentString = "".join((x.lower()))
uniqueString = ''.join(set(currentString))
print(uniqueString + "  " + str(len(uniqueString)))
print("".join(sorted(uniqueString))) ## Returns the sorted string

```

Thank you for wasting your time with me!
