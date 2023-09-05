import PyPDF2
import tkinter as tk
from tkinter import filedialog

def unirPDF():
    archivosPDF = filedialog.askopenfilenames(title="Selecciona los archivos PDF", filetypes=[("Archivos PDF", ".pdf")])
    if archivosPDF:
        pdfEscribir = PyPDF2.PdfWriter()
        for archivo in archivosPDF:
            with open(archivo, "rb") as pdfFile:
                pdfLeer = PyPDF2.PdfReader(pdfFile)
                for pagina in range(len(pdfLeer.pages)):
                    paginaActual = pdfLeer.pages[pagina]
                    pdfEscribir.add_page(paginaActual)
        archivoSalida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", ".pdf")])
        if archivoSalida:
            with open(archivoSalida, "wb") as salidaPDF:
                pdfEscribir.write(salidaPDF)
            mensaje_label.config(text=f"Archivo PDF unido y guardado correctamente '{archivoSalida}'")

app = tk.Tk()
app.title("Unir PDFs")

unirBoton = tk.Button(app, text="Unir PDF", command=unirPDF)
unirBoton.pack(pady=20)

mensaje_label = tk.Label(app, text="")
mensaje_label.pack()

app.mainloop()