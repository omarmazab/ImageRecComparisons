import google.genai as genai
import google.genai.types as types
from PIL import Image
from io import BytesIO

def analyze_with_gemini(image_bytes: bytes, prompt: str, api_key: str, temperature: float) -> str:
    try:
        client = genai.Client(api_key=api_key)

        image = Image.open(BytesIO(image_bytes))


        config = types.GenerateContentConfig(
            temperature=temperature,
          #  top_k=top_k,
          #  top_p=top_p,
          #  max_output_tokens=max_output_tokens,

        )

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            config=config,
            contents=[prompt, image]
        )

        return response.text
    except Exception as e:
        return f"Gemini error: {str(e)}"