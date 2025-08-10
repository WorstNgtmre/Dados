import random
import customtkinter as ctk

def toggle_bonus():
    state = "normal" if bonus_active.get() else "disabled"
    entry_bon.configure(state=state)
    toggle_signo.configure(state=state)
    if not bonus_active.get():
        entry_bon.delete(0, ctk.END)
        entry_bon.insert(0, "0")

# ---------- Lanzamiento ----------
def lanzar():
    try:
        cant = int(entry_cant.get())
        caras = int(dropdown_caras.get())

        if bonus_active.get():
            bon = int(entry_bon.get())
            signo = toggle_signo.get()
            bon = -bon if signo == "-" else bon
        else:
            bon = 0

        valores = [random.randint(1, caras) for _ in range(cant)]
        total_dados = sum(valores)
        resultado_final = total_dados + bon

        output.configure(state="normal")
        output.delete("1.0", ctk.END)
        output.insert(ctk.END, f"Tirada: {cant}d{caras}")
        if bonus_active.get() and bon != 0:
            output.insert(ctk.END, f"{'+' if bon >= 0 else ''}{bon}")
        output.insert(ctk.END, "\n")
        for i, v in enumerate(valores, 1):
            output.insert(ctk.END, f"Dado {i}: {v}\n")
        output.insert(ctk.END, f"\nTotal dados: {total_dados}\n")
        if bon != 0:
            output.insert(ctk.END, f"Bonus: {bon:+}\n")
        output.insert(ctk.END, f"Resultado final: {resultado_final}")
        output.configure(state="disabled")

    except ValueError:
        output.configure(state="normal")
        output.delete("1.0", ctk.END)
        output.insert(ctk.END, "Revisa los valores introducidos.")
        output.configure(state="disabled")

# ---------- GUI ----------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Lanzador de Dados")
root.geometry("500x540")
root.resizable(True, True)
# ---------- Bonus enable/disable ----------
bonus_active = ctk.BooleanVar(value=False)

top = ctk.CTkFrame(root, fg_color="transparent")
top.pack(pady=20)

# Cantidad
ctk.CTkLabel(top, text="Cantidad:").grid(row=0, column=0, padx=10, pady=5)
entry_cant = ctk.CTkEntry(top, width=60, justify="center")
entry_cant.insert(0, "2")
entry_cant.grid(row=0, column=1, padx=10)

# Caras
ctk.CTkLabel(top, text="Caras:").grid(row=0, column=2, padx=10)
dropdown_caras = ctk.CTkComboBox(top, values=["4", "6", "8", "10", "12", "20", "100"], width=70)
dropdown_caras.set("6")
dropdown_caras.grid(row=0, column=3, padx=10)

# Bonificador
ctk.CTkLabel(top, text="Bonif:").grid(row=1, column=0, padx=10, pady=10)
entry_bon = ctk.CTkEntry(top, width=60, justify="center")
entry_bon.insert(0, "1")
entry_bon.grid(row=1, column=1, padx=10)

toggle_signo = ctk.CTkSegmentedButton(top, values=["+", "-"], width=90)
toggle_signo.set("+")
toggle_signo.grid(row=1, column=2, columnspan=2, padx=10)

# Checkbox
chk_bonus = ctk.CTkCheckBox(top, text="Usar bonus", variable=bonus_active,
                            command=toggle_bonus)
chk_bonus.grid(row=2, column=0, columnspan=4, pady=(10,0))

# Botón lanzar
ctk.CTkButton(root, text="¡Lanzar!", command=lanzar, width=200).pack(pady=10)

# Output
output = ctk.CTkTextbox(root, width=340, height=260, state="disabled", font=("Consolas", 12))
output.pack(pady=10)

root.mainloop()