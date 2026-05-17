def word_frequency(file_path):
    """"this function reads a text from the file 
    and returns a dictionary with the frequency of words in the text."""
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:

            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?";()')  # Remove punctuation and convert to lowercase
                word_freq[word] = word_freq.get(word, 0)+1
    return word_freq
    
if __name__ == "__main__":
    file_path = 'basics_python\sample.txt'
    print(word_frequency(file_path))