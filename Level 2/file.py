def count_word_occurrences(text):
    
    words = text.lower().split()

    
    word_count = {}
    for word in words:
       
        word = ''.join(char for char in word if char.isalnum())
        if word:  
            word_count[word] = word_count.get(word, 0) + 1

   
    sorted_word_count = dict(sorted(word_count.items()))

    return sorted_word_count

def main():
    
    text = input("Enter sentences (or a paragraph): ")

    
    word_occurrences = count_word_occurrences(text)

    
    print("\nWord occurrences:")
    for word, count in word_occurrences.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
