import numpy as np
from collections import defaultdict

sentences = [
        "I am a developer",
        "I am currently enrolled in masters for data science",
        "I like data science"
       ]

unique_words = set(word for sentence in sentences for word in sentence.split(' '))
stop_words = "I a are is am in it for".split(" ")
meaningfull_words = [word for word in unique_words if word not in stop_words ]

frequencies = defaultdict(int)

for sentence in sentences:
    for word in meaningfull_words:
        if word in sentence:
            frequencies[sentence][word] += 1

print(unique_words)
print(stop_words)
print(meaningfull_words)
print(frequencies)
