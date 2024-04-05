import os
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from signup_page import open_signup_window 

def open_login_window(main_window_size):
    login_window = tk.Toplevel()
    login_window.title("Connexion")
    login_window.geometry(main_window_size) 
    login_window.configure(bg='white')

    # Charger l'image pour le logo
    webtv_image = Image.open(os.path.join(os.path.dirname(__file__), "images", "WebTV.png"))
    webtv_photo = ImageTk.PhotoImage(webtv_image)


    
    original_width, original_height = webtv_image.size
    # Get the current size of the image
    
    # Define new dimensions (e.g., double the size)
    new_width = original_width * 2
    new_height = original_height * 2
    
    # Resize the image to the new dimensions
    bigger_webtv_image = webtv_image.resize((new_width, new_height))
    
    # Convert the resized image for use with Tkinter
    webtv_photo = ImageTk.PhotoImage(bigger_webtv_image)

    # Définir les polices
    title_font = tkfont.Font(family='Helvetica', size=18, weight='bold')
    entry_font = tkfont.Font(family='Helvetica', size=12)

    # Frame pour le logo
    logo_frame = tk.Frame(login_window, bg='white')
    logo_frame.pack(side='top', pady=20)
    logo_label = tk.Label(logo_frame, image=webtv_photo, bg='white')
    logo_label.image = webtv_photo  # Garder une référence
    logo_label.pack()

    # Frame pour le titre "Connexion"
    subtitle_frame = tk.Frame(login_window, bg='white')
    subtitle_frame.pack(side='top', pady=10)
    subtitle_label = tk.Label(subtitle_frame, text='Connexion', font=title_font, bg='white')
    subtitle_label.pack()

    # Frame pour les champs de saisie
    form_frame = tk.Frame(login_window, bg='white')
    form_frame.pack(side='top', pady=20)

    # Champs de saisie
    entry_username = tk.Entry(form_frame, font=entry_font, width=20)
    entry_username.grid(row=0, column=1, pady=5)
    label_username = tk.Label(form_frame, text="Nom d'utilisateur", bg='white')
    label_username.grid(row=0, column=0, pady=5)

    entry_password = tk.Entry(form_frame, font=entry_font, show='*', width=20)
    entry_password.grid(row=1, column=1, pady=5)
    label_password = tk.Label(form_frame, text='Mot de passe', bg='white')
    label_password.grid(row=1, column=0, pady=5)

    # Bouton de connexion
    login_button = tk.Button(form_frame, text="Login", bg='purple', fg='white', font=entry_font, relief='flat', width=20)
    login_button.grid(row=2, column=0, columnspan=2, pady=20)

    # Question "pas de compte ?"
    no_account_frame = tk.Frame(login_window, bg='white')
    no_account_frame.pack(side='top')
    no_account_label = tk.Label(no_account_frame, text="pas de compte ?", fg="black", bg='white', font=entry_font)
    no_account_label.pack()

    # Bouton "S'inscrire"
    signup_button = tk.Button(no_account_frame, text="S'inscrire", bg='black', fg='white', font=entry_font, relief='flat', command=open_signup_window)
    signup_button.pack()

    