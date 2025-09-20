#import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

#Acción del botón
def mensaje():
    texto = entradat.text()
    QMessageBox.information(ventana,"Mensaje",texto)

app = QApplication(sys.argv)
ventana = QWidget()

#Propiedades de una ventana
ventana.setWindowTitle("Mi primera ventana")
ventana.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout()
label = QLabel("Este es un texto")
entradat = QLineEdit()

boton = QPushButton("Haz clic aquí")
boton.clicked.connect(mensaje)
#boton.setGeometry(100,80,100,20)
#boton.clicked.connect()

layout.addWidget(label)
layout.addWidget(entradat)
layout.addWidget(boton)
ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())


#import PyQt5
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget,
                             QPushButton,QVBoxLayout,QLineEdit,
                             QMessageBox)
import sys

#Acción del botón
def mensaje():
    n1 = float(enum1.text())
    n2 = float(enum2.text())
    resultado = n1+n2
    QMessageBox.information(ventana,"Resultado",f"El resultado es: {resultado}")

app = QApplication(sys.argv)
ventana = QWidget()

#Propiedades de una ventana
ventana.setWindowTitle("Suma de dos números")
ventana.setGeometry(100, 100, 300, 200)

layout = QVBoxLayout()
label = QLabel("Ingresa dos números y súmalos")

enum1 = QLineEdit()
enum2 = QLineEdit()

boton = QPushButton("Sumar")
boton.clicked.connect(mensaje)
#boton.setGeometry(100,80,100,20)
#boton.clicked.connect()

#layout.addWidget(label)
#layout.addWidget(enum1)
#layout.addWidget(enum2)
#layout.addWidget(boton)

widgets = [label,enum1,enum2,boton]
for w in widgets:
    layout.addWidget(w)

ventana.setLayout(layout)
ventana.show()
sys.exit(app.exec_())

