from openai import OpenAI


class OpenAIService:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def responder(self, mensaje: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Eres Sabado, un asistente útil, claro y directo.",
                },
                {"role": "user", "content": mensaje},
            ],
            temperature=0.7,
        )

        return completion.choices[0].message.content or ""
