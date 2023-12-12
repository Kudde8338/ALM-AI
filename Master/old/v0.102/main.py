import os

# variables
p1="$"
p1space=(p1+" ")
found_match=False


def startup():
    synthisis = input("Please select syntisiser: ")
    if synthisis == "math":
        return "./csv/math.values"
    elif synthisis == "speech":
        return "./csv/språk.kontroll"
    elif synthisis == "words":
        return "./csv/words"
    else:
        print("not found. Math has been loaded.")
        return "./csv/math.values"

def find_relevant_lines(prompt, file_path):
    with open(file_path, "r") as saved:
        lines = saved.readlines()

    # Split the prompt into words
    prompt_words = prompt.split()

    # Initialize a list to store relevant lines
    relevant_lines = []

    for line in lines:
        # Split each line into words
        line_words = line.split()

        # Check if there is at least one matching word (ignoring case)
        if any(all(letter.lower() in lw.lower() for letter in prompt_word) for prompt_word in prompt_words for lw in line_words):
            relevant_lines.append(line.strip())

    return relevant_lines

def relevancy(words, prompt):
    output = [word for word in words if len(word) < len(prompt) + 2]  # Adjusted the condition
    return output

        
        



path=startup()
prompt=input(p1space)
prompt_split=prompt.split()
for word in prompt_split:
    if os.path.exists(word):
        pass
    else:
        term=find_relevant_lines(word, path)
        result=relevancy(term, prompt)
        with open(word, "a") as file:
            for i in result:
                file.write(i + "\n")

