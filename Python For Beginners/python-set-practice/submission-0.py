from typing import List

def contains_duplicate(words: List[str]) -> bool:
    list_with_no_duplicates = set(words)
    if len(words) == len(list_with_no_duplicates):
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
