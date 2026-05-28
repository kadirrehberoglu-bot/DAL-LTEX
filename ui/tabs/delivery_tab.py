#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İplik Hızı Sekmesi (Delivery Speed Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class DeliveryTab(QWidget):
    """
    İplik Hızı sekmesi.
    L = ni / (T/m) formülünü kullanır.
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
        title = QLabel("İplik Teslim Hızı (Delivery Speed)")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Input grup
        input_group = QGroupBox("Giriş Verileri")
        input_layout = QFormLayout()
        
        # İğ devri (RPM)
        self.spindle_rpm = QSpinBox()
        self.spindle_rpm.setRange(100, 20000)
        self.spindle_rpm.setValue(7500)
        input_layout.addRow("İğ Devri (RPM):", self.spindle_rpm)
        
        # Büküm (T/m)
        self.twist = QDoubleSpinBox()
        self.twist.setRange(0.1, 1000)
        self.twist.setValue(810)
        self.twist.setDecimals(2)
        input_layout.addRow("Büküm (T/m):", self.twist)
        
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)
        
        # Hesapla butonu
        calc_btn = QPushButton("Hesapla")
        calc_btn.clicked.connect(self.calculate)
        calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #00BCD4;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0097a7;
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
        İplik hızını hesapla.
        """
        try:
            rpm = self.spindle_rpm.value()
            twist = self.twist.value()
            
            if twist <= 0:
                raise ValueError("Büküm değeri sıfırdan büyük olmalıdır.")
            
            delivery_speed = self.calc.calculate_delivery_speed(rpm, twist)
            
            # Sonuçları göster
            results = {
                "İplik Hızı (m/dk)": f"{delivery_speed:.2f}",
                "İğ Devri (RPM)": str(rpm),
                "Büküm (T/m)": f"{twist:.2f}"
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
