# Find every sentace on Londons wikipedia page where the word 'population' has been mentioned

import wikipedia

london = wikipedia.page("London")

# List of individual sentances
split_sentances =london.content.split(".")
sentaces_with_population_substring = []

for sentance in split_sentances:
    if("population" in sentance):
        sentaces_with_population_substring.append(sentance)
print(sentaces_with_population_substring)