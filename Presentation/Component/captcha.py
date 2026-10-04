import random
import string
from io import BytesIO

import tkinter as tk
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha


class CaptchaComponent(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.captcha = ImageCaptcha(width=180, height=60)

        self.current_code = ""

        self.image_label = tk.Label(self)
        self.image_label.grid(row=0, column=0, padx=5)

        self.refresh_button = tk.Button(
            self,
            text="Refresh",
            command=self.refresh
        )
        self.refresh_button.grid(row=0, column=1, padx=5)

        self.entry = tk.Entry(self)
        self.entry.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=5,
            sticky="ew"
        )

        self.refresh()

    def generate_code(self):
        characters = string.ascii_uppercase + string.digits

        return "".join(
            random.choices(characters, k=5)
        )

    def refresh(self):
        # Generate new CAPTCHA code
        self.current_code = self.generate_code()

        # Generate CAPTCHA image
        image_data = self.captcha.generate(self.current_code)

        # Convert generated image to Tkinter image
        image = Image.open(BytesIO(image_data.getvalue()))

        self.photo = ImageTk.PhotoImage(image)

        self.image_label.configure(image=self.photo)

        # Clear user input
        self.entry.delete(0, tk.END)

    def get_value(self):
        return self.entry.get().strip().upper()

    def is_valid(self):
        return self.get_value() == self.current_code