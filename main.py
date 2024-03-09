
path_to_file = "books/frankenstein.txt"
with open(path_to_file) as f:
    file_contents = f.read()

def wordCount():
    """
    Counts the number of words in a text file
    Args: 
        None
    Returns:
        int: number or words in file
    """
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    

    return count
    

def letterCount(file_contents):
    """
    Counts the occurrences of each character in the book text (case-insensitive).

    Args:
        book_text (str): The input text from the book.

    Returns:
        dict: A dictionary where keys are lowercase characters and values are their counts.
    """
    char_counts = {}
    lower_case = file_contents.lower()
    for char in lower_case:
        if char.isalpha():
            char_counts[char] = char_counts.get(char,0) + 1

    return char_counts
    # Example usage:
def printReport():

    """
    ta
    Converts dictionary into a list of dictionaries, sorts it and 

    Args:
        book_text (str): The input text from the book.

    Returns:
        dict: A dictionary where keys are lowercase characters and values are their counts.
    
    """
    frankenstein_text = file_contents  # Replace with the actual content of "frankenstein.txt"
    word_count = wordCount()
    letter_counts = letterCount(frankenstein_text)

    # Convert the dictionary to a list of dictionaries
    sorted_letter_counts = [{"character": char, "count": count} for char, count in letter_counts.items()]

    # Sort the list by count (descending order)
    sorted_letter_counts.sort(key=lambda x: x["count"], reverse=True)

    # Print the report
   

    print(f"""{word_count} words found in document
          """)

    print("""Character Occurrences in 'Frankenstein':
          """)

    
    for entry in sorted_letter_counts:
        print(f"{entry['character']}: {entry['count']} times")

  

def main():
    print("""--Beginning of Report---
          """)
    printReport()
    print("""
    --End of Report--""")
    



main()