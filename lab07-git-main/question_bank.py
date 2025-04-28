#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What planet is known as the Red Planet?", "Mars"),
        ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
        ("What part of the cell contains DNA?", "Nucleus"),
        ("What force keeps us on the ground?", "Gravity"),
        ("How many legs does an insect have?", "Six"),
        ("What is the boiling point of water (in Celsius)?", "100"),
        ("What is the center of an atom called?", "Nucleus"),
        ("What organ pumps blood through the body?", "Heart"),
        ("Which planet is the largest in our solar system?", "Jupiter")
    ],
    "Math": [
        ("What is 7 + 8?", "15"),
        ("What is the square root of 81?", "9"),
        ("What is 12 x 12?", "144"),
        ("What is 45 divided by 5?", "9"),
        ("What is the value of pi rounded to two decimal places?", "3.14"),
        ("What is 100 minus 47?", "53"),
        ("Solve for x: 2x = 10", "5"),
        ("What is the next prime number after 7?", "11"),
        ("What is 10% of 200?", "20"),
        ("What is 5 cubed (5³)?", "125")
    ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In which year did World War II end?", "1945"),
        ("What ancient civilization built the pyramids?", "Egyptians"),
        ("Who discovered America?", "Christopher Columbus"),
        ("Who was known as the Maid of Orléans?", "Joan of Arc"),
        ("In which year did Pakistan gain independence?", "1947"),
        ("Who was the famous queen of ancient Egypt?", "Cleopatra"),
        ("What wall divided East and West Berlin?", "Berlin Wall"),
        ("Who wrote the Declaration of Independence?", "Thomas Jefferson"),
        ("What empire was ruled by Julius Caesar?", "Roman Empire")
    ]
}

hints = {
    "Science": [
        "It’s made of hydrogen and oxygen.",
        "It's the fourth planet from the Sun.",
        "It's the gas humans exhale.",
        "It’s often called the brain of the cell.",
        "It pulls objects towards the Earth.",
        "Think about ants and bees.",
        "It’s a three-digit number, very hot!",
        "It shares a name with the part of a cell that holds DNA.",
        "It beats about 100,000 times a day.",
        "It’s a gas giant, very big!"
    ],
    "Math": [
        "Think simple addition.",
        "What number times itself equals 81?",
        "A famous multiplication table value.",
        "How many times does 5 fit into 45?",
        "Commonly approximated as 3.14.",
        "Subtract carefully!",
        "Divide both sides by 2.",
        "Prime numbers are only divisible by 1 and themselves.",
        "10 percent means divide by 10.",
        "5 × 5 × 5."
    ],
    "History": [
        "He appears on the U.S. $1 bill.",
        "It ended after atomic bombs were dropped.",
        "They are famous for building huge stone structures.",
        "He sailed the ocean blue in 1492.",
        "A young heroine from France.",
        "It was after the partition of British India.",
        "A female ruler associated with Egypt.",
        "It symbolized the Cold War divide.",
        "He later became the third U.S. President.",
        "An ancient Roman general and dictator."
    ]
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    if category in questions and questions[category]:
        return random.choice(questions[category])
    else:
        return None, None
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer == correct_answer:
        return True
    else:
        return False

    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        new_list = []
        for q, a in questions[category]:
            if q != question:
                new_list.append((q, a))
        questions[category] = new_list
    else:
        return None
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    answer= (input(question))
    return answer
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    hints = {
        "math": "Remember to apply the correct formula.",
        "science": "Think about the scientific method.",
        "history": "Consider the major events of that time.",
        "geography": "Focus on the location and its features."
    }
    return hints.get(category(), "Think carefully about your answer!")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print(f"The correct answer is: {correct_answer}")
    #------------------------

#---------------------------------------




