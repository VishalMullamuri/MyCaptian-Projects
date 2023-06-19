def most_frequent(string):    
    frequency = {}
    for letter in string:
        frequency[letter] = frequency.get(letter, 0) + 1   
    sorted_letters = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters:
        print(letter, count)

# Example 
string = "Mississippi"
most_frequent(string)
