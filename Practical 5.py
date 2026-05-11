def chatbot():
    print("🤖 Chatbot: Hello! Welcome to Customer Support.")
    print("Type 'bye' to exit.\n")
    
    while True:
        user = input("You: ").lower()
        
        # Greeting
        if user in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")
        
        # Product Inquiry
        elif "product" in user:
            print("🤖 Chatbot: We offer laptops, mobiles, and accessories.")
        
        # Price Inquiry
        elif "price" in user:
            print("🤖 Chatbot: Prices start from ₹10,000. Please specify product.")
        
        # Order Status
        elif "order" in user:
            print("🤖 Chatbot: Please provide your order ID.")
        
        # Help
        elif "help" in user:
            print("🤖 Chatbot: You can ask about products, prices, or order status.")
        
        # Exit
        elif user == "bye":
            print("🤖 Chatbot: Thank you! Have a great day 😊")
            break
        
        # Default Response
        else:
            print("🤖 Chatbot: Sorry, I didn’t understand. Can you rephrase?")

# Run chatbot
chatbot()