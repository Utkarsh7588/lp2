# Define the chatbot's knowledge base for customer support
knowledge_base = {
    "hello": "Hello! How can I assist you today?",
    "order status": "To check your order status, please provide your order number.",
    "payment issue": "I'm sorry to hear that you're facing payment issues. Please contact our support team at support@example.com for assistance.",
    "product information": "Our products are known for their high quality and durability. Is there any specific product you would like to know about?",
    "default": "I apologize, but I am unable to assist with your request. Please contact our support team for further assistance."
}


def customer_support_chatbot():
    while True:
 
        user_input = input("User: ")
        response=False

        for v in knowledge_base:
            if v in user_input.lower() :
          
                print("ChatBot:", knowledge_base[v])
                response=True
        if not response:
            print("ChatBot:",knowledge_base["default"])        
            


customer_support_chatbot()
