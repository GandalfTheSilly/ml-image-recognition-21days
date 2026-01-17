import string
def main():
    
    read_text_file()        
    letters_in_the_file()
    clean_text()
    get_stats()
    top_words()

def read_text_file():
        
        with open("sample.txt", "r") as file:
            file = file.read()
            print("""Your file succesfully read by program!""")
        return file

file = read_text_file()

def letters_in_the_file():
    
    letters = set(file)
    
    cleaned_list = []
    
    for char in letters:
        if char not in string.punctuation:
            cleaned_list.append(char)
    print(f"""
Here's your text with splited into letters and cleaned from punctuations.""", cleaned_list)

def clean_text():
    lwr_file = file.lower()
    
    cleaned_lwr_file = ""
    
    for ch in lwr_file:
        if ch not in string.punctuation:
            cleaned_lwr_file += ch
        
    print(f"""
{cleaned_lwr_file}""")
    return cleaned_lwr_file
cleaned_lwr_file = clean_text()   

def get_stats():
    
    lines = file.splitlines()
    line_cntr = len(lines)
    
    words = file.split()
    word_cntr = len(words)
    
    ch_cntr = 0
    for ch in file:
        ch_cntr += 1  
    
    print(f"""Stats:
There are {line_cntr} lines,
          {word_cntr} words,
          {ch_cntr} letters.""")

def top_words():
    words = file.split()
    
    top_word = max(set(words), key = words.count)
    print(f"The most frequent word in the file is {top_word}")

if __name__ == '__main__':
    main()
