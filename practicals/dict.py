# (a) Given a string, create a dictionary where keys are words & values are word lengths
# (a) Create dictionary of word : length

sentence = input("Enter a sentence: ")

# Split into words
words = sentence.split()

# Dictionary with word length
word_lengths = {word: len(word) for word in words}

print("Word Length Dictionary:", word_lengths)

# (b) Given a list of integers, find all pairs whose sum = target


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))

pairs = []

# Check all pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs with sum", target, ":", pairs)


# (c) Rotate tuple by n positions

t = tuple(input("Enter tuple elements separated by space: ").split())
n = int(input("Enter number of positions to rotate: "))

# Left rotation
left_rotated = t[n:] + t[:n]

# Right rotation
right_rotated = t[-n:] + t[:-n]

print("Original Tuple:", t)
print("Left Rotated :", left_rotated)
print("Right Rotated:", right_rotated)
