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

easy = '''    New __1__ is the biggest city of the USA. __2__ is the capital of Japan. 
    __3__ is the capital of South Korea. __4__ is the capital of Canada.'''
medium = '''    Jae-in __1__ is the president of South Korea now. Donald __2__ is 
    the president of USA. __3__ Obama is the previous 
    president of USA, and his wife's first name is __4__.'''
hard = '''    An existentialist novel 'Stranger' is written by Albert __1__. This novel is 
    famous for its first sentence, 'Mother died today. Or maybe, yesterday; 
    I can't be sure', a quote by the main character, __2__. Norwegian Wood is 
    a Japanese novel written by Murakami __3__. In this novel, Watanabe longs for a girl 
    named __4__, who also longs for her dead lover.'''
answer_easy = ['York', 'Tokyo', 'Seoul', 'Ottawa']
answer_medium = ['Moon', 'Trump', 'Barack', 'Michelle']
answer_hard = ['Camus', 'Meursault', 'Haruki', 'Naoko']

ques_mode = '''Q: Please select a game difficulty by typing it in!
Possible choices include EASY, MEDIUM, and HARD!!'''
info_diffi = "!!"+"-"*10 + "INFO" +"-"*10+"!!" + "\n" + "INFO: You've chosen " 
ques_num_try = "Q: How many tries do you want to have to win?"
info_crt_psg = 'INFO: The current passage reads as such:' + '\n' + ' '*4 +'_' * 10 + "QUIZ" + '_' * 10
ques_try_again = "Q: Do you want to try again? Type yes or no"

def get_game(caller):
    """take as input a user's input, and return a quiz sentence for the selected difficulty."""     

    if caller == 'easy':                                    
        return easy
    if caller == 'medium':
        return medium
    if caller == 'hard':
        return hard      
    else: # if user's input has a typo, give more tries
        print "INFO: Your input contains a typo. Type it again."   
        return opening()

def get_answer_list(answer_caller):                              
    """take as input a user's input, and return the corresponding answer list"""

    if answer_caller == 'easy':
        return answer_easy
    if answer_caller == 'medium':
        return answer_medium
    if answer_caller == 'hard':
        return answer_hard   

def get_num_try(u_input_num_try):
    """
    take as input user's input for a question asking how many guesses user would take.
    unless user typed '0' or none, return the number, or
    guide user to type an appropriate number(numbers above 0).
    """

    if u_input_num_try == '0': 
        print "Please select a number above 0. let's try again from the start."
        return opening()
    elif u_input_num_try != '': 
        return u_input_num_try
    else:
        print ques_num_try + "Please select a number. let's try again from the start."
        return opening()

def game_over():
    """
    announce a game-over and ask user for another try.
    if user would try again, return opening(), or if not, announce good-bye. 
    """

    print "\n" + "GAME OVER. Nice try~"
    u_input_try_again = raw_input("\n" + ques_try_again + "\n")
    if u_input_try_again  == "yes":                                       
        return opening()
    elif u_input_try_again == "no":
        return "Thank you for playing. Bye~"
    else:
        print "Type yes or no."
        return game_over()   

def replacement(index):
    return "__" + str(index + 1) + "__"

def play_game(answer_list, game_stc, n_tries): 
    """
    1. Loop over answers in the corresponding answer list, and ask for input by prompting the corresponding blank number
    2. If the input is correct, prompt for next answer 
    3. otherwise ask for input again until the user uses up times for guess
    4. When all blanks are filled or user uses up guesses, process extra functions to exit the game.
    """

    for i in range(len(answer_list)):  
        u_input_answer = raw_input("\n" + "Q: What should be substituted in for " + replacement(i) + "?\n")
        num_try = 1    
        while u_input_answer != answer_list[i]:
            if int(n_tries) - num_try <= 0:
                return game_over()   
            print "Not quite! Try again. You have " + str(int(n_tries) - num_try) + " guess(es) left"
            u_input_try_again = raw_input("\n" + "Q: What should be substituted in for " + replacement(i) + "?\n") 
            if u_input_try_again == answer_list[i]:
                u_input_answer = u_input_try_again
                break                
            num_try += 1
        if u_input_answer == answer_list[i]:
            game_stc = game_stc.replace(replacement(i), answer_list[i])
            print "^"*10 + " is CORRECT!" + "-"*15 + "\n\n" + info_crt_psg + "\n\n" + game_stc
            if i == len(answer_list)-1:
                return "\nBUNGA!!! YOU'VE COMPLETED YOUR QUIZ!"

def opening():           
    """
    let user to select a game mode and how many tries user would take, 
    which prints opening, then returns 'play_game' procedure.
    """                                          

    u_input_diffi = raw_input("\n" + ques_mode + "\n").lower()       
    u_input_num_try = raw_input("\n" + ques_num_try + "\n")    
    game_stc = get_game(u_input_diffi)
    num_tries = get_num_try(u_input_num_try)
    answer_list = get_answer_list(u_input_diffi)
    stc_num_try = "INFO: You will get " + num_tries + " guess(es) per problem.\n      (The answers are case sensitive)"
    opening = info_diffi + u_input_diffi + "\n\n" + stc_num_try + "\n\n" + info_crt_psg + "\n\n" + game_stc + "\n"
    print opening
    return play_game(answer_list, game_stc, num_tries)

print opening()