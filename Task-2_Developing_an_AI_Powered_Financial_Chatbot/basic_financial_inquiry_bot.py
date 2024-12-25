import pandas as pd

def simple_chatbot(user_query):
    if user_query.lower() == "what is the total revenue?":
        return "The total revenue is [amount]."
    elif user_query.lower() == "how was net income has changed over the last year?":
        return "The net income has increased/decreased by [amount] over the last year."
    elif user_query.lower() == "what is the current cash flow?":
        return "The current cash flow is [amount]."

user_query = input("Please enter your query: ")
response = simple_chatbot(user_query)
print(response)