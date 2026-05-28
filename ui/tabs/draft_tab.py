#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çekim Hesabı Sekmesi (Draft Calculation Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class DraftTab(QWidget):
    """
    Çekim Hesabı sekmesi.
    Nm veya ktex tabanlı çekim hesaplamaları yapar.
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
        title = QLabel("Çekim Hesabı (Draft Calculation)")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Input grup
        input_group = QGroupBox("Giriş Verileri")
        input_layout = QFormLayout()
        
        # Birim seçimi
        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Nm Tabanlı", "ktex Tabanlı"])
        self.unit_combo.currentTextChanged.connect(self.on_unit_changed)
        input_layout.addRow("Birim:", self.unit_combo)
        
        # Giriş numarası
        self.input_nm = QDoubleSpinBox()
        self.input_nm.setRange(0.1, 1000)
        self.input_nm.setValue(20)
        self.input_nm.setDecimals(2)
        input_layout.addRow("Giriş Nm:", self.input_nm)
        
        # Çıkış numarası
        self.output_nm = QDoubleSpinBox()
        self.output_nm.setRange(0.1, 1000)
        self.output_nm.setValue(40)
        self.output_nm.setDecimals(2)
        input_layout.addRow("Çıkış Nm:", self.output_nm)
        
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
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
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
    
    def on_unit_changed(self):
        """
        Birim değiştiğinde etiketleri güncelle.
        """
        if self.unit_combo.currentText() == "ktex Tabanlı":
            self.input_nm.setPrefix("")
            self.output_nm.setPrefix("")
        else:
            self.input_nm.setPrefix("")
            self.output_nm.setPrefix("")
    
    def calculate(self):
        """
        Çekim hesabını yap.
        """
        try:
            input_val = self.input_nm.value()
            output_val = self.output_nm.value()
            doubling = self.doubling.value()
            
            if input_val <= 0 or output_val <= 0:
                raise ValueError("Nm/ktex değerleri sıfırdan büyük olmalıdır.")
            
            draft = self.calc.calculate_draft(output_val, doubling, input_val)
            
            # Sonuçları göster
            results = {
                "Çekim Oranı": f"{draft:.4f}",
                "Giriş Numarası": f"{input_val:.2f}",
                "Çıkış Numarası": f"{output_val:.2f}",
                "Dublaj Sayısı": str(doubling)
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
