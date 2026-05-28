#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Günlük Üretim Sekmesi (Daily Production Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox
)
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class ProductionTab(QWidget):
    """
    Günlük Üretim sekmesi.
    Formül: Günlük Üretim = (m/dk × 60 × 24 × verim × iğ sayısı) / (1000 × Nm)
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
        title = QLabel("Günlük Üretim Hesabı")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        left_layout.addWidget(title)
        
        # Input grup
        input_group = QGroupBox("Giriş Verileri")
        input_layout = QFormLayout()
        
        # Makine hızı (m/dk)
        self.machine_speed = QDoubleSpinBox()
        self.machine_speed.setRange(1, 10000)
        self.machine_speed.setValue(100)
        self.machine_speed.setDecimals(2)
        input_layout.addRow("Makine Hızı (m/dk):", self.machine_speed)
        
        # Verim
        self.efficiency = QDoubleSpinBox()
        self.efficiency.setRange(0, 100)
        self.efficiency.setValue(90)
        self.efficiency.setDecimals(2)
        self.efficiency.setSuffix(" %")
        input_layout.addRow("Verim (%):", self.efficiency)
        
        # İğ sayısı
        self.spindle_count = QSpinBox()
        self.spindle_count.setRange(1, 10000)
        self.spindle_count.setValue(1000)
        input_layout.addRow("İğ Sayısı:", self.spindle_count)
        
        # Nm
        self.nm_value = QDoubleSpinBox()
        self.nm_value.setRange(0.1, 1000)
        self.nm_value.setValue(32)
        self.nm_value.setDecimals(2)
        input_layout.addRow("Nm:", self.nm_value)
        
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
    
    def calculate(self):
        """
        Günlük üretimi hesapla.
        """
        try:
            speed = self.machine_speed.value()
            efficiency = self.efficiency.value() / 100
            spindles = self.spindle_count.value()
            nm = self.nm_value.value()
            
            if nm <= 0:
                raise ValueError("Nm değeri sıfırdan büyük olmalıdır.")
            if efficiency < 0 or efficiency > 1:
                raise ValueError("Verim 0-100% arasında olmalıdır.")
            
            daily_prod = self.calc.calculate_daily_production(speed, efficiency, spindles, nm)
            
            # Sonuçları göster
            results = {
                "Günlük Üretim (kg/gün)": f"{daily_prod:.2f}",
                "Makine Hızı (m/dk)": f"{speed:.2f}",
                "Verim (%)": f"{efficiency*100:.2f}",
                "İğ Sayısı": str(spindles),
                "Nm": f"{nm:.2f}"
            }
            
            self.result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
