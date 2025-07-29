from openai import OpenAI
import base64

def analyze_with_openai(image_bytes: bytes, prompt: str, api_key: str, temperature: float) -> str:
    client = OpenAI(api_key=api_key)

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI error: {str(e)}"