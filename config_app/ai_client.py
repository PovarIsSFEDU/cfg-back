import requests
import json
import zipfile
import io
from django.conf import settings


class AIClient:
    def __init__(self):
        self.base_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
        self.token = "sk-779ed724e4a34b41912335b4689ad75c"
        self.model = "qwen3-coder-plus-2025-09-23"

    def extract_zip_structure(self, zip_file_path):
        """Извлекает структуру файлов из zip-архива"""
        structure = []
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            for file_info in zip_file.filelist:
                if not file_info.is_dir():
                    structure.append(file_info.filename)
        return structure

    def send_to_ai(self, file_structure, prompt):
        """Отправляет запрос к ИИ модели с файловой структурой и промптом"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        # Формируем сообщение для ИИ
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that helps with configuration management. The user has provided a file structure and a prompt. Please analyze the structure and provide appropriate response."
            },
            {
                "role": "user",
                "content": f"File structure: {json.dumps(file_structure, indent=2)}\n\nPrompt: {prompt}"
            }
        ]

        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to AI: {e}")
            return None

    def process_config_request(self, zip_file_path, prompt):
        """Обрабатывает запрос на новую конфигурацию"""
        file_structure = self.extract_zip_structure(zip_file_path)
        ai_response = self.send_to_ai(file_structure, prompt)
        
        if ai_response:
            # Извлекаем ответ от ИИ
            choices = ai_response.get('choices', [])
            if choices:
                content = choices[0].get('message', {}).get('content', '')
                return {
                    'success': True,
                    'content': content,
                    'file_structure': file_structure
                }
        
        return {
            'success': False,
            'content': 'Failed to get response from AI',
            'file_structure': file_structure
        }