# Introduction
This project involves the implementation of first-order and Nth-order Markov models. The models were used on sentences and writing pieces to calculate transition probabilities and generate new text.

The Jupyter Notebook with the complete code and that should be reviewed is markov_models.ipynb.
# Pseudocode

```
def build_markov_model(markov_model, new_text, order):
  define start and stop states
  add start state to the text

  is our order greater than 1? if so:
    create a list of tuples that contains every n combo of words starting from i = 0 up until the last word in the text has at least n order of words that succeed it.
    (use this list of tuples for your order of words - if order = 1 just use the text split by whitespace with a start state added to it)


  for each index and current word/order of words in the text:
    if we are at a start state:
      if the start state is already in our markov model:
        if the next word is already in the inner dictionary mapped to our start state:
          add a count val of 1 to the inner dict val
        if the next word isn't in the inner dictionary:
          initialize it with a val of 1
      if the start state isn't already in our markov model:
          initialize it with the outer start key mapped to an inner dictionary with the key being the next word with a value of 1

    if we are at the end of the text:
      if the word/order of words is in the markov model:
        map the end state to 1 in the inner dictionary of the word/order of words
      if this is the first time encountering the word/order of words:
        add the word/order of words as a key in the outer dict and map the end state to 1 in the inner dictionary
      exit the loop

    if we're not at the start or the end of the text and the word/order of words is already in the markov model:
      if the next word in the text has already been encountered after the current word/order of words add 1 to the frequency val of the inner dict associated with that next word
      if the next word in the text hasn't been encountered initialize it as an inner dict key of the current word/order of words with a val of 1

    if we are not at a start state or end state, and haven't encountered the current word/order of words before:
      initialize the current word dict with a inner dict key of the next word in the text with a val of 1

  return the markov model
      
get_next_word
For every state in the Markov model:
  Add up how many times each possible next word occurs
  Convert counts into probabilities by dividing by the total
Look up the list of possible next words for the current state
Look up the corresponding probabilities for those next words
Randomly select one next word using those probabilities
Return the selected word


generate_random_text

Set random number generator with seed
Determine the Markov model order at the time 
Create a starting state using “*S” order number
Set the current state to the start state
Create an empty list to store the generated random words

Create a loop:  
  Pick the next word based on the current state
  If the next word equals “*E”
  Stop generating words
  If not,
      Add the word to the list
      To move to the next state, update the current state by dropping the oldest word and shifting to add the new word 

Join all the generated words to form a sentence
Return the sentence

Markov model for one fish two fish

Create an empty Markov model
Open the one_fish_two_fish.txt
Create an empty string to store the text
For each line in the file:
       Remove extra whitespaces from the line
	Add the line to the empty string
Use the string to train the Markov model with an order of 3 	
         
Markov model for sonnet
Create empty Markov model
Open sonnets.txt
Start with empty string for one sonnet
For each line in the file:
  Remove extra whitespace from the line
If the line is blank:
  Add the sonnet to the Markov model
  Reset the sonnet text to empty
Else:
  Add the line to the current sonnet text
Generate a random text sequence from the Markov model
```

# Successes
One of our biggest successes was that we learnt how a Markov model worked practically and how to implement them.


# Struggles
One struggle we faced was making current_word a tuple in the get_random_text function for n > 1. At first, the function we built was taking current_word as a string and trying to replace the tuple with a string. 
We initially struggled with placing the random seed on the right function so that it doesn't cause the randomness to reset every call and potentially lead to repetitive outputs. 

The most rewarding part of this project was getting to collaborate amongst peers to resolve bugs and talk through ideas.
An example of this comes from our generate_random_text() function. We initially had built it to only set the current word as the next word gathered from the get_next_word() function, which works fine for order = 1, but not so much for any other order. Our dilemma then became: 'how can we get every word from the current order of words except for it's very first element for orders greater than 1?' setting this new value equal to the current word would create a new tuple of words equal to the length of the order, with the next word included in the state.
We were able to talk through strategies for this as a team, and ended up splicing the current word state tuple to include everything but it's first element, and add the current word to the tuple to create the proper state for the next function call of get_next_word.

Ultimately we talked through many small steps like these to get the markov model and generate text for more complicated texts like Shakespeare sonnets.

# Struggles
One struggle we faced was making current_word a tuple in the get_random_text function for n > 1. At first, the function we built was taking current_word as a string and trying to replace the tuple with a string.

Another difficult thing to manage was the quantity of work required for the project and the time we had to work on it together. While we were able to talk through a lot of things in our meetings, we also still had a lot of work we each had to do on our own to get all the functions working. This meant that when we were working individually we had to update each other on what changes we were making to out code, why were making them, and how it would impact all other members.

Ultimately, continuing to communicate on teams when we were working individually and providing updates as we made changes helped us deal with this.
# Personal Reflections
## Group Leader
Sneha: Jersha and Connor were both great group members. We were able to meet three times to work through the code together and problem solve.  I had never worked with Markov models before, so I found the implementation to be a little challenging  It was very helpful to talk through the logic involved in Markov model implementation in order find solutions for bugs in our code.

## Other member
Aaronie Jersha Jenyfred: My group members were great to work with. This is my first time learning about Markov Models and I initially had a hard time understanding how to work around it but as a group we were able to co-ordinate very well in terms of building & debugging the code and trying to overcome some challenging errors. Discussing about the bugs and improvising the code together surely helped me understand the topic better. 
Connor: This project helped build more comfortability with group work and coding/programming. Meeting with group members multiple times to talk through ideas, logic, and code was very helpful for progressing through the project and developing my understanding of the material.
In regards to the actual project, I felt like I regained familiarity with nested dictionaries and implementing multiple control flow statements (elif ended up being very helpful, and it had been a while since I'd used it). This project required me to be more thoughtful in the debugging process, I had to slow down, and think about what part of the code bugs were most likely coming from, which I struggle to do at times. Print statements became my best friends in that process. I know our code isn't perfect as it is, and one thing I'm starting to realize is that refactoring is often warranted and helps you understand not just the code, but the ideas behind the code even better - a lesson I will be taking forward. With that in mind I think it will be interesting to see, considering these repos are continually active and can be changed, how much these projects get updated as we learn new things during the course.

# Generative AI Appendix
As per the syllabus
