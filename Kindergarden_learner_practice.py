import random
import os

learner_fname = None


def get_learner_name():
  global learner_fname
  while True:
    fname = input("Enter your first name: \n")
    if fname.strip():
      learner_fname = Learner(fname)
      return fname, learner_fname
    else:
      print("please enter a valid name.")


def Learner_Menu():
  name, profile = get_learner_name()

  print("\nWelcome to the Kindergarten Learning Program!\n")

  while True:
    print("\nSelect an option to start practicing:\n")

    print("1. Practice Math")
    print("2. Practice Sight words")
    print("3. View Profile")
    print("4. Exit\n")

    learner_select = input("Select and option to start practising (1-4): \n")

    try:
      if learner_select == "1":
        score = math_practice()
        print(
            "\nEnd of practise Test! You can now check your Mastery profile.\n"
        )

        profile.update_math_mastery(score)

      elif learner_select == "2":
        score = test_word()

        print(
            "\nEnd of practise Test! You can now check your Mastery profile.\n"
        )

        profile.update_mastery_score(score)

      elif learner_select == "3":

        profile.learner_profile()

      elif learner_select == "4":
        print("Exiting the program. Goodbye!")
        break
      else:
        print("Invalid learner_select. Please enter a number between 1 and 4.")

    except KeyboardInterrupt:
      print("\nExiting the program. Goodbye!")
      break


def test_word():
  print("\nLET'S PRACTICE SIGHT WORDS!\n")

  score_count = 0

  term_sight_words = {
      "the", "bad", "sad", "me", "my", "to", "bird", "we", "he", "in", "am",
      "sun", "can", "go", "you", "get", "like", "love", "with", "do", "look",
      "likes", "little", "come", "was", "play", "some", "on", "are", "see",
      "Yes", "this", "Her", "down", "robot", "him", "big", "our", "Saw",
      "will", "say", "happy", "sad", "mad", "rat", "bat", "an", "let", "met",
      "men", "home", "man", "our", "she", "son", "mat", "no", "up", "got",
      "may", "us", "it", "is", "by", "comb", "run",
  }

  for i in range(1, 11):
    current_word = random.choice(list(term_sight_words))
    pattern = random.choice(range(len(current_word)))

    while True:
      learner_input = input(
          f"\nQuestion {i}: Type the missing letter : "
          f"{current_word[:pattern]}_{current_word[pattern + 1:]}: ")

      if learner_input.strip() == "":
        print("Please enter a valid input.")
      elif len(learner_input) == 1 and learner_input.isalpha():
        break
      else:
        print("Invalid input. Please enter a single letter.")

    try:
      entered_letter = learner_input.lower()
      current_word_reconstructed = current_word[:
                                                pattern] + entered_letter + current_word[
                                                    pattern + 1:]

      if (entered_letter == current_word[pattern].lower()
          or current_word_reconstructed.lower() == current_word
          or current_word_reconstructed.lower() in term_sight_words):
        print(
            f"Correct! Well done. The word is '{current_word_reconstructed}' 😊"
        )
        score_count += 1

      else:
        print(
            f"Incorrect! The possible letter in the pattern is '{current_word[pattern].lower()}'. "
            f"The full word is {current_word}.")
    except ValueError as err:
      print(str(err))

  return score_count


def math_practice():
  print("\nLET'S PRACTICE MATH!!!\n")
  score_count = 0

  for i in range(1, 11):
    first_num = random.randint(0, 100)
    sec_num = random.randint(0, 100)

    Math_prac_type = ["bigger_num", "next_number"]
    learner_select = random.choice(Math_prac_type)

    learner_input = None
    correct = None

    try:
      if learner_select == "bigger_num":
        print(
            f"\nQuestion {i}:  which is the bigger number: { first_num} or { sec_num}?\n"
        )
        while True:
          learner_input = input(
              "Type '1' for the first number, '2' for the second: \n")
          if learner_input in ['1', '2']:
            break
          print("Invalid input. Please enter '1' or '2'.")

        correct = (first_num > sec_num
                   and learner_input == '1') or (first_num < sec_num
                                                 and learner_input == '2')

      elif learner_select == "next_number":
        next_number = sec_num + 1
        print(f"\nQuestion {i}: Which number comes after { sec_num}?")

        while True:
          learner_input = input("\nEnter the next number: ")
          if learner_input.isdigit():
            break

          print("\nInvalid input. Please enter a valid number.")

        correct = int(learner_input) == next_number

      if correct:
        print("\nCorrect! Good job.")
        score_count += 1
      else:
        print("\nThat's not correct.")
        correct_answer = sec_num + 1 if learner_select == "next_number" else max(
            first_num, sec_num)
        print(f"\nThe correct answer is {correct_answer}.")

    except ValueError as e:
      print(str(e) + "\n")

  return score_count


class Learner:

  def __init__(self, first_name):

    self.first_name = first_name
    self.math_level = 0
    self.word_level = 0

  def update_math_mastery(self, score_count):
    self.math_level += (score_count / 10) * 100
    if self.math_level > 100:
      self.math_level = 100

  def update_mastery_score(self, score_count):
    self.word_level += (score_count / 10) * 100
    if self.word_level > 100:
      self.word_level = 100

  def learner_profile(self):

    print(f"Learner mastery profile for {self.first_name} ")

    print(f"\nMath Mastery Level: {round(self.math_level, 2)}%")
    print(f"\nWords Mastery Level: {round(self.word_level, 2)}%")


Learner_Menu()
