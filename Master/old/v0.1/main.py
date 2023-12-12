import os


p1="$"
p1space=(p1+" ")
found_match=False
file="./csv/math.values"

startup = input("select method: ")
if startup == "math":
    file = "./csv/math.values"
elif startup == "speech":
    file = "./csv/språk.kontroll"

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

prompt=input(p1space)

# Old Code #
####################################################################################
#with open(file_path, "r") as saved:
#    b = prompt.split()
#    print(b)
#    for i in b:
#        saved.seek(0)
#        data=saved.read()
#        splited=data.split()
#        matching_lines = [line for line in splited if i.lower() in line.lower()]
#        for positivereturn in matching_lines:
#            print(positivereturn)
#            found_match = True

#if not found_match:
#    print("No match found.")
#    print("Would you mind telling me the answer.")
#    add_INFO = input(p1space)
# print(saved.read())
####################################################################################


result = find_most_relevant_line(prompt, file)
if result:
    print(result)
