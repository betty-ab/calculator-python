import tkinter as tk
import math

history_list = []

def on_history_click(event):
    try:
        line_index = history_text.index(tk.CURRENT).split('.')[0]
        line_content = history_text.get(f"{line_index}.0", f"{line_index}.end")
        
        if "=" in line_content:
            result_only = line_content.split('=')[1].strip()
            entry.delete(0, tk.END)
            entry.insert(tk.END, result_only)
    except:
        pass

def update_history(entry_text, result_text):
    history_list.append(f"{entry_text} = {result_text}")
    history_text.config(state="normal")
    history_text.delete("1.0", tk.END)
    
    for item in history_list[-10:]:
        history_text.insert(tk.END, item + "\n", "clickable")
    
    history_text.tag_configure("clickable", foreground="#4DB6AC", font=("Consolas", 11, "bold"))
    history_text.tag_bind("clickable", "<Button-1>", on_history_click)
    
    history_text.config(state="disabled")
    history_text.see(tk.END)

def click(value):
    current_text = entry.get()
    if value == "factorial(" and current_text.isdigit():
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"factorial({current_text})")
    else:
        entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def show_error():
    entry.delete(0, tk.END)
    entry.insert(0, "Error")

def calculate():
    try:
        expr = entry.get()
        if not expr: return

        open_count = expr.count('(')
        close_count = expr.count(')')
        if open_count > close_count:
            expr += ')' * (open_count - close_count)

        processed_expr = expr.replace('^', '**').replace('π', 'math.pi').replace('e', 'math.e')
        
        context = {
            "math": math,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "sqrt": math.sqrt,
            "factorial": math.factorial,
            "pi": math.pi,
            "e": math.e
        }
        
        result = eval(processed_expr, {"__builtins__": None}, context)
        
        entry.delete(0, tk.END)
        if isinstance(result, float):
            result = round(result, 8)
        entry.insert(0, result)
        update_history(expr, result)
    except Exception:
        show_error()

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("Modern Scientific Calculator")
root.geometry("380x680")
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, font=("Arial", 24), bg="#2b2b2b", fg="white",
                 insertbackground="white", justify="right", bd=0)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, sticky="nsew")

# Instruction Label
instr = tk.Label(root, text="Click a previous result to reuse it", bg="#1e1e1e", fg="#555", font=("Arial", 9))
instr.grid(row=1, column=0, columnspan=4)

history_text = tk.Text(root, height=5, bg="#1e1e1e", fg="#888888",
                        state="disabled", font=("Consolas", 11), bd=0, cursor="hand2")
history_text.grid(row=2, column=0, columnspan=4, padx=15, pady=5, sticky="nsew")

buttons = [
    ("C", "clear"), ("(", "("), (")", ")"), ("/", "/"),
    ("7", "7"), ("8", "8"), ("9", "9"), ("*", "*"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("-", "-"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("+", "+"),
    ("0", "0"), (".", "."), ("π", "pi"), ("=", "equal"),
    ("sin", "sin("), ("cos", "cos("), ("tan", "tan("), ("^", "^"),
    ("log", "log("), ("√", "sqrt("), ("!", "factorial("), ("e", "e")
]

row, col = 3, 0 
for (text, value) in buttons:
    if value == "equal":
        cmd = calculate
        color = "#4CAF50"
    elif value == "clear":
        cmd = clear
        color = "#d9534f" 
    elif value in ["sin(", "cos(", "tan(", "log(", "sqrt(", "factorial("]:
        cmd = lambda v=value: click(v)
        color = "#3a3a3a"
    else:
        cmd = lambda v=value: click(v)
        color = "#2b2b2b" 

    tk.Button(root, text=text, font=("Arial", 14, "bold"), bg=color, fg="white",
              activebackground="#555", command=cmd, bd=0, height=2, width=5).grid(
              row=row, column=col, padx=3, pady=3, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.bind('<Return>', lambda event: calculate())
for i in range(3, 10): root.rowconfigure(i, weight=1)
for i in range(4): root.columnconfigure(i, weight=1)

root.mainloop()
