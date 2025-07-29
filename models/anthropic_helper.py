import anthropic
import base64

def analyze_with_anthropic(
    image_bytes: bytes,
    prompt: str,
    api_key: str,
    temperature: float,
) -> str:
    client = anthropic.Anthropic(api_key=api_key)

    try:
        # Encode image as base64
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        response = client.messages.create(
            model="claude-3-5-haiku-latest",
            temperature=temperature,
            max_tokens=2048,  # You can make this configurable if you want
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": base64_image,
                            },
                        },
                    ],
                }
            ],
        )

        # Extract the response text safely
        if response.content and hasattr(response.content[0], "text"):
            return response.content[0].text
        else:
            return "No response text found."

    except Exception as e:
        return f"Anthropic error: {str(e)}"