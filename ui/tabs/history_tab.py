#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hesaplama Geçmişi Sekmesi (History Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from database.db_manager import DatabaseManager


class HistoryTab(QWidget):
    """
    Hesaplama geçmişini gösteren sekme.
    """
    
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.init_ui()
    
    def init_ui(self):
        """
        Arayüzü başlat.
        """
        layout = QVBoxLayout()
        
        # Başlık
        title = QFont("Arial", 14, QFont.Bold)
        
        # Tablo
        self.history_table = QTableWidget()
        self.history_table.setColumnCount(5)
        self.history_table.setHorizontalHeaderLabels(["Tarih", "Hesaplama Türü", "Giriş", "Çıkış", "Sonuç"])
        self.history_table.horizontalHeader().setStretchLastSection(True)
        
        layout.addWidget(self.history_table)
        
        # Temizle butonu
        clear_btn = QPushButton("Geçmişi Temizle")
        clear_btn.clicked.connect(self.clear_history)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        layout.addWidget(clear_btn)
        
        self.setLayout(layout)
        
        # Geçmişi yükle
        self.load_history()
    
    def load_history(self):
        """
        Veritabanından geçmişi yükle.
        """
        try:
            history = self.db.get_calculations_history()
            
            self.history_table.setRowCount(len(history))
            
            for row, calc in enumerate(history):
                self.history_table.setItem(row, 0, QTableWidgetItem(str(calc[1])))
                self.history_table.setItem(row, 1, QTableWidgetItem(calc[2]))
                self.history_table.setItem(row, 2, QTableWidgetItem(str(calc[3])))
                self.history_table.setItem(row, 3, QTableWidgetItem(str(calc[4])))
                self.history_table.setItem(row, 4, QTableWidgetItem(str(calc[5])))
        
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Geçmiş yüklenirken hata: {str(e)}")
    
    def clear_history(self):
        """
        Hesaplama geçmişini temizle.
        """
        reply = QMessageBox.question(self, "Onay", "Tüm geçmişi silmek istediğinize emin misiniz?")
        
        if reply == QMessageBox.Yes:
            try:
                self.db.clear_history()
                self.history_table.setRowCount(0)
                QMessageBox.information(self, "Başarılı", "Geçmiş temizlendi.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Geçmiş silinirken hata: {str(e)}")
