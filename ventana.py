import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QGroupBox, QFormLayout)
from PyQt5.QtCore import Qt

class CalculadoraDescuentos(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Calculadora de Descuentos")
        self.setGeometry(100, 100, 500, 300)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout(central_widget)
        
        # Grupo para entrada de datos
        grupo_entrada = QGroupBox("Datos de Entrada")
        layout_form = QFormLayout()
        
        self.salario_edit = QLineEdit()
        self.salario_edit.setPlaceholderText("Ingrese el salario mensual")
        layout_form.addRow("Salario mensual ($):", self.salario_edit)
        
        grupo_entrada.setLayout(layout_form)
        layout.addWidget(grupo_entrada)
        
        # Grupo para resultados
        grupo_resultados = QGroupBox("Resultados")
        resultados_layout = QFormLayout()
        
        self.isss_label = QLabel("$0.00")
        self.afp_label = QLabel("$0.00")
        self.renta_label = QLabel("$0.00")
        self.total_descuentos_label = QLabel("$0.00")
        self.salario_neto_label = QLabel("$0.00")
        
        resultados_layout.addRow("Descuento ISSS:", self.isss_label)
        resultados_layout.addRow("Descuento AFP:", self.afp_label)
        resultados_layout.addRow("Descuento Renta:", self.renta_label)
        resultados_layout.addRow("Total descuentos:", self.total_descuentos_label)
        resultados_layout.addRow("Salario neto:", self.salario_neto_label)
        
        grupo_resultados.setLayout(resultados_layout)
        layout.addWidget(grupo_resultados)
        
        # Botones
        botones_layout = QHBoxLayout()
        
        self.calcular_btn = QPushButton("Calcular")
        self.limpiar_btn = QPushButton("Limpiar")
        
        self.calcular_btn.clicked.connect(self.calcular_descuentos)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)
        
        botones_layout.addWidget(self.calcular_btn)
        botones_layout.addWidget(self.limpiar_btn)
        
        layout.addLayout(botones_layout)
        
    def calcular_descuentos(self):
        try:
            salario = float(self.salario_edit.text())
            
            # Cálculo de descuentos
            # ISSS: 3% del salario, máximo $30 para salarios >= $1000
            isss = min(salario * 0.03, 30) if salario >= 1000 else salario * 0.03
            
            # AFP: 7.25% del salario
            afp = salario * 0.0725
            
            # Base para renta (salario - ISSS - AFP)
            base_renta = salario - isss - afp
            
            # Cálculo de renta 
            if base_renta <= 472.00:
                renta = 0
            elif base_renta <= 895.24:
                renta = (base_renta - 472.00) * 0.10 + 17.67
            elif base_renta <= 2038.10:
                renta = (base_renta - 895.24) * 0.20 + 60.00
            else:
                renta = (base_renta - 2038.10) * 0.30 + 288.57
            
            total_descuentos = isss + afp + renta
            salario_neto = salario - total_descuentos
            
            # Resultados
            self.isss_label.setText(f"${isss:.2f}")
            self.afp_label.setText(f"${afp:.2f}")
            self.renta_label.setText(f"${renta:.2f}")
            self.total_descuentos_label.setText(f"${total_descuentos:.2f}")
            self.salario_neto_label.setText(f"${salario_neto:.2f}")
            
        except ValueError:
            self.limpiar_campos()
            self.salario_neto_label.setText("Error: Ingrese un número válido")
    
    def limpiar_campos(self):
        self.salario_edit.clear()
        self.isss_label.setText("$0.00")
        self.afp_label.setText("$0.00")
        self.renta_label.setText("$0.00")
        self.total_descuentos_label.setText("$0.00")
        self.salario_neto_label.setText("$0.00")

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ventana = CalculadoraDescuentos()
    ventana.show()
    sys.exit(app.exec_())

