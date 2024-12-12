import io
import re

pattern = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

file = io.open("CSV/Marvel_DC.csv",
               "r", encoding='utf-8')
string_list = [string.replace(",,", ",ND,").replace(
    '""', '') for string in file.readlines()]

matrix = []

# Process each line and find matches
for string in string_list:
    temp = pattern.findall(string)
    matrix.append(temp)

# Initialise lists for films and scores
films = []
scores = []

# Extract films and scores
for row in matrix[1:]:  # Start from 1 to skip the header
    try:
        films.append(row[1])  # Film name
        scores.append(float(row[6]))  # Score
    except (ValueError, IndexError):
        continue  # Ignore if there is an error in conversion

# Analyse films with scores
num_films = len(scores)
if num_films == 0:
    print("There are no films with valid scores.")
else:
    # 1. Film with the highest score
    best_score = max(scores)
    best_film_index = scores.index(best_score)
    best_film = films[best_film_index]
    print(f"The film with the highest score is: {
          best_film} with a score of {best_score}")

    # 2. Film with the lowest score
    worst_score = min(scores)
    worst_film_index = scores.index(worst_score)
    worst_film = films[worst_film_index]
    print(f"The film with the lowest score is: {
          worst_film} with a score of {worst_score}")

    # 3. Average score
    mean_score = sum(scores) / num_films
    print(f"The average score of all films is: {mean_score:.2f}")

    # 4. Total number of films with valid scores
    print(f"The total number of films with valid scores is: {num_films}")
