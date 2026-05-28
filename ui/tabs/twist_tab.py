#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Büküm Hesabı Sekmesi (Twist Calculation Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class TwistTab(QWidget):
    """
    Büküm Hesabı sekmesi.
    T/m = αm × √Nm formülünü kullanır.
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
        title = QLabel("Büküm Hesabı (Twist Calculation)")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Input grup
        input_group = QGroupBox("Giriş Verileri")
        input_layout = QFormLayout()
        
        # Nm değeri
        self.nm_value = QDoubleSpinBox()
        self.nm_value.setRange(0.1, 1000)
        self.nm_value.setValue(32)
        self.nm_value.setDecimals(2)
        input_layout.addRow("Nm:", self.nm_value)
        
        # Alpha_m katsayısı
        self.alpha_m = QDoubleSpinBox()
        self.alpha_m.setRange(0, 200)
        self.alpha_m.setValue(90)
        self.alpha_m.setDecimals(2)
        input_layout.addRow("αm Katsayısı:", self.alpha_m)
        
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)
        
        # Hesapla butonu
        calc_btn = QPushButton("Hesapla")
        calc_btn.clicked.connect(self.calculate)
        calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e68900;
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
        Büküm hesabını yap.
        """
        try:
            nm = self.nm_value.value()
            alpha_m = self.alpha_m.value()
            
            if nm <= 0:
                raise ValueError("Nm değeri sıfırdan büyük olmalıdır.")
            if alpha_m < 0:
                raise ValueError("αm katsayısı negatif olamaz.")
            
            twist = self.calc.calculate_twist(alpha_m, nm)
            
            # Sonuçları göster
            results = {
                "Büküm (T/m)": f"{twist:.4f}",
                "Nm": f"{nm:.2f}",
                "αm Katsayısı": f"{alpha_m:.2f}",
                "√Nm": f"{nm**0.5:.4f}"
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
