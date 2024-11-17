import base64
from openai import OpenAI
from utils.prompt_loader import load_prompt

class VisionService:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    def analyze_image(self, image_base64):
        """Analyze a single image with OpenAI Vision API"""
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": load_prompt("system_prompt")
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": load_prompt("user_prompt")},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_base64}",
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=4096,
            temperature=0.5
        )
        return response.choices[0].message.content
    
    def process_camera_input(self, camera_input):
        """Process camera input and return analysis"""
        image_bytes = camera_input.getvalue()
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        return self.analyze_image(base64_image)
