#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DAL-LTEX: Tekstil Mühendisliği Profesyonel Hesaplama Sistemi
Main Application Entry Point

Author: Kadir Rehberoglu Bot
Version: 1.0.0
Date: 2026
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLocale, QTranslator
from ui.main_window import MainWindow
from database.db_manager import DatabaseManager


def main():
    """
    Ana uygulama fonksiyonu.
    QApplication'ı başlatır ve MainWindow'u gösterir.
    """
    app = QApplication(sys.argv)
    
    # Veritabanını başlat
    db = DatabaseManager()
    db.initialize()
    
    # Ana pencereyi oluştur ve göster
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
