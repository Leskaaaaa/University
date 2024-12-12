import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

def fetch_repository_data():
    repo_name = entry_repo_name.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория.")
        return

    url = f"https://api.github.com/repos/{repo_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        repo_data = response.json()

        filtered_data = {
            'company': repo_data.get('owner', {}).get('company', None),
            'created_at': repo_data.get('created_at', None),
            'email': repo_data.get('owner', {}).get('email', None),
            'id': repo_data.get('owner', {}).get('id', None),
            'name': repo_data.get('owner', {}).get('login', None),
            'url': repo_data.get('owner', {}).get('url', None),
        }

        output_file = "repository_data.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Успех", f"Данные сохранены в файл: {output_file}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

app = tk.Tk()
app.title("API Рвачев")

frame_input = ttk.Frame(app)
frame_input.pack(pady=10, padx=10, fill="x")

label_repo_name = ttk.Label(frame_input, text="Имя репозитория (формат: owner/repo):")
label_repo_name.pack(anchor="w")

entry_repo_name = ttk.Entry(frame_input)
entry_repo_name.pack(fill="x")

button_fetch = ttk.Button(app, text="Получить данные", command=fetch_repository_data)
button_fetch.pack(pady=10)

app.mainloop()