import io
import re
import time

start_time = time.time()

pattern = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

file = io.open(
    "CSV/Marvel_DC.csv", "r", encoding='utf-8')

string_list = [line.replace(",,", ",ND,").replace(
    '""', '') for line in file.readlines()]

file.close()

matrix = [pattern.findall(line) for line in string_list[1:]]

genres = []

scores = []

for row in matrix:
    genres.append(row[3])
    scores.append(float(row[6]))

categories = list(set(genres))

total_scores = len(categories) * [0]

counts = len(categories) * [0]

for pos in range(len(genres)):
    index = categories.index(genres[pos])
    total_scores[index] += scores[pos]
    counts[index] += 1

for pos in range(len(total_scores)):
    print(categories[pos], total_scores[pos] / counts[pos])

end_time = time.time()

print(end_time - start_time)
