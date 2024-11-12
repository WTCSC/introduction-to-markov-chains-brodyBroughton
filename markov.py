import random
import re
import argparse


def generate_text(start_word, num_words):
    """
    Generate new text using the Markov Chain, starting with a given word and
    generating a specified number of words:
    
    1. Start with the given word
    2. Add the word to the result list
    3. For the specified number of words:
        a. If the current word is in the transitions dictionary, choose a random next word
        b. Add the next word to the result list
        c. Update the current word to the next word
    4. Return the generated text as a string

    TODO: Clean up the generated text for better formatting and readability,
    e.g., capitalization, punctuation, line breaks, etc.
    """
    current_word = start_word
    result = [current_word.capitalize()]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            if next_word in ".,!?;":
                result[-1] += next_word
            else:
                result.append(next_word)
            current_word = next_word
        else:
            break
    # Capitalize the first word after ., ?, !
    for i in range(1, len(result)):
        if result[i-1][-1] in ".!?":
            result[i] = result[i].capitalize()
    return " ".join(result)

# Arg parser
parser = argparse.ArgumentParser(description="Generate text using a Markov chain")
parser.add_argument("start_word", help="The starting word for the generated text")
parser.add_argument("num_words", type=int, help="The number of words to generate")
args = parser.parse_args()

# Create the sample text and the dictionary to store word transitions
corpusFile = open("corpus.txt", "r")
text = corpusFile.read()
corpusFile.close()
transitions = {}

# Build the Markov Chain
# 1. Split the text into words
# 2. Iterate over the words
# 3. For each word, add the next word to the list of transitions
words = re.findall(r"[\w']+|[.,!?;]", text)
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
#print(transitions)
print(generate_text(args.start_word, args.num_words))

# Example usage, generating 10 words starting with "Mary"
# TODO: Accept user input for the starting word and number of words to generate