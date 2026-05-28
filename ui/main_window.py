#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ana Pencere (Main Window)

Tüm sekmeler ve işlevleri koordine eden ana pencere.
"""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget,
    QStatusBar, QMenuBar, QMenu, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from ui.tabs.draft_tab import DraftTab
from ui.tabs.comber_tab import ComberTab
from ui.tabs.twist_tab import TwistTab
from ui.tabs.conversion_tab import ConversionTab
from ui.tabs.delivery_tab import DeliveryTab
from ui.tabs.production_tab import ProductionTab
from ui.tabs.passage_tab import PassageTab
from ui.tabs.history_tab import HistoryTab


class MainWindow(QMainWindow):
    """
    Ana pencere sınıfı.
    Tüm hesaplama sekmelerini içerir.
    """
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DAL-LTEX - Tekstil Mühendisliği Hesaplama Sistemi")
        self.setGeometry(100, 100, 1200, 800)
        
        # Merkezi widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Tab widget oluştur
        self.tabs = QTabWidget()
        
        # Sekmeler ekle
        self.tabs.addTab(DraftTab(), "📊 Çekim Hesabı")
        self.tabs.addTab(ComberTab(), "🔍 Tarama Hesabı")
        self.tabs.addTab(TwistTab(), "🔄 Büküm Hesabı")
        self.tabs.addTab(DeliveryTab(), "⚡ İplik Hızı")
        self.tabs.addTab(ProductionTab(), "📈 Günlük Üretim")
        self.tabs.addTab(PassageTab(), "📋 Pasaj Çekim")
        self.tabs.addTab(ConversionTab(), "↔️ Nm/ktex Dönüşümü")
        self.tabs.addTab(HistoryTab(), "📚 Hesaplama Geçmişi")
        
        layout.addWidget(self.tabs)
        
        # Menü bar oluştur
        self.create_menu_bar()
        
        # Status bar
        self.statusBar().showMessage("Hazır")
    
    def create_menu_bar(self):
        """
        Menü barını oluştur.
        """
        menubar = self.menuBar()
        
        # Dosya menüsü
        file_menu = menubar.addMenu("Dosya")
        
        export_action = QAction("Dışa Aktar", self)
        export_action.triggered.connect(self.export_results)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Çıkış", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Yardım menüsü
        help_menu = menubar.addMenu("Yardım")
        
        about_action = QAction("Hakkında", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def export_results(self):
        """
        Sonuçları dışa aktar.
        """
        QMessageBox.information(self, "Bilgi", "Dışa aktarma özelliği gelecek versiyonda eklenecek.")
    
    def show_about(self):
        """
        Hakkında bilgisini göster.
        """
        about_text = """
        <h2>DAL-LTEX v1.0.0</h2>
        <p><b>Tekstil Mühendisliği Profesyonel Hesaplama Sistemi</b></p>
        <p>Bu program, tekstil üretim süreçlerinde kullanılan teknik hesaplamaları
        otomatik olarak yapmak için geliştirilmiştir.</p>
        <p><b>Geliştirici:</b> Kadir Rehberoglu Bot</p>
        <p><b>Lisans:</b> MIT</p>
        <p><b>Python 3.10+ | PySide6</b></p>
        """
        QMessageBox.about(self, "DAL-LTEX Hakkında", about_text)
