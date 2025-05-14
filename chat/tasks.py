import openai
from celery import shared_task
from ai_support_chat.settings import OPEN_AI_TOKEN

openai.api_key = OPEN_AI_TOKEN

@shared_task
def generate_ai_response_task(message):
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo", 
            prompt=message,  
            max_tokens=200,  
            temperature=0.7
        )
        ai_answer = response['choices'][0]['text'].strip() 
        return ai_answer
    except Exception as e:
        return f'AI error: {str(e)}'