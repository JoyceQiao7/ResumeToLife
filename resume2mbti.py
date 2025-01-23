from openai import OpenAI
import requests
import base64

def image_2_question(image_path):
    api_key =  "API_KEY"
    # Function to encode the image
    def encode_image(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    # Path to your image
    path = image_path
    # Getting the base64 string
    base64_image = encode_image(path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4o",  # choose your own model
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        # 在此输入问题：
                        "text": "Try to tell this person's MBTI from her resume. First give out the four letter MBTI, and then explain why do you choose those four letters."
                                "Here are some advice on how to make a more accurate estimation:"
                                "1) If personal interest is listed out in the resume, depend at least half of your reasoning on that."
                                "2) Do not reason only from what specific things that person did, but also look into the style of her writing. For example, does she exaggerate a lot or is more down-to-earth."
                                "3) It's ok to use law of large numbers. For example, programmers are usually shy, thus might be introverted (I)."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

# 测试
print(image_2_question("IMAGE_PATH"))