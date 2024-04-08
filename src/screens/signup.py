import tkinter as tk
from PIL import Image, ImageTk

class SignupPage(tk.Frame):
    def __init__(self, parent, styles, controller):
        super().__init__(parent, bg=styles.base_style['bg'])
        self.styles = styles
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        # Back button frame
        back_frame = tk.Frame(self, bg=self.styles.base_style['bg'])
        back_frame.pack(side='top', anchor='nw', padx=10, pady=10)

        # Back button
        back_image_path = "images/backtrack.png"
        back_image = Image.open(back_image_path).resize((48, 48))
        back_photo = ImageTk.PhotoImage(back_image)
        back_button = tk.Button(back_frame, image=back_photo, command=lambda: self.controller.switch_frame('HomePage'), borderwidth=0)
        back_button.image = back_photo
        back_button.pack(side='left')

        # Centered frame for the signup elements
        center_frame = tk.Frame(self, bg=self.styles.base_style['bg'])
        center_frame.pack(expand=True)

        # Logo
        webtv_image_path = self.styles.resource_path("images/WebTV.png")
        webtv_image = Image.open(webtv_image_path)
        webtv_photo = ImageTk.PhotoImage(webtv_image)
        logo_label = tk.Label(center_frame, image=webtv_photo, bg=self.styles.base_style['bg'])
        logo_label.image = webtv_photo
        logo_label.pack(pady=20)

        # Title "Inscription"
        subtitle_label = tk.Label(center_frame, text='Inscription', font=self.styles.large_font, bg=self.styles.base_style['bg'])
        subtitle_label.pack(pady=(0, 20))

        # Entry fields
        self.create_entry(center_frame, "Nom d'utilisateur", 0)
        self.create_entry(center_frame, "Mot de passe", 1, show='*')
        self.create_entry(center_frame, "Email", 2)
        self.create_entry(center_frame, "Téléphone", 3)

        # Sign up button
        signup_button_canvas = self.styles.create_rounded_button(center_frame, "S'inscrire", self.submit_signup)
        signup_button_canvas.pack(pady=10)

    def create_entry(self, parent, label, row, show=None):
        entry_frame = tk.Frame(parent, bg=self.styles.base_style['bg'])
        entry_frame.pack(pady=5, fill='x', padx=50)

        # Set a fixed width for the label column
        label_widget = tk.Label(entry_frame, text=label, width=20, anchor='w', **self.styles.base_style)
        label_widget.grid(row=0, column=0, padx=(0, 10))

        entry_container = tk.Frame(entry_frame, borderwidth=1.5, relief='sunken', bg='white')
        entry_container.grid(row=0, column=1, sticky='ew', padx=(0, 10))
        entry_frame.grid_columnconfigure(1, weight=1)

        entry_widget = tk.Entry(entry_container, **self.styles.entry_style, show=show, width=30)
        entry_widget.pack(fill='both', expand=True)

        # Set the attributes for username, password, email, and phone entries
        if label == "Nom d'utilisateur":
            self.entry_username = entry_widget
        elif label == "Mot de passe":
            self.entry_password = entry_widget
        elif label == "Email":
            self.entry_email = entry_widget
        elif label == "Téléphone":
            self.entry_phone = entry_widget

    def submit_signup(self):
        # Handle the signup submission here
        print("Signup submitted")
