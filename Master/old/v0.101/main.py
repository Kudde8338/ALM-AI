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
        return "./words/words"
    else:
        print("not found. Math has been loaded.")
        return "./csv/math.values"

def find_most_relevant_line(prompt, file_path):
    with open(file_path, "r") as saved:
        lines = saved.readlines()

    # Split the prompt into words
    prompt_words = prompt.split()

    # Initialize variables to track the most relevant line and the maximum number of matches
    most_relevant_line = None
    max_matches = 0

    for line in lines:
        # Split each line into words
        line_words = line.split()

        # Count the number of matching words (ignoring case)
        matches = sum(1 for prompt_word in prompt_words if any(all(letter.lower() in lw.lower() for letter in prompt_word) for lw in line_words))

        # Update the most relevant line if the current line has more matches
        if matches > max_matches:
            most_relevant_line = line.strip()
            max_matches = matches

    return most_relevant_line

path=startup()
prompt=input(p1space)
relevant_line=find_most_relevant_line(prompt, path)
print(relevant_line)

