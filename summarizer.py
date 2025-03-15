import os
from groq import Groq
from langchain.prompts import PromptTemplate

class Summarizer:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_summary(self, text, summary_type):
        if summary_type == "brief":
            prompt = "Summarize this in 1-2 sentences: {text}"
        elif summary_type == "detailed":
            prompt = "Summarize this in a paragraph: {text}"
        else:
            raise ValueError("Invalid summary type. Choose 'brief' or 'detailed'.")

        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt.format(text=text)},
            ],
            model="mixtral-8x7b-32768",  # Use Mixtral or Llama 2
            temperature=0.5,
        )
        return response.choices[0].message.content

    def brief_summary(self, text):
        return self.generate_summary(text, "brief")

    def detailed_summary(self, text):
        return self.generate_summary(text, "detailed")