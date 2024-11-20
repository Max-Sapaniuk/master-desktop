import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from bs4 import BeautifulSoup
import requests

# Завантаження токенізатора та моделі
model_path = './working/fake-news-model'
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained(model_path)


# Функція для передбачення на основі тексту
def classify_message(message):
    inputs = tokenizer(message, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    return "Фейкове повідомлення" if prediction == 1 else "Правдиве повідомлення"


# Функція для витягнення тексту з вебсторінки
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            page_text = ' '.join([p.get_text() for p in paragraphs])
            return page_text
        else:
            return None
    except Exception as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None


# Створення графічного інтерфейсу (GUI) з Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Виявлення фейкових повідомлень")
    root.geometry("500x300")
    root.configure(bg="#2c2c2c")  # Темний фон

    # Налаштування стилів через ttk
    style = ttk.Style()
    style.theme_use("clam")  # Використовуємо "clam" тему для більшої кастомізації
    style.configure("TButton",
                    background="#ff4500",  # Темно-помаранчевий фон для кнопки
                    foreground="white",  # Білий текст
                    font=("Helvetica", 10, "bold"),
                    padding=6,

                    relief="flat")
    style.map("TButton",
              background=[("active", "#ff8c00")],)  # Світліший помаранчевий при наведенні мишки

    # Кольори
    bg_color = "#2c2c2c"  # Темний фон
    text_color = "#ff8c00"  # Темно-помаранчевий колір
    result_color = "#ffa500"  # Яскраво-помаранчевий для результату

    # Заголовок
    title_label = tk.Label(root, text="Fake News Detection", font=("Helvetica", 16, "bold"), bg=bg_color, fg=text_color)
    title_label.pack(pady=20)

    # Поле для введення повідомлення або URL
    label = tk.Label(root, text="Введіть повідомлення або URL для аналізу:", font=("Helvetica", 12, "bold"),
                     bg=bg_color, fg=text_color)
    label.pack(pady=10)

    message_entry = tk.Entry(root, width=50, font=("Helvetica", 10), borderwidth=2, relief="groove", bg="#3a3a3a",
                             fg="white")
    message_entry.pack(pady=5)

    # Поле для виводу результату
    result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg=bg_color, fg=result_color)
    result_label.pack(pady=10)

    # Функція для обробки натискання кнопки "Перевірити"
    def check_message():
        message = message_entry.get()
        if not message:
            messagebox.showwarning("Попередження", "Будь ласка, введіть повідомлення або URL.")
            return

        # Перевіряємо, чи це URL
        if message.startswith("http://") or message.startswith("https://"):
            page_text = extract_text_from_url(message)
            if page_text:
                result = classify_message(page_text)
                result_label.config(text=f"Результат: {result}")
            else:
                messagebox.showerror("Помилка", "Не вдалося завантажити або проаналізувати сторінку.")
        else:
            result = classify_message(message)
            result_label.config(text=f"Результат: {result}")

    # Кнопка для запуску перевірки
    check_button = ttk.Button(root, text="Перевірити", style="TButton", command=check_message)
    check_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
