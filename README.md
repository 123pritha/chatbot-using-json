<p>
  # JSON-Based Chatbot

This project is a simple chatbot implementation in Python, using a JSON file to store questions and responses. The chatbot reads the user's input, looks for matching questions in the JSON file, and provides an appropriate response. If it doesn't understand the input, it returns a default fallback message.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)

## Features

- Reads and parses a JSON file containing predefined questions and responses.
- Basic pattern matching for user inputs.
- Interactive user input via command line.
- Fallback response if input is not understood.
- Easy-to-customize responses stored in a JSON file.

## Technologies Used

- **Python 3.x**
- **JSON (JavaScript Object Notation)** for storing chatbot responses.

## Project Structure

### chatbot_data.json

The chatbot's responses are stored in the `chatbot_data.json` file. This file contains a list of questions and their corresponding responses.

```json
{
  "conversations": [
    {
      "question": "hello",
      "response": "Hi! How can I help you today?"
    },
    {
      "question": "what is your name",
      "response": "I'm your friendly chatbot!"
    },
    {
      "question": "bye",
      "response": "Goodbye! Have a great day!"
    }
  ]
}



</p>
