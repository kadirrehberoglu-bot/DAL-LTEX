#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonuç Gösterimi Widget'ı
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class ResultDisplay(QWidget):
    """
    Hesaplama sonuçlarını gösteren widget.
    """
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """
        Arayüzü başlat.
        """
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Başlık
        title = QLabel("Sonuçlar")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        self.layout.addWidget(title)
        
        # İçeriği başlat
        self.results_label = QLabel("Hesaplama yapılmamış.")
        self.results_label.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ddd;
            }
        """)
        self.layout.addWidget(self.results_label)
        
        self.layout.addStretch()
    
    def display_results(self, results: dict):
        """
        Sonuçları göster.
        
        Args:
            results: Sonuçlar sözlüğü
        """
        html = "<table style='width:100%;'>"
        
        for key, value in results.items():
            html += f"<tr><td style='font-weight:bold;padding:5px;'>{key}:</td><td style='padding:5px;'>{value}</td></tr>"
        
        html += "</table>"
        
        self.results_label.setText(html)
