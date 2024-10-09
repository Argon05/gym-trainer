def chat_with_trainer():
    print("Hi, I am your personal trainer, how can I help you today?(diet, workout, motivation)")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye', 'thanks', 'thank you', 'okay', 'goodbye']:
            print("Trainer: Thank you for chatting! Have a great day!")
            break
        elif 'workout' in user_input.lower():
            print("Trainer: What type of workout are you interested in? Strength, cardio, or flexibility?")
        elif 'strength' in user_input.lower():
            print("Trainer: Here you go with the  most sutable workout plan for each muscle group--> "
                  "Chest: bench press, push-ups."
                  " Triceps: overhead press, tricep dips. "
                  "Shoulders: lateral raises, front raises."
                  " Back: deadlifts, pull-ups. "
                  "Biceps: bicep curls, hammer curl."
                  " Legs: squats, lunges, leg press. "
                  "Abs: crunches, plank")
        elif 'cardio' in user_input.lower():
            print("Trainer: Here are some cardio exercises--> running, cycling, swimming, biking, walking, jogging.")
        elif 'flexibility' in user_input.lower():
            print("Trainer: Here are some exercises for flexibility--> yoga, pilates, aerobics, stretching.")
        elif 'diet' in user_input.lower():
            print("Trainer: Are you looking for meal plans, nutrition advice, or something specific?")
        elif 'meal plans' in user_input.lower():
            print("Trainer: Here are some meal plans--> Breakfast: Greek yogurt with honey, mixed berries, and a sprinkle of granola."
                  "Snack: A banana with a tablespoon of almond butter."
                  "Lunch: Quinoa salad with cherry tomatoes, cucumber, feta cheese, and a lemon vinaigrette. "
                  "Snack: Carrot sticks with hummus."
                  "Dinner: Grilled chicken breast with steamed broccoli and sweet potato.")
        elif 'nutrition advice' in user_input.lower():
            print("Trainer:Here are some nutrition advice-->"
                  "Stay hydrated."
                  "Control portion sizes."
                  "Include a variety of foods."
                  "Limit added sugars and processed foods.Plan meals and snacks."
                  "Practice mindful eating.Don’t skip meals.""Listen to your body.")
        elif 'motivation' in user_input.lower():
            print("Trainer: Remember, every workout brings you one step closer to your goals! Stay focused!")
        else:
            print("Trainer: I'm here to help! Can you please specify your question or concern?")

if __name__ == "__main__":
    chat_with_trainer()

