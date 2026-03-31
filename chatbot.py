def chatbot():
    print("Welcome to Admission Chatbot!")
    
    while True:
        user = input("You: ").lower()
        
        if "admission" in user:
            print("Bot: Admission starts from June.")
        
        elif "fees" in user:
            print("Bot: Fees is around 50,000 per year.")
        
        elif "course" in user:
            print("Bot: We offer B.Tech, MBA, and B.Sc.")
        
        elif "exit" in user:
            print("Bot: Thank you!")
            break
        
        else:
            print("Bot: Sorry, I didn't understand.")

chatbot()
