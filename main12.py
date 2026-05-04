import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

FAV_FILE = "favorites.json"

# Загрузка избранных
def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r") as f:
            return json.load(f)
    return []

# Сохранение избранных
def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f, indent=4)

favorites = load_favorites()

# Поиск пользователей
def search_users():
    query = entry.get().strip()
    
    if not query:
        messagebox.showerror("Ошибка", "Поле поиска не должно быть пустым")
        return
    
    listbox.delete(0, tk.END)

    url = f"https://api.github.com/search/users?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for user in data["items"]:
            listbox.insert(tk.END, user["login"])
    else:
        messagebox.showerror("Ошибка", "Ошибка запроса к GitHub API")

# Добавление в избранное
def add_to_favorites():
    selected = listbox.curselection()
    if not selected:
        return
    
    user = listbox.get(selected)
    
    if user not in favorites:
        favorites.append(user)
        save_favorites(favorites)
        messagebox.showinfo("Успех", f"{user} добавлен в избранное")

# Просмотр избранного
def show_favorites():
    listbox.delete(0, tk.END)
    for user in favorites:
        listbox.insert(tk.END, user)

# GUI
root = tk.Tk()
root.title("GitHub User Finder")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

search_btn = tk.Button(root, text="Поиск", command=search_users)
search_btn.pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

fav_btn = tk.Button(root, text="Добавить в избранное", command=add_to_favorites)
fav_btn.pack()

show_fav_btn = tk.Button(root, text="Показать избранное", command=show_favorites)
show_fav_btn.pack()

root.mainloop()
