import requests

def send_prompt(prompt):
    response = requests.post('http://127.0.0.1:5000/llm', json={'prompt': prompt})
    return response.json()

while True:
    user_input = input("Enter your prompt (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    response = send_prompt(user_input)
    print(response)

print("Goodbye!")

