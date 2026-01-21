from openai import OpenAI


class LocalLLM:
    def __init__(self, model="llama-3.3-70b-versatile"):
        self.client = OpenAI()
        self.model = model
        
    def generate(self, system_prompt, user_prompt):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content
