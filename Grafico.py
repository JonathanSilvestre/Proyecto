import ImportacionBD as bd
import tkinter as tk
from tkinter import ttk

def mostrar_lista(productos):
    root = tk.Tk()
    root.title("Inventario de Productos")

    tree = ttk.Treeview(root, columns=("ID", "Descripción", "Cantidad", "Precio", "Talla", "Color"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Descripción", text="Descripción")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Precio", text="Precio")
    tree.heading("Talla", text="Talla")
    tree.heading("Color", text="Color")

    for producto in productos:
        tree.insert("", tk.END, values=producto)

    tree.pack(expand=True, fill='both')
    root.mainloop()

def main():
    nombre_archivo = 'inventario.csv'
    
    # Leer el archivo CSV
    productos = bd.leer_csv(nombre_archivo)
    
    # Mostrar lista en la interfaz gráfica
    mostrar_lista(productos)

if __name__ == '__main__':
    main()