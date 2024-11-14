import os
import qrcode

class Generator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.qr_img = None

    def generate_qr_code(self, url):
        self.qr_img = qrcode.make(url)
        return self.qr_img
    
    def save_qr_code(self, file_path):
        if file_path:
            self.qr_img.save(file_path)
        else:
            self.qr_img.save(self.output_dir)