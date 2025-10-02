from collections import Counter
import string

def analyze_text(text):
    # Number of characters
    num_chars = len(text)
    
    # Number of lines
    lines = text.split('\n')
    num_lines = len(lines)
    
    # Remove punctuation and split words
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.lower().split()
    num_words = len(words)
    
    # Word frequency
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(10)
    
    # Display results
    print("\n📊 Text Analysis Results 📊")
    print(f"Total characters: {num_chars}")
    print(f"Total words: {num_words}")
    print(f"Total lines: {num_lines}")
    print("\nTop 10 most common words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

def main():
    print("📄 Word Count and Frequency Analysis Tool 📄")
    print("Enter your text below (press Enter twice to finish):\n")
    
    # Multi-line input
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    text = "\n".join(lines)
    analyze_text(text)

if __name__ == "__main__":
    main()
