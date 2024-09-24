# You can initialize important data at the top of the program

# Initalize a list called Trivia
trivia = [
    # Q1
      { 
       'question': "What is Bowie's Favorite food?",
       'answer': 'pizza crust',
       'options': ['chicken', 'kible', 'pizza crust','rabbit']
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
       'answer': 'the side of his face',
       'options': ['his tummy',' the side of his face', 'his legs', 'his back']
      },
    # Q7
      { 
       'question': "🤬Who is Bowie's opp?🤬",
       'answer': 'bear🐕',
       'options': ['bear🐕', 'the door man🧍‍♂️', 'lordy🐕', 'yellow dog🐕']
      },
    # Q8
      { 
       'question': '🏊🏼‍♂️How does Bowie feel about swimming?🏊🏼‍♂️',
       'answer': 'It is the scariest thing in the world and any body of water is the gates of hell',
       'options': ['Its his favorite thing in the world', 'He tolerates it, but needs to be given spa treatment after', 'He rather not swim', 'It is the scariest thing in the world and any body of water is the gates of hell']
      },
    # Q9
      { 
       'question': "🥰Who is Bowie's favorite🥰",
       'answer': "probably Lucian's dad",
       'options': ["probably Lucian's sister","probably Lucian's mom", "probably lucian", "probably Lucian's dad"]
      },
    # Q10
      { 
       'question': "What is Bowie's flaw?",
       'answer': "He thinks he is alpha",
       'options': ["he farts a lot", "he's stubborn", "He thinks he is alpha", "he insits on peeing in the home"]
      }  
]

# Dispaly the question and possible options
# Function takes question (String), answer (String), options (list)
# function returns a boolean

def ask_question(question, answer, options):
  # 1. Print out a question from the Trivia list
  print(question)
  
  # 2. Print out the options (list)
  for option in options:
    print(f"🐶{option}")
  
  # 3. get user input
  choice = input("Enter answer: ")
  
  # 4. Check if choice matches correct answer

  
  
# Main Method for the game loop
def main():
    print("Let's Play 🐩🐶 Bowie 🐶🐩 Trivia!")
    # Initialize the score
    score = 0
    
    # Starting with just ONE trivia item, loop laster
    current = (trivia[0]) # prints the first dictionary
    # Get data from that item
    q = current['question'] # Prints the question (value of the first key)
    a = current['answer'] 
    opts = current['options']
    # Pass in q, a, and options into ask_question
    is_correct = ask_question(q, a, opts)
    
    
    # Update score accordingly 


if __name__ == "__main__":
    main()
   