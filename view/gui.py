import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from generator.generator import Generator

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("QR Code Generator")
        self.qr_generator = Generator('test')
        self.start_window()

    def start_window(self):
          
        self.label = tk.Label(self.window, text="Enter URL:")
        self.label.pack()

        self.url_entry = tk.Entry(self.window, width=40)
        self.url_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate QR Code", command=self.generate_qrcode)
        self.generate_button.pack()

        self.qr_code_image_label = tk.Label(self.window)
        self.qr_code_image_label.pack()

        self.save_button = tk.Button(self.window, text="Download QR Code", command=self.save_qrcode, state=tk.DISABLED)
        self.save_button.pack()

    def generate_qrcode(self):
        url = self.url_entry.get()
        if url:
            qr_image = self.qr_generator.generate_qr_code(url)
            self.qr_image = ImageTk.PhotoImage(qr_image)
            self.qr_code_image_label.config(image=self.qr_image)
            self.save_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Invalid input", "Please, input an URL.")

    def save_qrcode(self):
        """Permite ao usuário salvar o QR Code gerado em um local à sua escolha."""
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        print(f"Tentando salvar em: {file_path}")
        if file_path:
            self.qr_generator.save_qr_code(file_path)
            messagebox.showinfo("Success!", f"QR Code downloaded to: {file_path}")
            
        
    def run(self):
        self.window.mainloop()
    