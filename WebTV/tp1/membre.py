import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
from PIL import Image, ImageTk, ImageDraw

def add_category(root, thumbnails, row):
    frame = tk.Frame(content_frame)
    frame.grid(row=row, column=0, sticky='ew', pady=(100,100))
    frame.grid_columnconfigure(1, weight=1)

    # Vignettes
    for i, thumb in enumerate(thumbnails):
        frame.grid_columnconfigure(i+2, weight=1)
        tk.Label(frame, image=thumb).grid(row=0, column=i+1, sticky='w', padx=10)


def create_image(path, size):
   
    """Load an image from the given path and resize it to the specified size."""
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)  # Updated to use Resampling.LANCZOS
    return ImageTk.PhotoImage(img)

# Function to create a rounded button
def create_rounded_button(container, text, command=None):
    return tk.Button(
        container, 
        text=text, 
        command=command, 
        bg="white", 
        fg="black", 
        bd=0, 
        font=tkfont.Font(family="Arial", size=10, weight="bold")
    )


def create_round_image(path, size):
    img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + img.size, fill=255)
    
    result = Image.new('RGBA', img.size, (255, 255, 255, 0))
    result.paste(img, (0, 0), mask=mask)
    return ImageTk.PhotoImage(result)


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


# Configurer le canevas pour utiliser la barre de défilement


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



#A modifier avec le path  absolu qui est dans le sratch.py
# Profile Picture
profile_pic = create_image("C:\\Users\\Aymen\\Desktop\\WebTV_2\\WebTV_2\\WebTV\\images\\user.png", (100, 100))
profile_pic_label = tk.Label(profile_frame, image=profile_pic, bg="#F5F5F5")
profile_pic_label.grid(row=0, column=0, padx=20, pady=20)

# Username and Info
username_label = tk.Label(profile_frame, text="CATINA.B", font=("Arial", 20, "bold"), bg="#F5F5F5")
username_label.grid(row=0, column=1, sticky="w")

username_info = tk.Label(profile_frame, text="Username: Catina.b", font=("Arial", 10), bg="#F5F5F5")
username_info.grid(row=1, column=1, sticky="w")

# Buttons for Modifying Profile
btn_edit_profile = create_rounded_button(profile_frame, "Modifier mon profile")
btn_edit_profile.grid(row=2, column=1, pady=(10, 0), sticky="w")

btn_edit_favorites = create_rounded_button(profile_frame, "Modifier mes categories favoris")
btn_edit_favorites.grid(row=3, column=1, pady=(10, 0), sticky="w")

# Favorite Categories Section
fav_categories_frame = tk.Frame(content_frame, bg="#F5F5F5")
fav_categories_frame.grid(row=2, column=0, sticky='ew', padx=20, pady=20)

fav_categories_label = tk.Label(fav_categories_frame, text="Categories Favoris", font=("Arial", 15, "bold"), bg="#F5F5F5")
fav_categories_label.grid(row=0, column=0, sticky="w")



root.mainloop()