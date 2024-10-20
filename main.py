import random 

# You can initialize important data at the top of the program

# Initalize a list called Trivia
trivia = [
    # Q1
      { 
       'question': "What is Bowie's Favorite food?",
       'answer': 'pizza crust',
       'options': ['chicken', 'kibble', 'pizza crust','rabbit']
      },
    # Q2
      { 
       'question': "What adjective best describes Bowie?",
       'answer': 'devious',
       'options': ['ugly', 'devious', 'mellow', 'cute']
      },
    # Q3
      { 
       'question': "What is Bowie's Favorite toy?",
       'answer': 'white ball',
       'options': ['white ball', 'bunny ball', 'pig ball', 'tire']
      },
     # Q4
      { 
       'question': '👶How old is Bowie👴',
       'answer': '3 years old',
       'options': ['2 months old', '4 years old', '3 years old','5 years old']
      },
    # Q5
      { 
       'question': '🥰Does Bowie love Lucian?🥰',
       'answer': 'he better',
       'options': ['not enough', 'he better', 'yes', 'no']
      },
    # Q6
      { 
       'question': '👨‍🍼💆‍♂️Where does Bowie like to be pet?💆‍♂️👨‍🍼',
       'answer': 'side of face',
       'options': ['his tummy','side of face', 'his legs', 'his back']
      },
    # Q7
      { 
       'question': "🤬Who is Bowie's opp?🤬",
       'answer': 'bear🐕',
       'options': ['bear', 'the door man', 'lordy', 'yellow dog']
      },
    # Q8
      { 
       'question': '🏊🏼‍♂️How does Bowie feel about swimming?🏊🏼‍♂️',
       'answer': 'water is hell',
       'options': ['Its his fav', 'He tolerates it', 'He rather not', 'water is hell']
      },
    # Q9
      { 
       'question': "🥰Who is Bowie's favorite🥰",
       'answer': "Lucian's dad",
       'options': ["Lucian's sister","Lucian's mom", "Lucian", "Lucian's dad"]
      },
    # Q10
      { 
       'question': "What is Bowie's flaw?",
       'answer': "He thinks he is alpha",
       'options': ["he farts a lot", "he's stubborn", "he thinks he is alpha", "he stinks"]
      }  
]

# Dispaly the question and possible options
# Function takes question (String), answer (String), options (list)
# function returns a boolean
def ask_question(question, answer, options):
  # 1. Print out a question from the Trivia list
  print(question)
  
  # 2. Print out the options (list)
  random.shuffle(options)
  for option in options:
    print(f"🤔 {option}")
  
  # 3. get user input
  choice = input("Enter answer: ")
  
  # 4. Check if choice matches correct answer
  if choice.lower() == answer.lower(): # .lower() turns all characters lowercase 
    return True
  return False # if it passes the if check then it will ignore the return false line

  # 5. Print a "That wasn't an option" if choice does not == one of the choices
   
# MAIN METHOD for the Game Loop
def main():
    print("Let's Play 🐩🐶 Bowie 🐶🐩 Trivia!")
    print("🐶🤨🐶🤔🐶🥺🐶🤨🐶🤔🐶🥺🐶🤨🐶🤔🐶🥺🐶🤨🐶🤔🐶🥺🐶")

    # Initialize the score
    score = 0
    
    # Trivia is a list 
    for num in range(len(trivia)):
      current = (trivia[num]) # dictionary
      # Get data from that item
      q = current['question']
      a = current['answer'] 
      opts = current['options']
      # Pass in q, a, and options into ask_question
      is_correct = ask_question(q, a, opts)
      print(".......")
      if is_correct: 
        print("🤩🥰😁😆😃🤗  You are CORRECT! 🤩🥰😁😆😃🤗")
      else: 
        print("😖😢😠🥹  You are WRONG 😖😢😠🥹")
      # Update score accordingly 
      if is_correct == True:
        score+=1
      # DisplayScpixore
      print(f"Current Score: {score}")
      print()

if __name__ == "__main__":
    main()
   