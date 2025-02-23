import os
import requests
import time
import json
import threading
from tkinter import Tk, filedialog, Button, Label, Entry, StringVar, Toplevel, messagebox, ttk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

class DownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Archive Downloader")
        self.root.geometry("630x400")

        self.cookies_file = StringVar()
        self.links_file = StringVar()
        self.html_file = StringVar()
        self.save_folder = StringVar()
        self.links_count = StringVar()

        self.load_last_used_paths()

        self.create_widgets()

    def create_widgets(self):
        Button(self.root, text="Wähle HTML Datei", command=self.select_html_file).grid(row=0, column=0, padx=10, pady=5)
        self.generate_links_button = Button(self.root, text="Erstelle Download Links", command=self.generate_links, state="disabled")
        Entry(self.root, textvariable=self.html_file, width=50).grid(row=0, column=1, padx=10, pady=5)
        self.generate_links_button.grid(row=1, column=0, padx=10, pady=5)
        Label(self.root, textvariable=self.links_count).grid(row=1, column=1, padx=10, pady=5, sticky="w")

        Button(self.root, text="Wähle Links Datei", command=self.select_links_file).grid(row=2, column=0, padx=10, pady=5)
        Entry(self.root, textvariable=self.links_file, width=50).grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        Button(self.root, text="Wähle Zielordner", command=self.select_save_folder).grid(row=3, column=0, padx=10, pady=5)
        Entry(self.root, textvariable=self.save_folder, width=50).grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        Button(self.root, text="Erstelle Login Datei", command=self.generate_cookies).grid(row=4, column=0, padx=10, pady=5)
        Button(self.root, text="Wähle Login Datei", command=self.select_cookies_file).grid(row=5, column=0, padx=10, pady=5)
        Entry(self.root, textvariable=self.cookies_file, width=50).grid(row=5, column=1, padx=10, pady=5)

        self.start_button = Button(self.root, text="Start Download", command=self.start_download, state="disabled")
        self.start_button.grid(row=6, column=0, columnspan=3, pady=20)

        self.update_start_button_state()

    def load_last_used_paths(self):
        if os.path.exists("last_used_paths.json"):
            with open("last_used_paths.json", 'r') as f:
                paths = json.load(f)
                self.cookies_file.set(paths.get("cookies_file", ""))
                self.links_file.set(paths.get("links_file", ""))
                self.html_file.set(paths.get("html_file", ""))
                self.save_folder.set(paths.get("save_folder", ""))

    def save_last_used_paths(self):
        with open("last_used_paths.json", 'w') as f:
            json.dump({
                "cookies_file": self.cookies_file.get(),
                "links_file": self.links_file.get(),
                "html_file": self.html_file.get(),
                "save_folder": self.save_folder.get()
            }, f)

    def generate_cookies(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://archive.org/account/login")
        while "archive.org/account/login" in driver.current_url:
            time.sleep(5)
        cookies = driver.get_cookies()
        with open("Login_Data.json", "w") as file:
            json.dump(cookies, file)
        driver.quit()
        self.cookies_file.set("Login_Data.json")
        self.save_last_used_paths()
        self.update_start_button_state()

    def select_cookies_file(self):
        file_path = filedialog.askopenfilename(title="Wähle die JSON-Datei mit Login-Data")
        if file_path:
            self.cookies_file.set(file_path)
            self.save_last_used_paths()
            self.update_start_button_state()

    def generate_links(self):
        file_path = self.html_file.get()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                links = soup.find_all('a', href=re.compile(r'\.7z$'))
                links = [link['href'] for link in links]
            output_file = "download_links.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                for link in links:
                    file.write(link + '\n')
            self.links_file.set(output_file)
            self.links_count.set(f"Anzahl der Links: {len(links)}")
            self.save_last_used_paths()
            self.update_start_button_state()

    def select_links_file(self):
        file_path = filedialog.askopenfilename(title="Wähle die Textdatei mit den Links")
        if file_path:
            self.links_file.set(file_path)
            self.save_last_used_paths()
            self.update_start_button_state()

    def select_html_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if file_path:
            self.html_file.set(file_path)
            self.save_last_used_paths()
            self.update_start_button_state()

    def select_save_folder(self):
        folder_path = filedialog.askdirectory(title="Wähle den Zielordner für die Downloads")
        if folder_path:
            self.save_folder.set(folder_path)
            self.save_last_used_paths()
            self.update_start_button_state()

    def update_start_button_state(self):
        if self.cookies_file.get() and self.links_file.get() and self.save_folder.get():
            self.start_button.config(state="normal")
        else:
            self.start_button.config(state="disabled")

        if self.html_file.get():
            self.generate_links_button.config(state="normal")
        else:
            self.generate_links_button.config(state="disabled")

    def start_download(self):
        self.root.withdraw()
        self.download_window = Toplevel(self.root)
        self.download_window.title("Download Progress")
        self.download_window.geometry("400x200")

        self.progress_label = Label(self.download_window, text="Download Progress")
        self.progress_label.pack(pady=10)

        self.file_label = Label(self.download_window, text="")
        self.file_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.download_window, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.pause_button = Button(self.download_window, text="Pause", command=self.pause_download)
        self.pause_button.pack(side="left", padx=10, pady=10)

        self.cancel_button = Button(self.download_window, text="Abbrechen", command=self.cancel_download)
        self.cancel_button.pack(side="right", padx=10, pady=10)

        self.download_window.protocol("WM_DELETE_WINDOW", self.cancel_download)  # Handle window close event

        self.download_thread = threading.Thread(target=self.download_files)
        self.download_thread.start()

    def pause_download(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Fortsetzen")
        else:
            self.pause_button.config(text="Pause")

    def cancel_download(self):
        self.cancelled = True

    def download_files(self):
        self.paused = False
        self.cancelled = False
        session = self.load_cookies(self.cookies_file.get())
        links = self.read_links(self.links_file.get())
        total_links = len(links)
        failed_links = []

        for index, link in enumerate(links, start=1):
            if self.cancelled:
                break
            while self.paused:
                time.sleep(1)
            self.file_label.config(text=f"Downloading: {os.path.basename(link)}")
            self.progress_label.config(text=f"Downloading {index}/{total_links}")
            self.download_window.update_idletasks()
            if not self.download_file(link, self.save_folder.get(), session, index, total_links):
                failed_links.append(link)

        self.download_window.destroy()
        if not self.cancelled:
            self.show_completion_window(total_links - len(failed_links), self.save_folder.get())
        else:
            self.root.quit()

    def show_completion_window(self, successful_downloads, save_folder):
        completion_window = Toplevel(self.root)
        completion_window.title("Download Completed")
        completion_window.geometry("400x200")

        Label(completion_window, text=f"Download-Prozess abgeschlossen!").pack(pady=10)
        Label(completion_window, text=f"Erfolgreich heruntergeladene Dateien: {successful_downloads}").pack(pady=10)
        Label(completion_window, text=f"Speicherort: {save_folder}").pack(pady=10)

        Button(completion_window, text="OK", command=self.root.quit).pack(side="left", padx=10, pady=10)
        Button(completion_window, text="Ordner öffnen", command=lambda: os.startfile(save_folder)).pack(side="right", padx=10, pady=10)

    def read_links(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]

    def load_cookies(self, cookies_file):
        try:
            with open(cookies_file, 'r') as f:
                cookies = json.load(f)
            session = requests.Session()
            for cookie in cookies:
                session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'], path=cookie['path'])
            return session
        except (json.JSONDecodeError, FileNotFoundError) as e:
            messagebox.showerror("Fehler", "Die ausgewählte Login-Datei ist ungültig oder nicht vorhanden.")
            return None

    def is_file_complete(self, file_path, expected_size):
        if not os.path.exists(file_path):
            return False
        actual_size = os.path.getsize(file_path)
        return actual_size == expected_size

    def download_file(self, url, save_folder, session, current_index, total_links):
        filename = os.path.join(save_folder, os.path.basename(url))
        attempt = 0
        retries = 3
        while attempt < retries:
            try:
                response = session.get(url, stream=True)
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                if self.is_file_complete(filename, total_size):
                    print(f"{filename} ist bereits vollständig heruntergeladen.")
                    return True
                elif os.path.exists(filename):
                    print(f"{filename} ist nur teilweise heruntergeladen.")
                downloaded_size = 0
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        while self.paused:
                            print("Download pausiert")
                            time.sleep(1)
                        if self.cancelled:
                            print("Download abgebrochen")
                            return False
                        if chunk:
                            f.write(chunk)
                            downloaded_size += len(chunk)
                            percent_complete = (downloaded_size / total_size) * 100 if total_size else 0
                            self.progress_bar['value'] = percent_complete
                            self.download_window.update_idletasks()
                            print(f"{os.path.basename(url)} {current_index}/{total_links} {percent_complete:.2f}%", end='\r')
                print(f"\nDownload erfolgreich: {filename}")
                return True
            except Exception as e:
                attempt += 1
                print(f"Fehler beim Download von {url}, Versuch {attempt}/{retries}: {e}")
                time.sleep(2)
        return False

if __name__ == "__main__":
    root = Tk()
    app = DownloaderApp(root)
    root.mainloop()
