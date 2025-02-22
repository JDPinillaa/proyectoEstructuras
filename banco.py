from datetime import date
from cuentaBancaria import CuentaBancaria
class Banco:
    numeroCuentas = 0
    def __init__(self, cuentasBanco):
        self.cuentasBanco = cuentasBanco
    def __init__(self):
        self.cuentasBanco = []
    def crearCuenta(self, titular, saldo_inicial):
        self.numeroCuentas += 1
        try:
            cuentaNueva = CuentaBancaria(titular, saldo_inicial, self.numeroCuentas)
        except ValueError as err:
            self.numeroCuentas -= 1
            raise err
        cuentaDict = dict()
        cuentaDict[cuentaNueva.getNumeroCuenta()] = cuentaNueva
        self.cuentasBanco.append(cuentaDict)
    def depositar(self, numero_cuenta, monto):
        for cuenta in self.cuentasBanco:
            if numero_cuenta in cuenta.keys():
                saldoActual = cuenta[numero_cuenta].getSaldo()
                saldoNuevo = saldoActual + monto
                cuenta[numero_cuenta].setSaldo(saldoNuevo)
                return
    def retirar(self, numero_cuenta, monto):
        for cuenta in self.cuentasBanco:
            if numero_cuenta in cuenta.keys():
                saldoActual = cuenta[numero_cuenta].getSaldo()
                if(monto > saldoActual):
                    print('MONTO A RETIRAR EXCEDIÓ SU SALDO')
                    return
                saldoNuevo = saldoActual - monto
                infoTransaccion = 'SE HA RETIRADO: {0}|{1}'.format(monto, date.today())
                cuenta[numero_cuenta].registrarTransaccion(infoTransaccion)
                cuenta[numero_cuenta].setSaldo(saldoNuevo)
                return
        for cuenta in self.cuentasBanco:
            if numero_cuenta in cuenta.keys():
                saldoActual = cuenta[numero_cuenta].getSaldo()
                if(monto > saldoActual):
                    print('MONTO A RETIRAR EXCEDIÓ SU SALDO')
                    return
                saldoNuevo = saldoActual - monto
                infoTransaccion = 'SE HA RETIRADO: {0}|{1}'.format(monto, date.today())
                cuenta[numero_cuenta].registrarTransaccion('')
                cuenta[numero_cuenta].setSaldo(saldoNuevo)
                return
    def consultarCuenta(self, numeroCuenta):
        for cuenta in self.cuentasBanco:
            if numeroCuenta in cuenta.keys():
                return cuenta[numeroCuenta]
        raise ValueError("CUENTA NO ENCONTRADA")
    def transferir(self, numCuentaOrigen, numCuentaDestino, monto):
        for cuenta in self.cuentasBanco:
            if numCuentaOrigen in cuenta.keys():
                cuentaOrigen = cuenta[numCuentaOrigen]
                saldoOrigen = cuentaOrigen.getSaldo()
            if numCuentaDestino in cuenta.keys():
                cuentaDestino = cuenta[numCuentaDestino]
                saldoDestino = cuentaDestino.getSaldo()
        if(monto > saldoOrigen):
            return
        nuevoSaldoOrigen = saldoOrigen - monto
        cuentaOrigen.setSaldo(nuevoSaldoOrigen)
        infOrigen = '${0} TRANSFERIDOS A: {1}|{2}'.format(monto,cuentaDestino.getNumeroCuenta(), date.today())
        cuentaOrigen.registrarTransaccion(infOrigen)
        nuevoSaldoDestino = saldoDestino + monto
        cuentaDestino.setSaldo(nuevoSaldoDestino)
        infDestino = '${0} RECIBIDOS DE: {1}|{2}'.format(monto, cuentaOrigen.getNumeroCuenta(), date.today())
        cuentaDestino.registrarTransaccion(infDestino)
    