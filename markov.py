import random, re, argparse

def generate_text(start_word, num_words):
    """
    Generate new text using the Markov Chain, starting with a given word and
    generating a specified number of words
    """
    current_word = start_word
    result = [current_word.capitalize()] # Capitalizes first word
    for _ in range(num_words - 1):
        if current_word in transitions: # If current word is in transitions, select a random next word
            next_word = random.choice(transitions[current_word]) 
            if next_word in ".,!?;": # If random word is punctuation, append it to the last word without a space
                result[-1] += next_word 
            else: # Otherwise, append the word to the result list
                result.append(next_word)
            current_word = next_word
        else: 
            break
    # Capitalize the first word after ., ?, !
    for i in range(1, len(result)):
        if result[i-1][-1] in ".!?":
            result[i] = result[i].capitalize()
    return " ".join(result) + "."

# User input
parser = argparse.ArgumentParser(description="Generate text using a Markov chain")
parser.add_argument("start_word", help="The starting word for the generated text")
parser.add_argument("num_words", type=int, help="The number of words to generate")
args = parser.parse_args()

# File reading
corpusFile = open("corpus.txt", "r")
text = corpusFile.read()
corpusFile.close()

transitions = {}

# Splits the text into all words and punctuation and adds it to transitions dictionary
words = re.findall(r"[\w']+|[.,!?;]", text)
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

print(generate_text(args.start_word, args.num_words))