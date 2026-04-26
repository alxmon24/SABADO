from openai import OpenAI


class OpenAIService:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def responder(self, mensaje: str, contexto: list[dict[str, str]] | None = None) -> str:
        messages = [
            {
                "role": "system",
                "content": "Eres Sabado, un asistente útil, claro y directo.",
            }
        ]

        if contexto:
            messages.extend(contexto)

        messages.append({"role": "user", "content": mensaje})

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
        )

        return completion.choices[0].message.content or ""
