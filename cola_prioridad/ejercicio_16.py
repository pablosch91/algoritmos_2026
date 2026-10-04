# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

from heap import Heap

# La clase Heap guarda [prioridad, valor] al llamar a arrive(valor, prioridad).

cola_impresion = Heap()

# a
print("Cargando 3 documentos de empleados...")
cola_impresion.arrive("Reporte_Mensual_Empleado1.pdf", 1)
cola_impresion.arrive("Planilla_Horarios_Empleado2.docx", 1)
cola_impresion.arrive("Nota_Gastos_Empleado3.pdf", 1)
print("Documentos cargados correctamente")
print()

# b
doc = cola_impresion.attention()
if doc: # si la cola está vacía, no imprime nada
    print(doc[1])
print()

# c
print("Cargando 2 documentos del staff de TI...")
cola_impresion.arrive("Configuracion_Servidor_TI1.txt", 2)
cola_impresion.arrive("Parche_Seguridad_TI2.log", 2)
print("Documentos cargados correctamente")
print()

# d
print("Cargando 1 documento del gerente...")
cola_impresion.arrive("Balance_Anual_Gerente.pdf", 3)
print("Documento cargado correctamente")
print()

# e
print("Imprimiendo los dos primeros documentos de la cola")
for i in range(2):
    doc = cola_impresion.attention()
    if doc:
        print(doc[1])
print()

# f
print("Cargando 2 documentos de empleados y 1 de gerente...")
cola_impresion.arrive("Solicitud_Vacaciones_Empleado4.pdf", 1)
cola_impresion.arrive("Formulario_Reclamo_Empleado5.docx", 1)
cola_impresion.arrive("Presupuesto_Q4_Gerente.xlsx", 3)
print("Documentos cargados correctamente")
print()

# g
print("Imprimiendo todos los documentos restantes de la cola")
while cola_impresion.size() > 0:
    doc = cola_impresion.attention()
    if doc:
        print(doc[1])