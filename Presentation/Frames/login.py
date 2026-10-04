from tkinter import Frame, Label, Entry, Button, Checkbutton, messagebox

from Presentation.Component.password_entry import PasswordEntry
from Presentation.Component.captcha import CaptchaComponent

from BusinessLogic.user_business_logic import UserBusinessLogic


class LoginFrame(Frame):

    def __init__(
        self,
        main_window,
        main_view,
        user_business: UserBusinessLogic
    ):
        super().__init__(main_window)

        self.main_view = main_view
        self.user_business = user_business

        self.grid_columnconfigure(1, weight=1)

        # -------------------------
        # Username
        # -------------------------

        self.username_label = Label(
            self,
            text="Username"
        )

        self.username_label.grid(
            row=0,
            column=0,
            pady=10,
            padx=10,
            sticky="e"
        )

        self.username_entry = Entry(self)

        self.username_entry.grid(
            row=0,
            column=1,
            pady=10,
            padx=(0, 10),
            sticky="ew"
        )

        # -------------------------
        # Password
        # -------------------------

        self.password_label = Label(
            self,
            text="Password"
        )

        self.password_label.grid(
            row=1,
            column=0,
            pady=(0, 10),
            padx=10,
            sticky="e"
        )

        self.password_entry = PasswordEntry(self)

        self.password_entry.grid(
            row=1,
            column=1,
            pady=(0, 10),
            padx=(0, 10),
            sticky="ew"
        )

        # -------------------------
        # CAPTCHA
        # -------------------------

        self.captcha = CaptchaComponent(self)

        self.captcha.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10,
            padx=10
        )

        # -------------------------
        # Remember Me
        # -------------------------

        self.remember_me_button = Checkbutton(
            self,
            text="Remember Me?"
        )

        self.remember_me_button.grid(
            row=3,
            column=1,
            pady=(0, 10),
            padx=(0, 10),
            sticky="w"
        )

        # -------------------------
        # Login Button
        # -------------------------

        self.login_button = Button(
            self,
            text="Login",
            command=self.login_button_clicked
        )

        self.login_button.grid(
            row=4,
            column=1,
            pady=(0, 10),
            padx=(0, 10),
            sticky="w"
        )

        # -------------------------
        # Register Button
        # -------------------------

        self.register_button = Button(
            self,
            text="Register",
            command=self.register_button_clicked
        )

        self.register_button.grid(
            row=5,
            column=1,
            pady=(0, 10),
            padx=(0, 10),
            sticky="w"
        )

    def login_button_clicked(self):

        username = self.username_entry.get()

        password = self.password_entry.get_value()

        # -------------------------
        # Validate CAPTCHA first
        # -------------------------

        if not self.captcha.is_valid():

            messagebox.showerror(
                "CAPTCHA Error",
                "Invalid CAPTCHA."
            )

            self.captcha.refresh()

            return

        # -------------------------
        # Login
        # -------------------------

        response = self.user_business.login(
            username,
            password
        )

        if response.success:

            messagebox.showinfo(
                "Login",
                response.message
            )

        else:

            messagebox.showerror(
                "Login Failed",
                response.message
            )

    def register_button_clicked(self):

        self.main_view.show_frame("register")