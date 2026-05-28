#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pasaj Çekim Sekmesi (Passage Draft Tab)
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QMessageBox, QTabWidget
)
from PySide6.QtGui import QFont
from services.textile_calculations import TextileCalculations
from ui.widgets.result_display import ResultDisplay


class PassageTab(QWidget):
    """
    Pasaj Çekim sekmesi.
    1., 2. ve 3. pasaj hesaplamalarını yapar.
    """
    
    def __init__(self):
        super().__init__()
        self.calc = TextileCalculations()
        self.init_ui()
    
    def init_ui(self):
        """
        Arayüzü başlat.
        """
        main_layout = QVBoxLayout()
        
        # Başlık
        title = QLabel("Pasaj Çekim Hesapları")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        main_layout.addWidget(title)
        
        # Tab widget
        passages = QTabWidget()
        
        # 1. Pasaj
        passages.addTab(self.create_passage_tab(1), "1. Pasaj")
        
        # 2. Pasaj
        passages.addTab(self.create_passage_tab(2), "2. Pasaj")
        
        # 3. Pasaj
        passages.addTab(self.create_passage_tab(3), "3. Pasaj")
        
        main_layout.addWidget(passages)
        
        self.setLayout(main_layout)
    
    def create_passage_tab(self, passage_num: int) -> QWidget:
        """
        Pasaj sekmesi oluştur.
        """
        widget = QWidget()
        layout = QHBoxLayout()
        
        # Sol taraf - Input
        left_layout = QVBoxLayout()
        
        input_group = QGroupBox(f"{passage_num}. Pasaj Giriş Verileri")
        input_layout = QFormLayout()
        
        # Giriş
        input_spinbox = QDoubleSpinBox()
        input_spinbox.setRange(0.1, 1000)
        input_spinbox.setValue(20)
        input_spinbox.setDecimals(2)
        input_spinbox.setObjectName(f"input_p{passage_num}")
        input_layout.addRow(f"Giriş Nm:", input_spinbox)
        
        # Çıkış
        output_spinbox = QDoubleSpinBox()
        output_spinbox.setRange(0.1, 1000)
        output_spinbox.setValue(40)
        output_spinbox.setDecimals(2)
        output_spinbox.setObjectName(f"output_p{passage_num}")
        input_layout.addRow(f"Çıkış Nm:", output_spinbox)
        
        # Dublaj
        doubling_spinbox = QSpinBox()
        doubling_spinbox.setRange(1, 10)
        doubling_spinbox.setValue(1)
        doubling_spinbox.setObjectName(f"doubling_p{passage_num}")
        input_layout.addRow(f"Dublaj Sayısı:", doubling_spinbox)
        
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)
        
        # Hesapla butonu
        calc_btn = QPushButton("Hesapla")
        calc_btn.clicked.connect(lambda: self.calculate_passage(passage_num, input_spinbox, output_spinbox, doubling_spinbox))
        calc_btn.setStyleSheet("""
            QPushButton {
                background-color: #673AB7;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #512da8;
            }
        """)
        left_layout.addWidget(calc_btn)
        left_layout.addStretch()
        
        # Sağ taraf - Output
        right_layout = QVBoxLayout()
        result_display = ResultDisplay()
        result_display.setObjectName(f"result_p{passage_num}")
        right_layout.addWidget(result_display)
        
        # Ana layout'a ekle
        layout.addLayout(left_layout, 1)
        layout.addLayout(right_layout, 1)
        
        widget.setLayout(layout)
        return widget
    
    def calculate_passage(self, passage_num, input_spinbox, output_spinbox, doubling_spinbox):
        """
        Pasaj çekim hesabını yap.
        """
        try:
            input_val = input_spinbox.value()
            output_val = output_spinbox.value()
            doubling = doubling_spinbox.value()
            
            if input_val <= 0 or output_val <= 0:
                raise ValueError("Nm/ktex değerleri sıfırdan büyük olmalıdır.")
            
            draft = self.calc.calculate_draft(output_val, doubling, input_val)
            
            results = {
                f"{passage_num}. Pasaj Çekim": f"{draft:.4f}",
                "Giriş Nm": f"{input_val:.2f}",
                "Çıkış Nm": f"{output_val:.2f}",
                "Dublaj": str(doubling)
            }
            
            # Find the result display widget
            result_display = self.findChild(ResultDisplay, f"result_p{passage_num}")
            if result_display:
                result_display.display_results(results)
            
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Hesaplama hatası: {str(e)}")
