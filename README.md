# Programacion_PyQt5
Actividad Sumativa - Semana 8

# Integrantes:
Brayan Audiel Chavarría Romero - SMSS020924                                                                  
Esmeralda Isabel Cruz Roldán   - SMSS011124

# Problemática:
En El Salvador, los trabajadores asalariados están sujetos a tres descuentos obligatorios sobre su salario: el aporte al Instituto Salvadoreño del Seguro Social (ISSS), la cotización a la Administradora de Fondos de Pensiones (AFP) y el impuesto sobre la renta. Cada uno de estos descuentos tiene reglas de cálculo diferentes y complejas:

ISSS: 3% del salario con un tope máximo de $30 mensuales para salarios iguales o superiores a $1000  
AFP: 7.25% del salario sin tope máximo  
Renta: Se calcula por tramos progresivos con porcentajes que van del 10% al 30%

Los trabajadores frecuentemente tienen dificultades para calcular manualmente estos descuentos, especialmente el impuesto sobre la renta que requiere realizar múltiples operaciones matemáticas según diferentes tramos salariales. Esto genera incertidumbre sobre el monto exacto que recibirán neto cada mes y dificulta la planificación financiera personal.

# Solución:
Se desarrolló una aplicación con interfaz gráfica utilizando PyQt5 que automatiza el cálculo de los tres descuentos obligatorios. La aplicación permite a los usuarios ingresar su salario y obtiene instantáneamente el desglose detallado de cada descuento, el total de deducciones y el salario neto resultante.

# DATOS DE ENTRADA:
Salario mensual ($): Valor numérico del salario

# RESULTADOS MOSTRADOS:
Descuento ISSS: Monto del seguro social  
Descuento AFP: Monto del fondo de pensiones  
Descuento Renta: Monto del impuesto sobre la renta  
Total descuentos: Suma de los tres descuentos  
Salario neto: Monto final a recibir  
