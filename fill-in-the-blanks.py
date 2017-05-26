# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

easy = '''QUIZ: New __1__ is the biggest city of the USA. __2__ is the capital of Japan. 
__3__ is the capital of South Korea. __4__ is the capital of Canada.'''
medium = '''QUIZ: Jae-in __1__ is the president of South Korea now. Donald __2__ is 
the president of USA. __3__ Obama is the previous 
president of USA, and his wife's first name is __4__.'''
hard = '''QUIZ: An existentialist novel 'Stranger' is written by Albert __1__. This novel is 
famous for its first sentence, 'Mother died today. Or maybe, yesterday; 
I can't be sure', a quote by the main character, __2__. Norwegian Wood is 
a Japanese novel written by Murakami __3__. In this novel, Watanabe longs for a girl 
named __4__, who also longs for her dead lover.'''
answer_easy = ['York', 'Tokyo', 'Seoul', 'Ottawa']
answer_medium = ['Moon', 'Trump', 'Barack', 'Michelle']
answer_hard = ['Camus', 'Meursault', 'Haruki', 'Naoko']

check_list = ["__1__", "__2__", "__3__", "__4__", "NUMBER"]

ques_mode = '''Q: Please select a game difficulty by typing it in!
Possible choices include EASY, MEDIUM, and HARD!!'''
info_difficulty = "INFO: You've chosen " 
ques_num_try = "Q: How many tries do you want to have to win?"
info_num_try = "INFO: You will get NUMBER guess(es) per problem. (The answers are case sensitive)"
info_current_psg = 'INFO: The current passage reads as such:' + '\n' + '____________________________________________________________'
question = "Q: What should be substituted in for NUMBER?"

def get_game(caller):                                       # procedure that takes as input a user's input, 
    if caller == 'easy':                                    # and returns a sentence for the game
        return easy
    if caller == 'medium':
        return medium
    if caller == 'hard':
        return hard      
    else:                                                   # if user's input has a typo, give more tries
        print "INFO: Your input contains a typo. Type it again."   
        return opening()

def get_answer(answer_caller):                              # test paper
    if answer_caller == 'easy':
        return answer_easy
    if answer_caller == 'medium':
        return answer_medium
    if answer_caller == 'hard':
        return answer_hard   

def word_checker(word, check_list):                         # procedure that takes as input each word in sentence, 
    for pos in check_list:                                  # and picks out and returns only the positions for the word to be replaced
        if pos in word:
            return pos
    return None

def get_sent_num_try(sentence, input_number):               # procedure, to return the sentence informing 
    replaced = []                                           # how many tries user will get, taking as input 
    sentence = sentence.split()                             # an user's input number for it
    for word in sentence:
        replacement = word_checker(word, check_list)
        if replacement != None:
            word = word.replace(replacement, input_number)
            replaced.append(word)
        else:
            replaced.append(word)
    else:
        replaced.append(word)
    replaced = ' '.join(replaced)
    return replaced

def get_ques_numbered(sentence, num_to_replace):            # procedure, to return the question asking
    replaced = []                                           # "What should be substituted for NUMBER?"
    sentence = sentence.split()                             # taking as input an user's input and replacing 
    for word in sentence:                                   # NUMBER with it
        replacement = word_checker(word, check_list)
        if replacement != None:
            word = word.replace(replacement, check_list[num_to_replace])
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = ' '.join(replaced)
    return replaced

def get_sentence_filled(sentence, correct_answer, q_num):   # procedure, to return the game sentence filled with
    replaced = []                                           # correct answers
    sentence = sentence.split()
    for word in sentence:
        replacement = word_checker(word, check_list)
        if replacement != None:
            if replacement == check_list[q_num]:
                word = word.replace(replacement, correct_answer)
                replaced.append(word)
            else:
                replaced.append(word)
        else:
            replaced.append(word)
    replaced = ' '.join(replaced)
    return replaced

def play_game(user_input_diffi, game_sentence, how_many_try):   # procedure that takes as input an user's input
    q_num = 0                                                   # selecting game difficulty, original game sentence, 
    num_try = 0                                                 # and a number that user input to select how many tries,
    while q_num < 4:                                            # and prints each process accordingly as to correct or wrong
        user_input_answer = raw_input("\n" + get_ques_numbered(question, q_num) + "\n")
        correct_answer = get_answer(user_input_diffi)[q_num]
        if user_input_answer == correct_answer:
            sentence_filled = get_sentence_filled(game_sentence, correct_answer, q_num)
            print "is a correct answer!" + "\n\n" + info_current_psg + "\n\n" + sentence_filled
            q_num += 1
            game_sentence = sentence_filled
            if q_num == 4:
                return "BUNGA!!! YOU'VE COMPLETED YOUR QUIZ!"
        else:
            num_try += 1
            num_try_left = int(how_many_try) - num_try             
            print "INFO: Not quite! Try again. You have " + str(num_try_left) + " guess(es) left."
            if num_try == int(how_many_try):
                print "\n" + "GAME OVER."
                user_input = raw_input("\n" + "Q: Do you want to try again? Type yes or no" + "\n")    
                if user_input == "yes":                                       
                    return opening()
                else:
                    return "Bye~"
    
def opening():                                                          # procedure, for user to select a game mode
    user_input_diffi = raw_input("\n" + ques_mode + "\n").lower()       # and how many tries user would take, which
    user_input_how_many_try = raw_input("\n" + ques_num_try + "\n")     # prints opening, then returns 'play_game' procedure 
    game_sentence = get_game(user_input_diffi)
    sent_num_try = get_sent_num_try(info_num_try, user_input_how_many_try)
    opening = info_difficulty + user_input_diffi + "\n\n" + sent_num_try + "\n\n" + info_current_psg + "\n\n" + game_sentence + "\n"
    print opening
    return play_game(user_input_diffi, game_sentence, user_input_how_many_try)

print opening()