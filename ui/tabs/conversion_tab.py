#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nm/ktex Dönüşümü Sekmesi (Unit Conversion Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class ConversionTab(QWidget):
    """
    Nm/ktex Dönüşümü sekmesi.
    ktex = 1 / Nm
    Nm = 1 / ktex
    """
    
    def __init__(self):
        super().__init__()
        self.calc = TextileCalculations()
        self.init_ui()
    
    def init_ui(self):
        """
        Arayüzü başlat.
        """
        main_layout = QHBoxLayout()
        
        # Sol taraf - Input
        left_layout = QVBoxLayout()
        
        # Başlık
        title = QLabel("Nm ↔ ktex Dönüşümü")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Nm grup
        nm_group = QGroupBox("Nm'den ktex'e")
        nm_layout = QFormLayout()
        
        self.nm_input = QDoubleSpinBox()
        self.nm_input.setRange(0.1, 1000)
        self.nm_input.setValue(32)
        self.nm_input.setDecimals(2)
        nm_layout.addRow("Nm:", self.nm_input)
        
        nm_group.setLayout(nm_layout)
        left_layout.addWidget(nm_group)
        
        nm_btn = QPushButton("Nm → ktex")
        nm_btn.clicked.connect(self.convert_nm_to_ktex)
        nm_btn.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7b1fa2;
            }
        """)
        left_layout.addWidget(nm_btn)
        
        left_layout.addSpacing(20)
        
        # ktex grup
        ktex_group = QGroupBox("ktex'ten Nm'ye")
        ktex_layout = QFormLayout()
        
        self.ktex_input = QDoubleSpinBox()
        self.ktex_input.setRange(0.001, 1000)
        self.ktex_input.setValue(31.25)
        self.ktex_input.setDecimals(4)
        ktex_layout.addRow("ktex:", self.ktex_input)
        
        ktex_group.setLayout(ktex_layout)
        left_layout.addWidget(ktex_group)
        
        ktex_btn = QPushButton("ktex → Nm")
        ktex_btn.clicked.connect(self.convert_ktex_to_nm)
        ktex_btn.setStyleSheet("""
            QPushButton {
                background-color: #F44336;
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
        left_layout.addWidget(ktex_btn)
        
        left_layout.addStretch()
        
        # Sağ taraf - Output
        right_layout = QVBoxLayout()
        self.result_display = ResultDisplay()
        right_layout.addWidget(self.result_display)
        
        # Ana layout'a ekle
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)
        
        self.setLayout(main_layout)
    
    def convert_nm_to_ktex(self):
        """
        Nm'yi ktex'e çevir.
        """
        try:
            nm = self.nm_input.value()
            
            if nm <= 0:
                raise ValueError("Nm değeri sıfırdan büyük olmalıdır.")
            
            ktex = self.calc.convert_count(nm, 'nm_to_ktex')
            
            results = {
                "Nm (Giriş)": f"{nm:.2f}",
                "ktex (Çıkış)": f"{ktex:.4f}"
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dönüşüm hatası: {str(e)}")
    
    def convert_ktex_to_nm(self):
        """
        ktex'i Nm'ye çevir.
        """
        try:
            ktex = self.ktex_input.value()
            
            if ktex <= 0:
                raise ValueError("ktex değeri sıfırdan büyük olmalıdır.")
            
            nm = self.calc.convert_count(ktex, 'ktex_to_nm')
            
            results = {
                "ktex (Giriş)": f"{ktex:.4f}",
                "Nm (Çıkış)": f"{nm:.2f}"
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dönüşüm hatası: {str(e)}")
