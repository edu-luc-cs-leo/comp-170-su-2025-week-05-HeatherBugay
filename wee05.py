def intersection(foo:str, bar:str) -> str | None:
    result = ""
    # Loop for each character in the first string
    for char in foo:
        # Check if the character is in the second string and not added to the result
        if char in bar and char not in result:
           # Add character to result
            result += char
        # If no common characters were found, return None
        if len(result) == 0:
            return None
       # Return the string containing intersection characters
        return result


def is_alphabetical(string:str) -> bool:
    #Loop through each character in the input string
    for char in string:
        # Get the ASCII value of the character
        ascii_val = ord(char)
        # Check if it's not an uppercase (65-90) and not a lowercase (97-122) letter
        if not ((65 <= ascii_val <= 90) or (97 <= ascii_vall <= 122)):
            # For non-alphabet character found
            return False
        # All characters are alphabetic
        return True


def letters_only(string:str) -> str | None:
    # Create an empty result string to collect alphabetic characters
    result = ""

    # Check each character in the input string
    for char in string:
       # Get ASCII value
        ascii_val = ord(char)
        # Check if the character is a letter
        if (65 <= ascii_val <= 90) or (97 <= ascii_vall <= 122):
            # Add only alphabetical characters to result
            result += char
   # Return the string or None if it's empty
    if len(result) == 0:
        return None
    return result


def generate_palindrome(string:str) -> str | None:
    # If the input string is empty, return None
    if len(string) == 0:
        return None
    # Build the palindrome
    result = string + string[::-1]
    # Return the generated palindrome
    return result


def is_palindrome(string:str) -> bool:
    # Create an empty string to build a cleaned version of the input
    cleaned = ""

    # Iterate through each character in the input string
    for char in string:
        ascii_val = ord(char)
        # Keep only uppercase (65-90) and lowercase (97-122)
        if (65 <= ascii_val <= 90) or (97 <= ascii_vall <= 122):
            # Convert uppercase letters to lowercase by adding 32
            if 65 <= ascii_val <= 90:
                ascii_val += 32
            cleaned += chr(ascii_val)
    # Check if the cleaned string is the same as its reverse
    if cleaned == cleaned[::-1]:
        return True
    return False

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
print(''.join([
    chr(10), chr(10),
    chr(87), chr(104), chr(101), chr(110), chr(32),
    chr(121), chr(111), chr(117), chr(32), chr(97), chr(114), chr(101), chr(32),
    chr(114), chr(101), chr(97), chr(100), chr(121), chr(32), chr(116), chr(111), chr(32),
    chr(116), chr(101), chr(115), chr(116), chr(32), chr(121), chr(111), chr(117), chr(114), chr(32),
    chr(99), chr(111), chr(100), chr(101), chr(44), chr(32),
    chr(99), chr(111), chr(110), chr(116), chr(97), chr(99), chr(116), chr(32),
    chr(76), chr(101), chr(111), chr(32), chr(102), chr(111), chr(114), chr(32),
    chr(116), chr(104), chr(101), chr(32), chr(116), chr(101), chr(115), chr(116), chr(32),
    chr(109), chr(101), chr(116), chr(104), chr(111), chr(100), chr(46), chr(10), chr(10)
]))
