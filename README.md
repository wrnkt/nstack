## N Stack

### Gameplay:

There are 3 stacks of letters.
The middle stack is a supply of letters.
The side stacks are used to create words.
Move letters from the center stack to the side stacks and try to create words on
them.
Your score is based on how many words you can create within a certain number of
tiles.

### TODO:
[] test different algorithms to find the most possible words that can be created
 (given a number (2) of play stacks and one source stack)

### Algorithms
1. Utilize multiple character checks at once
 - stick together common sequences of letters that occur in words
  like vowel consonant pairs ("he", "we", "ea")
 - reduces check time
2. Brute force

### Concerns:

- letter generation
 compare both random and predetermined letter generation for difficulty
 * can generate predetermined letters by starting with word lists on play stacks
   and then loading them at random to the center stack (can be broken by random
   numbers to determine difficulty
   Ex: "makefeastmusty" "atdhherhamehrsdfname"
- consider adding more stacks
