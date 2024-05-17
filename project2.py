import time
def typing_speed_test():
    sample_text = (
        "The quick brown fox jumps over the lazy dog. This is a sample sentence to test your typing speed."
    )

    print("Type the following text and press Enter when done:")
    print(sample_text)
    print()

    input("Press Enter to start...")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    word_count = len(sample_text.split())
    user_word_count = len(user_input.split())

    correct_words = 0
    for i, word in enumerate(user_input.split()):
        if i < len(sample_text.split()) and word == sample_text.split()[i]:
            correct_words += 1

    accuracy = (correct_words / word_count) * 100
    wpm = user_word_count / time_taken_minutes

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
