import os
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk

def open_signup_window(main_window_size):
    signup_window = tk.Toplevel()
    signup_window.title("Inscription")
    signup_window.geometry(main_window_size) 
    signup_window.configure(bg='white')

        # Charger l'image pour le logo
    webtv_image = Image.open(os.path.join(os.path.dirname(__file__), "images", "WebTV.png"))
    webtv_photo = ImageTk.PhotoImage(webtv_image)


    
    original_width, original_height = webtv_image.size
    # Get the current size of the image
    
    # Define new dimensions (e.g., double the size)
    new_width = original_width * 2
    new_height = original_height * 2
    
    bigger_webtv_image = webtv_image.resize((new_width, new_height))
    
    # Convert the resized image for use with Tkinter
    webtv_photo = ImageTk.PhotoImage(bigger_webtv_image)

    # Définir les polices
    title_font = tkfont.Font(family='Helvetica', size=18, weight='bold')
    entry_font = tkfont.Font(family='Helvetica', size=12)

    # Frame pour le logo
    logo_frame = tk.Frame(signup_window, bg='white')
    logo_frame.pack(side='top', pady=20)
    logo_label = tk.Label(logo_frame, image=webtv_photo, bg='white')
    logo_label.image = webtv_photo
    logo_label.pack()

    # Frame pour le titre "Inscription"
    subtitle_frame = tk.Frame(signup_window, bg='white')
    subtitle_frame.pack(side='top', pady=10)
    subtitle_label = tk.Label(subtitle_frame, text='Inscription', font=title_font, bg='white')
    subtitle_label.pack()

    # Frame pour les champs de saisie
    form_frame = tk.Frame(signup_window, bg='white')
    form_frame.pack(side='top', pady=20)

    # Champ de saisie pour le nom d'utilisateur
    label_username = tk.Label(form_frame, text="Nom d'utilisateur", bg='white', font=entry_font)
    label_username.grid(row=0, column=0, sticky='w', padx=10)
    entry_username = tk.Entry(form_frame, font=entry_font, width=30)
    entry_username.grid(row=0, column=1, pady=5, padx=10)

    # Champ de saisie pour le mot de passe
    label_password = tk.Label(form_frame, text="Mot de passe", bg='white', font=entry_font)
    label_password.grid(row=1, column=0, sticky='w', padx=10)
    entry_password = tk.Entry(form_frame, font=entry_font, show='*', width=30)
    entry_password.grid(row=1, column=1, pady=5, padx=10)

    # Champ de saisie pour l'email
    label_email = tk.Label(form_frame, text="Email", bg='white', font=entry_font)
    label_email.grid(row=2, column=0, sticky='w', padx=10)
    entry_email = tk.Entry(form_frame, font=entry_font, width=30)
    entry_email.grid(row=2, column=1, pady=5, padx=10)

    # Champ de saisie pour le téléphone
    label_telephone = tk.Label(form_frame, text='Téléphone', bg='white', font=entry_font)
    label_telephone.grid(row=3, column=0, sticky='w', padx=10)
    entry_telephone = tk.Entry(form_frame, font=entry_font, width=30)
    entry_telephone.grid(row=3, column=1, pady=5, padx=10)

    # Bouton d'inscription
    signup_button = tk.Button(form_frame, text="S'inscription", bg='black', fg='white', font=entry_font, relief='flat', width=30)
    signup_button.grid(row=4, column=0, columnspan=2, pady=20, padx=10)