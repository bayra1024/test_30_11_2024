import requests


def upload_file(api_url, file_path):
    """
    Завантажує файл на вказаний API URL.

    Args:
        api_url (str): URL для завантаження файлу.
        file_path (str): Шлях до файлу, який потрібно завантажити.

    Returns:
        str: Відповідь від API.
    """
    try:
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(api_url, files=files)

            # Перевірка статусу відповіді
            if response.status_code == 200:
                return f"Файл успішно завантажено: {response.text}"
            else:
                return f"Помилка: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Помилка під час завантаження: {str(e)}"


# Використання функції
api_url = "https://load-dag-135714666888.us-central1.run.app"
file_path = "test_dag.py"  # Заміна на фактичний шлях до файлу
print(upload_file(api_url, file_path))
