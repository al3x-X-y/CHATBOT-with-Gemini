import google.generativeai as genai


class GenAIEkception(Exception):
    "genai"


class ChatBot:
    CHATBOT_NAME = "My Gen AI"

    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key=api_key)
        self.model = self.genai.GenerativeModel("gemini-pro")
        self.conversation = None
        self._conversation_history = []
        self.preload_conversation()

    def send_promt(self, promt, temperature=0.1):
        if temperature < 0 or temperature > 1:
            raise GenAIEkception("Temperature must be between 0 and 1")
        if not promt:
            raise GenAIEkception("Promt cannot be empty")
        try:
            response = (
                self.conversation.send_message(
                    content=promt,
                    genaration_config=self._genaration_config(temperature),
                ),
            )
            response.resolve()
            return f'{{"text": "{response.text}"}}'
        except Exception as e:
            raise GenAIEkception(f"Error: {e}")

    @property
    def history(self):
        conversation_history = [
            {"role": message.role, "text": message.text}
            for message in self.conversation.history
        ]
        return conversation_history

    def clear_conversation(self):
        self.conversation = self.model.start_chat(history=[])

    def start_conversation(self):
        self.conversation = self.model.start_chat(history=self._conversation_history)

    def _genaration_config(self, temperature):
        return genai.types.GenerationConfig(self.conversation, temperature=temperature)

    def construct_message(self, text, role="role"):
        return {"role": role, "parts": [text]}

    def preload_conversation(self, conversation_history=None):
        if isinstance(conversation_history, list):
            self._conversation_history = conversation_history
        else:
            self._conversation_history = [
                self.construct_message(
                    'From now on, return the output as a JSON object that can be loaded in python with the key as \'text\'. For example, {"text" : "<output goes here>"}'
                ),
                self.construct_message(
                    'Sure, I can return the output as a regular JSON object with the key as "text". Here is an example: {"text" : "Your Output"}',
                    "model",
                ),
            ]
