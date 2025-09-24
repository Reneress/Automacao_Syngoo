import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from auto import executar_auto
from import_ import executar_import
from relatorio import executar_relatorio


def rodar_auto():
    try:
        executar_auto()
        messagebox.showinfo("Sucesso", "Auto finalizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar Auto:\n{e}")


def rodar_import():
    try:
        executar_import()
        messagebox.showinfo("Sucesso", "Import finalizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar Import:\n{e}")


def rodar_relatorio():
    try:
        executar_relatorio()
        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar Relatório:\n{e}")


def rodar_import_relatorio():
    try:
        executar_import()
        executar_relatorio()
        messagebox.showinfo("Sucesso", "Import + Relatório executados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar Import + Relatório:\n{e}")


def rodar_tudo():
    try:
        executar_auto()
        executar_import()
        executar_relatorio()
        messagebox.showinfo("Sucesso", "Todas as funções foram executadas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar todas as funções:\n{e}")


def iniciar_interface():
    app = ttk.Window(themename="minty")  # Tema verde
    app.title("Controler - Automação")
    app.geometry("400x450")
    app.resizable(False, False)

    ttk.Label(app, text="Escolha uma opção:", font=("Arial", 16, "bold")).pack(pady=20)

    estilo_btn = {"bootstyle": "SUCCESS-OUTSIDE", "width": 25, "padding": 10}

    ttk.Button(app, text="Executar Auto", command=rodar_auto, **estilo_btn).pack(pady=5)
    ttk.Button(app, text="Executar Import", command=rodar_import, **estilo_btn).pack(pady=5)
    ttk.Button(app, text="Executar Relatório", command=rodar_relatorio, **estilo_btn).pack(pady=5)

    ttk.Button(app, text="Executar Import + Relatório", command=rodar_import_relatorio, bootstyle="success-outline", width=25, padding=10).pack(pady=10)
    ttk.Button(app, text="Executar Tudo", command=rodar_tudo, bootstyle="success-outline", width=25, padding=10).pack(pady=10)

    ttk.Button(app, text="Sair", command=app.destroy, bootstyle="danger", width=25, padding=10).pack(pady=15)

    app.mainloop()


if __name__ == "__main__":
    iniciar_interface()
