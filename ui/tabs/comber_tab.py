#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tarama Hesabı Sekmesi (Comber Calculation Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class ComberTab(QWidget):
    """
    Tarama Hesabı sekmesi.
    Comber machine hesaplamalarını yapar.
    
    Formül: Tarama = [Çıkış ktex × (100 − Telef%) × Dublaj] / (100 × Giriş ktex)
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
        title = QLabel("Tarama Hesabı (Comber Calculation)")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Input grup
        input_group = QGroupBox("Giriş Verileri")
        input_layout = QFormLayout()
        
        # Çıkış ktex
        self.output_ktex = QDoubleSpinBox()
        self.output_ktex.setRange(0.1, 1000)
        self.output_ktex.setValue(14.6)
        self.output_ktex.setDecimals(2)
        input_layout.addRow("Çıkış ktex:", self.output_ktex)
        
        # Giriş ktex
        self.input_ktex = QDoubleSpinBox()
        self.input_ktex.setRange(0.1, 1000)
        self.input_ktex.setValue(28.8)
        self.input_ktex.setDecimals(2)
        input_layout.addRow("Giriş ktex:", self.input_ktex)
        
        # Telef yüzdesi
        self.waste_percent = QDoubleSpinBox()
        self.waste_percent.setRange(0, 100)
        self.waste_percent.setValue(15)
        self.waste_percent.setDecimals(2)
        self.waste_percent.setSuffix(" %")
        input_layout.addRow("Telef (%):", self.waste_percent)
        
        # Dublaj sayısı
        self.doubling = QSpinBox()
        self.doubling.setRange(1, 10)
        self.doubling.setValue(1)
        input_layout.addRow("Dublaj Sayısı:", self.doubling)
        
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)
        
        # Hesapla butonu
        calc_btn = QPushButton("Hesapla")
        calc_btn.clicked.connect(self.calculate)
        calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        left_layout.addWidget(calc_btn)
        
        left_layout.addStretch()
        
        # Sağ taraf - Output
        right_layout = QVBoxLayout()
        self.result_display = ResultDisplay()
        right_layout.addWidget(self.result_display)
        
        # Ana layout'a ekle
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(right_layout, 1)
        
        self.setLayout(main_layout)
    
    def calculate(self):
        """
        Tarama hesabını yap.
        """
        try:
            output_ktex = self.output_ktex.value()
            input_ktex = self.input_ktex.value()
            waste = self.waste_percent.value()
            doubling = self.doubling.value()
            
            if output_ktex <= 0 or input_ktex <= 0:
                raise ValueError("ktex değerleri sıfırdan büyük olmalıdır.")
            if waste < 0 or waste > 100:
                raise ValueError("Telef yüzdesi 0-100 arasında olmalıdır.")
            
            comber = self.calc.calculate_comber(output_ktex, waste, doubling, input_ktex)
            
            # Sonuçları göster
            results = {
                "Tarama Oranı": f"{comber:.4f}",
                "Çıkış ktex": f"{output_ktex:.2f}",
                "Giriş ktex": f"{input_ktex:.2f}",
                "Telef (%)": f"{waste:.2f}",
                "Dublaj Sayısı": str(doubling)
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
