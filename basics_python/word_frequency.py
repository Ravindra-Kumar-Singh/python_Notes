def count_word_frequency(sentence):
    # Your code goes here
    import string
    words = sentence.split()
    #print(words)
    cleaned_words = [word.lower().strip('.,!?";()') for word in words]
    #print(cleaned_words)
    freq = {word: cleaned_words.count(word) for word in cleaned_words}
    return freq

if __name__ == "__main__":
    sentence = "Hello, Hello world! Hello..."
    print(count_word_frequency(sentence))
