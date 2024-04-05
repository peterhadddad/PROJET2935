import tkinter as tk
from tkinter import Scrollbar
from PIL import Image, ImageTk
from signup_page import open_signup_window  # importez la fonction de votre deuxième script
from login_page import open_login_window
import os  # Importez le module os pour travailler avec les chemins de fichiers


def on_resize(event):
    # Réajuster la position des boutons lors du redimensionnement de la fenêtre
    header.grid_columnconfigure(0, weight=1)
    header.grid_columnconfigure(1, weight=0)  # Empêcher le réajustement de cette colonne
    header.grid_columnconfigure(2, weight=1)


root = tk.Tk()
root.title("WeTV")

root.geometry('800x600')

# Fonction appelée lors du redimensionnement de la fenêtre
root.bind("<Configure>", on_resize)

# Frame principale avec une barre de défilement
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Créer un canevas pour contenir la frame de contenu
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Ajouter une barre de défilement verticale au canevas
scrollbar = Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurer le canevas pour utiliser la barre de défilement
canvas.configure(yscrollcommand=scrollbar.set)

# Créer une nouvelle frame pour contenir tous les widgets
content_frame = tk.Frame(canvas)
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Frame pour l'en-tête
header = tk.Frame(content_frame, bg="#F5F5F5")  # Couleur de fond grise
header.grid(row=0, column=0, sticky='ew')

# Icône pour le menu à gauche
# Chemin relatif vers l'icône de menu
menu_icon_path = "tp1/images/Style=bulk.png"
menu_icon_img = Image.open(menu_icon_path)
menu_icon_img = menu_icon_img.resize((30, 30))
menu_icon = ImageTk.PhotoImage(menu_icon_img)
menu_icon_label = tk.Label(header, image=menu_icon, bg="#F5F5F5")  # Afficher l'icône du menu
menu_icon_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Logo à côté de l'icône du menu
logo_path = "tp1/images/WebTV.png"
logo_img = Image.open(logo_path)
logo_img = logo_img.resize((100, 50))
logo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(header, image=logo, bg="#F5F5F5")  # Afficher le logo
logo_label.grid(row=0, column=1)

# Espace entre le logo et le reste de l'en-tête
tk.Label(header, text="", bg="#F5F5F5").grid(row=0, column=2)

# Barre de recherche à droite
search_bar = tk.Entry(header, width=40, bg="#FFFFFF", fg="#333333", font=("Arial", 12), bd=1, relief="groove")  # Contour arrondi
search_bar.grid(row=0, column=3, padx=(0, 10), pady=10, sticky='e')

# Icône loupe
search_icon_path = "tp1/images/search.png"
search_icon_img = Image.open(search_icon_path)
search_icon_img = search_icon_img.resize((15, 15))
search_icon = ImageTk.PhotoImage(search_icon_img)
search_icon_label = tk.Label(search_bar, image=search_icon, bg="#FFFFFF")  # Afficher l'icône de recherche à l'intérieur de la barre de recherche
search_icon_label.place(relx=0.99, rely=0.5, anchor='e')  # Positionner l'icône de recherche à droite de la barre de recherche

# Frame pour les boutons
buttons_frame = tk.Frame(header, bg="#F5F5F5")  # Couleur de fond grise
buttons_frame.grid(row=0, column=4, padx=(0, 10), pady=10, sticky='e')

# Bouton "S'inscrire" qui appelle la fonction open_signup_window
btn_signup = tk.Button(buttons_frame, text="S'inscrire", bg="black", fg="white", font=("Arial", 10, "bold"), command=lambda: open_signup_window(root.geometry()))
btn_signup.grid(row=0, column=0, padx=(0, 10))

# Bouton "Se connecter"
btn_login = tk.Button(buttons_frame, text="Se connecter", bg="black", fg="white", font=("Arial", 10, "bold"), command=lambda: open_login_window(root.geometry()))  # Bouton gris avec texte noir
btn_login.grid(row=0, column=1, padx=(0, 10))

# Icône utilisateur
user_icon_path = "tp1/images/user.png"
user_icon_img = Image.open(user_icon_path)
user_icon_img = user_icon_img.resize((30, 30))
user_icon = ImageTk.PhotoImage(user_icon_img)
user_icon_label = tk.Label(header, image=user_icon, bg="#F5F5F5")  # Afficher l'icône utilisateur
user_icon_label.grid(row=0, column=5, padx=10, pady=10, sticky='e')


# Fonction pour ajouter une catégorie
def add_category(root, category_name, thumbnails, row):
    frame = tk.Frame(content_frame)
    frame.grid(row=row, column=0, sticky='ew', pady=(100, 100))
    frame.grid_columnconfigure(1, weight=1)

    # Titre en gras
    label = tk.Label(frame, text=category_name, font=("Arial", 12, "bold"), bg="#F5F5F5", fg="#333333")  # Couleur de fond et de texte ajustées
    label.grid(row=0, column=0, sticky='w', padx=20)

    # Vignettes
    for i, thumb in enumerate(thumbnails):
        frame.grid_columnconfigure(i+2, weight=1)
        tk.Label(frame, image=thumb).grid(row=0, column=i+1, sticky='w', padx=10)


# Images exemple
img = tk.PhotoImage(width=100, height=50)
image1 = Image.open(os.path.join(os.path.dirname(__file__), "images", "KattyPerry.png"))
image2 = Image.open(os.path.join(os.path.dirname(__file__), "images", "Rihana.png"))
image3 = Image.open(os.path.join(os.path.dirname(__file__), "images", "Beyonce.png"))
image4 = Image.open(os.path.join(os.path.dirname(__file__), "images", "JustinBieber.png"))

image5 = Image.open(os.path.join(os.path.dirname(__file__), "images", "Chien.png"))
image6 = Image.open(os.path.join(os.path.dirname(__file__), "images", "Bebe.png"))
image7 = Image.open(os.path.join(os.path.dirname(__file__), "images", "Laugh.png"))
image8 = Image.open(os.path.join(os.path.dirname(__file__), "images", "fails1.png"))

image9 = Image.open(os.path.join(os.path.dirname(__file__), "images", "News1.png"))
image10 = Image.open(os.path.join(os.path.dirname(__file__), "images", "News2.png"))
image11 = Image.open(os.path.join(os.path.dirname(__file__), "images", "News3.png"))
image12 = Image.open(os.path.join(os.path.dirname(__file__), "images", "News4.png"))

photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
photo3 = ImageTk.PhotoImage(image3)
photo4 = ImageTk.PhotoImage(image4)

photo5 = ImageTk.PhotoImage(image5)
photo6 = ImageTk.PhotoImage(image6)
photo7 = ImageTk.PhotoImage(image7)
photo8 = ImageTk.PhotoImage(image8)

photo9 = ImageTk.PhotoImage(image9)
photo10 = ImageTk.PhotoImage(image10)
photo11 = ImageTk.PhotoImage(image11)
photo12 = ImageTk.PhotoImage(image12)
add_category(root,  "Music", [photo1, photo2, photo3, photo4], 1)
add_category(root, "Funny videos", [photo5, photo6, photo7, photo8], 2)
add_category(root, "News", [photo9, photo10, photo11, photo12], 3)

root.mainloop()