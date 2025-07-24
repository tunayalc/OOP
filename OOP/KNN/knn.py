import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

# KNN sınıflandırıcı GUI uygulaması
class KNNApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KNN Sınıflandırıcı GUI")
        self.root.geometry("1024x720")
        
        # Ana çerçeve için Canvas ve Scrollbar
        self.canvas = tk.Canvas(self.root)
        self.scroll_y = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scroll_x = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        
        # Kaydırılabilir ana çerçeve
        self.main_frame = ttk.Frame(self.canvas)
        self.main_frame.bind("<Configure>", self.update_scrollregion)
        
        # Canvas içine ana çerçeveyi yerleştir
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        
        # Canvas ayarları
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        
        # Kaydırma çubuklarını yerleştir
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.scroll_x.grid(row=1, column=0, sticky="ew")
        
        # Ana pencerenin genişleme durumunu yönet
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # GUI bileşenlerini oluştur
        self.create_widgets()
    
    def update_scrollregion(self, event=None):
        """Canvas scroll region ayarlarını günceller."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def create_widgets(self):
        # Başlık etiketi
        title_label = ttk.Label(self.main_frame, text="KNN Sınıflandırıcı", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # K değeri girişi
        ttk.Label(self.main_frame, text="K değeri girin:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.k_entry = ttk.Entry(self.main_frame)
        self.k_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Özellik girişi
        feature_label = ttk.Label(self.main_frame, text="Özellik Vektörlerini ve Etiketleri girin (virgülle ayrılmış):")
        feature_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        self.feature_frame = ttk.Frame(self.main_frame)
        self.feature_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.feature_entries = []
        self.label_entries = []
        
        self.add_feature_row()  # İlk satırı ekle
        
        # Yeni özellik satırı eklemek için buton
        self.add_feature_button = ttk.Button(self.main_frame, text="Yeni Özellik Satırı Ekle", command=self.add_feature_row)
        self.add_feature_button.grid(row=4, column=0, columnspan=3, pady=10)
        
        # Tahmin edilecek değerin girişi
        ttk.Label(self.main_frame, text="Tahmin edilecek Değer (virgülle ayrılmış):").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.predict_entry = ttk.Entry(self.main_frame, width=20)
        self.predict_entry.grid(row=5, column=1, padx=5, pady=5)
        
        # Tahmin butonu
        self.predict_button = ttk.Button(self.main_frame, text="Tahmin Et", command=self.predict)
        self.predict_button.grid(row=6, column=0, columnspan=3, pady=10)
        
        # Sonuç etiketi
        self.result_label = ttk.Label(self.main_frame, text="Tahmin Sonucu: ", font=("Helvetica", 12))
        self.result_label.grid(row=7, column=0, columnspan=3, pady=10)
        
        # En yakın komşular etiketi
        self.neighbors_label = ttk.Label(self.main_frame, text="En Yakın Komşular: ", font=("Helvetica", 12))
        self.neighbors_label.grid(row=8, column=0, columnspan=3, pady=10)

    def add_feature_row(self):
        row = len(self.feature_entries)
        feature_entry = ttk.Entry(self.feature_frame, width=20)
        feature_entry.grid(row=row, column=0, padx=5, pady=5)
        label_entry = ttk.Entry(self.feature_frame, width=10)
        label_entry.grid(row=row, column=1, padx=5, pady=5)
        
        self.feature_entries.append(feature_entry)
        self.label_entries.append(label_entry)

    def predict(self):
        pass  # Tahmin işlevselliği buraya eklenebilir

# Ana program çalıştırma
if __name__ == "__main__":
    root = tk.Tk()
    app = KNNApp(root)
    root.mainloop()