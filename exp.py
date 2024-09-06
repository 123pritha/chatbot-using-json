import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def ask_question(question):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=question + "\nAI:",
      max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the Product FAQ Chatbot!")
    print("You can ask any question about our product. Enter 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        answer = ask_question(user_input)
        print("AI:", answer)

if __name__ == "__main__":
    main()
