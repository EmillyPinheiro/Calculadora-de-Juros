import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# calculo
def calcular_juros():
    try:
        c, i, t = map(float, [entry_capital.get(), entry_taxa.get(), entry_tempo.get()])
        i /= 100
        if tipo_juros.get() == "Simples":
            resultado_label.config(text=f"Juros: R$ {c * i * t:.2f}\nTotal: R$ {c + c * i * t:.2f}")
        elif tipo_juros.get() == "Compostos":
            resultado_label.config(text=f"Juros: R$ {c * (1 + i)**t - c:.2f}\nTotal: R$ {c * (1 + i)**t:.2f}")
        else:
            resultado_label.config(text="Selecione o tipo de juros.")
    except ValueError:
        resultado_label.config(text="Valor inválido.")

# janela
janela = tk.Tk()
janela.title("Calculadora de Juros")
janela.geometry("500x700")
janela.resizable(False, False)

# background
fundo_imagem = Image.open("degrade background.png")
fundo_imagem = fundo_imagem.resize((500, 700), Image.Resampling.LANCZOS)  # Ajustar para o tamanho da janela
fundo = ImageTk.PhotoImage(fundo_imagem)

canvas = tk.Canvas(janela, width=500, height=700)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=fundo)

titulo = tk.Label(janela, text="Calculadora de Juros", font=("Arial Bold", 24), fg="white", bg="#2e074d", padx=10, pady=10)
canvas.create_window(250, 50, window=titulo)

# campos entrada de texto
def criar_input(y, texto):
    label = tk.Label(janela, text=texto, font=("Arial", 12), fg="white", bg="#2A2A2A")
    label.config(padx=10, pady=5)
    
    entry = tk.Entry(janela, font=("Arial", 14), bd=0, highlightthickness=0, bg="#1E1E1E", fg="white", justify="center", relief="flat")
    entry.config(highlightbackground="#5E17EB", highlightthickness=2, relief="solid", bd=0)
    
    # label e entry
    canvas.create_window(250, y - 10, window=label)
    canvas.create_window(250, y + 30, window=entry, width=250, height=40, anchor="center") 
    
    return entry

entry_capital = criar_input(150, "Capital (R$)")
entry_taxa = criar_input(250, "Taxa de Juros (%)")
entry_tempo = criar_input(350, "Tempo (anos)")

# combobox 
tipo_juros_label = tk.Label(janela, text="Tipo de Juros", font=("Arial", 12), fg="white", bg="#2A2A2A")
canvas.create_window(250, 430, window=tipo_juros_label)

tipo_juros = ttk.Combobox(janela, values=["Simples", "Compostos"], state="readonly", font=("Arial", 12))
tipo_juros.set("Selecione")
canvas.create_window(250, 470, window=tipo_juros, width=200, height=30)

#botao
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_juros, font=("Arial", 14), bg="#2e074d", fg="white", bd=0, relief="flat", highlightbackground="#5E17EB", highlightthickness=2)
canvas.create_window(250, 530, window=botao_calcular, width=150, height=40)

# resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12), fg="white", bg="#2A2A2A", wraplength=400, justify="center", padx=10, pady=10)
canvas.create_window(250, 600, window=resultado_label, width=400, height=80)

janela.mainloop()
