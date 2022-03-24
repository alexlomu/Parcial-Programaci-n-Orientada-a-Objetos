from datetime import date
class Banco:
    def __init__(self, ID, titular, fecha_apertura, fecha_vencimiento, numero_cuenta, saldo):
        self.ID = ID 
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.fecha_vencimiento = fecha_vencimiento
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def get_ID(self):
        return self.ID
    def get_titular(self):
        return self.titular
    def get_fecha_apertura(self):
        return self.fecha_apertura
    def get_fecha_vencimiento(self):
        return self.fecha_vencimiento
    def get_numero_cuenta(self):
        return self.numero_cuenta
    def get_saldo(self):
        return self.saldo
    

lista_cuentas =[]
class Cuentas:
    def crearcuenta():
        ID = int(input("Introduzca el ID de la cuenta: "))
        titular = input("Introduzca el titular de la cuenta:" )
        fecha_apertura = input("Introduzca la fecha de apertura de la cuenta de la siguiente manera |año, mes, dia|: ")
        fecha_vencimiento= input("Introduzca la fecha de apertura de la cuenta de la siguiente manera |año, mes, dia|: ")
        date(fecha_apertura)
        date(fecha_vencimiento)
        numero_cuenta = int(input("Introduzca el número de la cuenta: " ))
        saldo = int(input("Introduzca el saldo que tiene la cuenta: " ))
        if fecha_apertura < fecha_vencimiento and saldo >= 0:
            cuenta = Banco(ID, titular, fecha_apertura, fecha_vencimiento, numero_cuenta, saldo)
            lista_cuentas.append(cuenta)
    def crearcuenta_vip():
        ID = int(input("Introduzca el ID de la cuenta: "))
        titular = input("Introduzca el titular de la cuenta:" )
        fecha_apertura = input("Introduzca la fecha de apertura de la cuenta de la siguiente manera |año, mes, dia|: ")
        fecha_vencimiento= input("Introduzca la fecha de apertura de la cuenta de la siguiente manera |año, mes, dia|: ")
        date(fecha_apertura)
        date(fecha_vencimiento)
        numero_cuenta = int(input("Introduzca el número de la cuenta: " ))
        saldo = int(input("Introduzca el saldo que tiene la cuenta: " ))
        if fecha_apertura < fecha_vencimiento and saldo >= -1000:
            cuenta_vip = Banco(ID, titular, fecha_apertura, fecha_vencimiento, numero_cuenta, saldo)
            lista_cuentas.append(cuenta_vip)


    

class Operaciones:  
    global plazo_fijo
    global hoy

    plazo_fijo = date(2022, 8, 20)
    hoy = date.today()
    
    def deposit(self):
        cantidad = float(input("Introduce la cantidad a ingresar: "))
        if cantidad > 0:
            saldo =  saldo + cantidad
                 
    def retirar(self):
        cantidad = float(input("Introduce la cantidad a retirar: "))
        if cantidad > saldo:
            print ("Saldo insuficiente")
        elif plazo_fijo < hoy:
            saldo =  saldo - (cantidad*1.05)
        else:
            saldo -= cantidad
    def transferir(self):
        cantidad = float("Introduce la cantidad a transferir: ")
        if cantidad > saldo1:
            print ("Saldo insuficiente")
        else:
            saldo1 = saldo1 - cantidad
            saldo2 = saldo2 + cantidad
    



            


        


