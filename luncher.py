
import tkinter as tk
from tkinter import ttk
import minecraft_launcher_lib
import subprocess
import os

window = tk.Tk()
window.title("Minecraft Launcher")
window.geometry("500x500")

minecraft_directory = "C:\\.....\\.minecraft"

# --------------------------------------------------
# Create username file if missing
# --------------------------------------------------

if not os.path.exists("offline_username.txt"):
    with open("offline_username.txt", "w") as file:
        file.write("")

# --------------------------------------------------
# Load Offline Usernames
# --------------------------------------------------

offline_username = []

with open("offline_username.txt", "r") as file:
    offline_user = file.readlines()

    for name in offline_user:
        clean_name = name.strip()

        if clean_name != "":
            offline_username.append(clean_name)

# --------------------------------------------------
# Load Mod Loaders
# --------------------------------------------------

loader_ids = minecraft_launcher_lib.mod_loader.list_mod_loader()
loader_names = []

for current_id in loader_ids:
    loader_name = minecraft_launcher_lib.mod_loader.get_mod_loader(current_id).get_name()
    loader_names.append(loader_name)

# --------------------------------------------------
# Functions
# --------------------------------------------------

def update_versions(event=None):
    selected_loader_name = mod_loader_entry.get()

    if selected_loader_name == "":
        return

    loader_index = loader_names.index(selected_loader_name)
    loader_id = loader_ids[loader_index]

    selected_loader = minecraft_launcher_lib.mod_loader.get_mod_loader(loader_id)

    versions = selected_loader.get_minecraft_versions(True)

    version_names = []

    for version in versions:
        version_names.append(str(version))

    version_entry["values"] = version_names


def update_start_button(event=None):
    offline_user = Off_acc_entry.get().strip()
    microsoft_user = On_acc_entry.get().strip()

    if offline_user != "" or microsoft_user != "":
        start_button.config(state="normal")
    else:
        start_button.config(state="disabled")


def save_offline_username():
    username = username_entry.get().strip()

    if username == "":
        return

    if username not in offline_username:
        offline_username.append(username)

        with open("offline_username.txt", "w") as file:
            for name in offline_username:
                file.write(name + "\n")

    Off_acc_entry["values"] = offline_username
    Off_acc_entry.set(username)

    update_start_button()

    show_main_frame()


def start_minecraft():
    selected_loader_name = mod_loader_entry.get()
    selected_version = version_entry.get()

    if selected_loader_name == "" or selected_version == "":
        print("Please select loader and version")
        return

    loader_index = loader_names.index(selected_loader_name)
    loader_id = loader_ids[loader_index]

    selected_loader = minecraft_launcher_lib.mod_loader.get_mod_loader(loader_id)

    print("Installing mod loader...")

    installed_version = selected_loader.install(
        selected_version,
        minecraft_directory,
        callback={"setStatus": print}
    )

    username = Off_acc_entry.get().strip()

    options = {
        "username": username,
        "uuid": "",
        "token": ""
    }

    command = minecraft_launcher_lib.command.get_minecraft_command(
        installed_version,
        minecraft_directory,
        options
    )

    print("Launching Minecraft...")

    subprocess.Popen(command, cwd=minecraft_directory)


# --------------------------------------------------
# Frame Switch Functions
# --------------------------------------------------

def show_microsoft_frame():
    main_frame.pack_forget()
    login_frame.pack_forget()
    offline_frame.pack_forget()

    microsoft_frame.pack(fill="both", expand=True)


def show_offline_frame():
    main_frame.pack_forget()
    login_frame.pack_forget()
    microsoft_frame.pack_forget()

    offline_frame.pack(fill="both", expand=True)


def show_login_frame():
    main_frame.pack_forget()
    microsoft_frame.pack_forget()
    offline_frame.pack_forget()

    login_frame.pack(fill="both", expand=True)


def show_main_frame():
    login_frame.pack_forget()
    microsoft_frame.pack_forget()
    offline_frame.pack_forget()

    main_frame.pack(fill="both", expand=True)


# --------------------------------------------------
# Main Screen
# --------------------------------------------------

main_frame = tk.Frame(window, bg="cyan")

