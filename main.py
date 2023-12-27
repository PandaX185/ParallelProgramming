import data_sharing
import race_condition
import synchronization
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def data_btn_click():
    print("Data sharing test")
    data_sharing.perform_operations()

def race_btn_click():
    print("Race condition test")
    race_condition.perform_transactions()

def sync_btn_click():
    print("Synchronization condition test")
    synchronization.perform_transactions()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Parallel Programming")

    layout = QVBoxLayout()

    label = QLabel("Welcome to this simple program to demonstrate some parallel execution tasks")
    layout.addWidget(label)

    data_btn = QPushButton("Try data sharing")
    data_btn.clicked.connect(data_btn_click)

    race_btn = QPushButton("Try race conditions")
    race_btn.clicked.connect(race_btn_click)

    sync_btn = QPushButton("Try synchronization")
    sync_btn.clicked.connect(sync_btn_click)

    layout.addWidget(data_btn)
    layout.addWidget(race_btn)
    layout.addWidget(sync_btn)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())