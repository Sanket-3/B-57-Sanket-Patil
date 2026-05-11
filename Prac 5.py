def chatBot():
    print("============College Chatbot============")
    print("Hell0, Welocome to College Chatbot.")
    print("Type 'exit' to stop")
    
    while True:
    
        user = input("You: ").lower()
        
        if user == "hello":
            print("Bot: Hello Student!")
        
        elif user == "course":
            print("Bot: We offer AI, Computer and IT courses.")
    
        elif user == "fees":
            print("Bot: Fees are 80,000 per year.")
    
        elif user == "admission":
            print("Bot: Admission Process starts in June.")
    
        elif user == "placement":
            print("Bot: College provides placement support.")
         
        elif user == "exit":
            print("Bot: Thank You!!!")
            break
        
        else:
            print("Bot: Sorry, I don't understand")
    
    
chatBot()