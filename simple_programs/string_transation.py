def transformSentence(sentence):
    """
    This function transforms a given sentence according to the specified algorithm.

    Parameters:
    sentence (str): The input sentence to be transformed.

    Returns:
    str: The transformed sentence.
    """

    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty list to store the transformed words
    transformed_words = []

    # Iterate over each word in the sentence
    for word in words:
        # Initialize an empty string to store the transformed word
        transformed_word = ""

        # Add the first character of the word to the transformed word
        transformed_word += word[0]

        # Iterate over the rest of the characters in the word
        for i in range(1, len(word)):
            # Get the current character and the previous character
            current_char = word[i]
            previous_char = word[i - 1]

            # Check if the previous character comes before the current character in the alphabet
            if previous_char.lower() < current_char.lower():
                # If so, convert the current character to uppercase
                transformed_word += current_char.upper()
            # Check if the current character comes before the previous character in the alphabet
            elif previous_char.lower() > current_char.lower():
                # If so, convert the current character to lowercase
                transformed_word += current_char.lower()
            else:
                # If the characters are the same, keep the current character as it is
                transformed_word += current_char

        # Add the transformed word to the list of transformed words
        transformed_words.append(transformed_word)

    # Join the transformed words back into a sentence and return it
    return " ".join(transformed_words)


if __name__ == '__main__':


    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')
