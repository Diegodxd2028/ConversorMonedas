class ConversorMoneda:
    tasas_cambio = {
        ('USD', 'EUR'): 0.92,
        ('USD', 'JPY'): 152.16,
        ('USD', 'PEN'): 3.77,
        ('EUR', 'JPY'): 165.51,
        ('EUR', 'USD'): 1.09,
        ('EUR', 'PEN'): 4.12,
        ('JPY', 'USD'): 0.0066,
        ('JPY', 'EUR'): 0.0060,
        ('JPY', 'PEN'): 0.025,
        ('PEN', 'USD'): 0.27,
        ('PEN', 'EUR'): 0.24,
        ('PEN', 'JPY'): 40.38
    }

    def convertir(self, monto, moneda_origen, moneda_destino):
        if monto < 0:
            raise ValueError("El monto no puede ser negativo")
        if moneda_origen == moneda_destino:
            return monto
        try:
            tasa = self.tasas_cambio[(moneda_origen, moneda_destino)]
        except KeyError:
            raise ValueError("Moneda no válida")
        return monto * tasa
