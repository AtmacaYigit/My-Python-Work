import random

max_attempts = 3
words = ["MÜHENDiS", "OLAĞANÜSTÜ", "KUYRUKLU' 'YILDIZ", "VATANDAŞ", "ASTRONOT", "TELEVİZYON", "YEMEK' 'TARİFİ", "PROGRAMLAMA", "GÜNEŞ SİSTEMİ", "ALTIN ORAN"]
leaderboard = {}


while True:
    name = input("Enter your name (q to quit): ")

    if name == "q":
        break

    chosen_word = random.choice(words).lower()
    remaining_attempts = max_attempts
    current_word = "*" * len(chosen_word)
    print(f"Chosen Word: {current_word}")

    attempts = 0
    while remaining_attempts > 0:
        attempts += 1
        guess = input("Enter a letter or word: ").lower()

        if guess == chosen_word:
            print(f"Congratulations, you found the correct word! ({chosen_word})")
            if attempts == 1:
                print(f"You found the word in {attempts} try!")
            else:
                print(f"You found the word in {attempts} tries!")

            current_word = chosen_word

            if name in leaderboard:
                leaderboard[name].append(attempts)
            else:
                leaderboard[name] = [attempts]
            break

        elif len(guess) == 1 and guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    current_word = current_word[:i] + chosen_word[i] + current_word[i+1:]

            print(f"Congratulations, you found a correct letter! ({current_word})")

        else:
            remaining_attempts -= 1
            if remaining_attempts > 0:
                print(f"You entered the wrong letter or word. {remaining_attempts} remaining attempts. ({current_word})")
            else:
                print(f"You lost. The correct word was '{chosen_word}'.")

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: min(x[1])) #Here it is defined how to rank the leaderboard

    print("LEADERBOARD:")
    for i in range(len(sorted_leaderboard)):
        name, attempts = sorted_leaderboard[i]
        min_attempts = min(attempts)
        print(f"{i+1}. {name}: found in {min_attempts} attempts") 

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        break
