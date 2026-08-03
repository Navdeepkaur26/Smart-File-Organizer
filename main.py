import customtkinter as ctk
from tkinter import filedialog, messagebox

from file_manager import organize_files

# ---------------- Appearance ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Window ---------------- #

app = ctk.CTk()

app.title("Smart File Organizer")

app.geometry("700x500")

app.resizable(False, False)

# ---------------- Title ---------------- #

title = ctk.CTkLabel(
    app,
    text="📂 Smart File Organizer",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)

# ---------------- Folder Path ---------------- #

folder_var = ctk.StringVar()

folder_entry = ctk.CTkEntry(
    app,
    width=500,
    textvariable=folder_var
)

folder_entry.pack(pady=10)

# ---------------- Browse ---------------- #

def browse_folder():

    folder = filedialog.askdirectory()

    if folder:
        folder_var.set(folder)

browse_btn = ctk.CTkButton(
    app,
    text="📁 Browse Folder",
    command=browse_folder,
    width=220
)

browse_btn.pack(pady=10)

# ---------------- Result Box ---------------- #

result_box = ctk.CTkTextbox(
    app,
    width=600,
    height=180
)

result_box.pack(pady=20)

# ---------------- Organize ---------------- #

def organize():

    folder = folder_var.get()

    if folder == "":
        messagebox.showerror(
            "Error",
            "Please select a folder!"
        )
        return

    summary = organize_files(folder)

    result_box.delete("1.0", "end")

    total = 0

    result_box.insert("end", "===== ORGANIZATION SUMMARY =====\n\n")

    for key, value in summary.items():

        total += value

        result_box.insert(
            "end",
            f"{key} : {value}\n"
        )

    result_box.insert(
        "end",
        f"\nTotal Files : {total}"
    )

    messagebox.showinfo(
        "Success",
        "Files Organized Successfully!"
    )

organize_btn = ctk.CTkButton(
    app,
    text="🚀 Organize Files",
    command=organize,
    width=220
)

organize_btn.pack(pady=10)

# ---------------- Run ---------------- #

app.mainloop()