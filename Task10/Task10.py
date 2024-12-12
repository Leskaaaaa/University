import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combobox_operation.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ValueError("Деление на ноль.")
            result = num1 / num2
        else:
            raise ValueError("Некорректная операция.")
        label_result.config(text=f"Результат: {result}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")

def show_checkbox_result():
    if var1.get():
        choice = "первый вариант"
    elif var2.get():
        choice = "второй вариант"
    elif var3.get():
        choice = "третий вариант"
    else:
        choice = "ничего не выбрано"
    messagebox.showinfo("Ваш выбор", f"Вы выбрали {choice}.")

def load_text_file():
    file_path = filedialog.askopenfilename(title="Открыть файл", filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text_content)

app = tk.Tk()
app.title("Рвачев Алексей Сергеевич")

notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

#Вкладка 1: Калькулятор
frame_calculator = ttk.Frame(notebook)
notebook.add(frame_calculator, text="Калькулятор")

label_num1 = ttk.Label(frame_calculator, text="Число 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = ttk.Entry(frame_calculator)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_operation = ttk.Label(frame_calculator, text="Операция:")
label_operation.grid(row=0, column=2, padx=5, pady=5)
combobox_operation = ttk.Combobox(frame_calculator, values=["+", "-", "*", "/"], state="readonly")
combobox_operation.grid(row=0, column=3, padx=5, pady=5)
combobox_operation.current(0)

label_num2 = ttk.Label(frame_calculator, text="Число 2:")
label_num2.grid(row=0, column=4, padx=5, pady=5)
entry_num2 = ttk.Entry(frame_calculator)
entry_num2.grid(row=0, column=5, padx=5, pady=5)

button_calculate = ttk.Button(frame_calculator, text="Вычислить", command=calculate)
button_calculate.grid(row=1, column=0, columnspan=6, pady=10)

label_result = ttk.Label(frame_calculator, text="Результат:")
label_result.grid(row=2, column=0, columnspan=6, pady=5)

#Вкладка2: Чекбоксы
frame_checkboxes = ttk.Frame(notebook)
notebook.add(frame_checkboxes, text="Чекбоксы")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = ttk.Checkbutton(frame_checkboxes, text="Первый", variable=var1)
checkbox1.pack(anchor="w", padx=10, pady=5)
checkbox2 = ttk.Checkbutton(frame_checkboxes, text="Второй", variable=var2)
checkbox2.pack(anchor="w", padx=10, pady=5)
checkbox3 = ttk.Checkbutton(frame_checkboxes, text="Третий", variable=var3)
checkbox3.pack(anchor="w", padx=10, pady=5)

button_show_choice = ttk.Button(frame_checkboxes, text="Показать выбор", command=show_checkbox_result)
button_show_choice.pack(pady=10)

#Вкладка 3: Работа с текстом
frame_text = ttk.Frame(notebook)
notebook.add(frame_text, text="Работа с текстом")

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=load_text_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=app.quit)

text_area = tk.Text(frame_text, wrap="word")
text_area.pack(fill="both", expand=True, padx=10, pady=10)

# Запуск приложения
app.mainloop()