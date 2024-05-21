





# Chatbot Application

This is a simple chatbot application that interacts with OpenAI's GPT-3.5-turbo model to generate responses based on user input. The application is implemented in Python and features a graphical user interface (GUI) built with PyQt6. It also handles rate limit errors gracefully.

## Features

- Interacts with OpenAI's GPT-3.5-turbo model
- Provides a GUI for user interaction using PyQt6
- Handles rate limit errors with a user-friendly message
- Can be easily extended and customized

## Prerequisites

- Python 3.6 or higher
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/chatbot-application.git
   cd chatbot-application







Initialization: The Chatbot class is initialized with the OpenAI API key.
Get Response: The get_response method sends a prompt to the OpenAI API and returns the generated response. It handles rate limit errors by catching RateLimitError exceptions and printing a user-friendly message.
GUI Implementation: The ChatbotGUI class creates a simple GUI using PyQt6 with a text edit for displaying conversation, a line edit for user input, and a button to send messages.
Main Execution: When the script is run, it creates an instance of the ChatbotGUI class, displays the GUI, and starts the event loop.
