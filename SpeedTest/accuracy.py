def calculate_accuracy(original_text, user_text):
    correct = 0
    original_words = original_text.split()
    user_words = user_text.split()

    for word1, word2 in zip(original_words, user_words):
        if word1 == word2:
            correct += 1

    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)