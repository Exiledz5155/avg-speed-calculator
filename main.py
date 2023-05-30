from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, \
    QGridLayout, QLineEdit, QPushButton, QComboBox
import sys

class AvgSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance (km):")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_avg)
        self.output_label = QLabel("")

        self.units_dropdown = QComboBox()
        self.units_dropdown.addItems(['Metric (km)', 'Imperial (miles)'])

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.units_dropdown, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_avg(self):
        # Get distance and time from input
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        # Calculate avg
        speed = distance/time

        if self.units_dropdown.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.units_dropdown.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        # Display result
        self.output_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
avg_calculator = AvgSpeedCalculator()
avg_calculator.show()
sys.exit(app.exec())