main_label = tk.Label(
    main_frame,
    text="Welcome to Minecraft Launcher",
    font=("Arial", 24, "bold"),
    bg="lightcyan",
    fg="darkcyan"
)
main_label.pack(pady=30)

Off_acclabkel = tk.Label(
    main_frame,
    text="Offline Account:-",
    font=("Arial", 14, "bold"),
    fg="blue"
)
Off_acclabkel.pack(pady=5)

Off_acc_entry = ttk.Combobox(
    main_frame,
    font=("Arial", 14, "bold"),
    values=offline_username
)
Off_acc_entry.pack()
Off_acc_entry.bind("<<ComboboxSelected>>", update_start_button)

On_acclabkel = tk.Label(
    main_frame,
    text="Microsoft Account:-",
    font=("Arial", 14, "bold"),
    fg="blue"
)
On_acclabkel.pack(pady=5)

On_acc_entry = ttk.Combobox(
    main_frame,
    font=("Arial", 14, "bold"),
    values=[]
)
On_acc_entry.pack()

mod_loader_label = tk.Label(
    main_frame,
    text="Mod Loader:-",
    font=("Arial", 14, "bold"),
    fg="blue"
)
mod_loader_label.pack(pady=5)

mod_loader_entry = ttk.Combobox(
    main_frame,
    font=("Arial", 14, "bold"),
    values=loader_names
)
mod_loader_entry.pack()
mod_loader_entry.bind("<<ComboboxSelected>>", update_versions)

version_label = tk.Label(
    main_frame,
    text="Minecraft Version:-",
    font=("Arial", 14, "bold"),
    fg="blue"
)
version_label.pack(pady=5)

version_entry = ttk.Combobox(
    main_frame,
    font=("Arial", 14, "bold")
)
version_entry.pack()

start_button = tk.Button(
    main_frame,
    text="Start Minecraft",
    state="disabled",
    command=start_minecraft
)
start_button.pack(pady=20)
login_button = tk.Button(
    main_frame,
    text="Login",
    command=show_login_frame
)
login_button.pack(pady=10)

# --------------------------------------------------
# Login Screen
# --------------------------------------------------

login_frame = tk.Frame(window, bg="gray")

username_label = tk.Label(
    login_frame,
    text="Login",
    font=("Arial", 24, "bold"),
    bg="green",
    fg="white"
)
username_label.pack(pady=70)

on_button = tk.Button(
    login_frame,
    text="Microsoft",
    command=show_microsoft_frame
)
on_button.pack(pady=25)

off_button = tk.Button(
    login_frame,
    text="Offline",
    command=show_offline_frame
)
off_button.pack(pady=25)

# --------------------------------------------------
# Microsoft Screen
# --------------------------------------------------

microsoft_frame = tk.Frame(window, bg="lightgreen")

microsoft_label = tk.Label(
    microsoft_frame,
    text="Microsoft Login",
    font=("Arial", 24, "bold"),
    bg="green",
    fg="white"
)
microsoft_label.pack(pady=70)

cslabel = tk.Label(
    microsoft_frame,
    text="Coming Soon...",
    font=("Arial", 14, "bold"),
    fg="red"
)
cslabel.pack(pady=70)

back_button = tk.Button(
    microsoft_frame,
    text="Back",
    command=show_login_frame
)
back_button.pack(pady=10)

# --------------------------------------------------
# Offline Screen
# --------------------------------------------------

offline_frame = tk.Frame(window, bg="lightblue")

offline_label = tk.Label(
    offline_frame,
    text="Offline Login",
    font=("Arial", 24, "bold"),
    bg="blue",
    fg="white"
)
offline_label.pack(pady=70)

username_entry = tk.Entry(
    offline_frame,
    font=("Arial", 14, "bold"),
    width=30
)
username_entry.pack(pady=70)

username_save_button = tk.Button(
    offline_frame,
    text="Login",
    font=("Arial", 14, "bold"),
    command=save_offline_username
)
username_save_button.pack(pady=10)

back_button = tk.Button(
    offline_frame,
    text="Back",
    command=show_login_frame
)
back_button.pack(pady=10)

# --------------------------------------------------
# Start UI
# --------------------------------------------------

show_main_frame()

window.mainloop()

