### CHATBOT with Gemini

This repository contains a chatbot implemented using the Gemini AI model from Google's generative AI library. The chatbot is designed to interact with users and provide responses based on the input provided.

## Features
- Utilizes the Gemini AI model for generating responses.
- Supports conversation history to maintain context.
- Configurable response generation using temperature settings.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/al3x-X-y/CHATBOT-with-Gemini.git
   cd CHATBOT-with-Gemini
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add your API key to the `.env` file:
     ```
     API_KEY=your_api_key_here
     ```

## Usage

1. Run the chatbot:
   ```sh
   python main.py
   ```

2. Interact with the chatbot in the terminal. Type your messages, and the chatbot will respond. Type 'exit' to quit the conversation.

## Project Structure

- `main.py`: Entry point for running the chatbot.
- `ChatBot.py`: Contains the `ChatBot` class and related functionality.
- `requirements.txt`: Lists the dependencies required for the project.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes. Make sure to follow the existing coding style and include tests for new features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to modify this README file to better suit your project's specific needs.