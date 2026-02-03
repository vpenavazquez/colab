class StockInsuficienteError(Exception):
    pass


class SinDineroError(Exception):
    pass


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_stock(self, cantidad_deseada):
        if cantidad_deseada > self.stock:
            raise StockInsuficienteError(f"No hay stock suficiente de {self.nombre}. Quedan {self.stock}.")

    def restar_stock(self, cantidad):
        self.stock -= cantidad

    def __str__(self):
        return f"{self.nombre} ({self.precio}€) | Stock: {self.stock}"


class Cliente:
    def __init__(self, nombre, dinero_disponible):
        self.nombre = nombre
        self.dinero_disponible = dinero_disponible

    def comprar(self, producto, cantidad):
        coste_total = producto.precio * cantidad

        if coste_total > self.dinero_disponible:
            raise SinDineroError(
                f"No tienes dinero suficiente. Cuesta {coste_total}€ y tienes {self.dinero_disponible}€")

        producto.verificar_stock(cantidad)

        self.dinero_disponible -= coste_total
        producto.restar_stock(cantidad)

        print(f"Compra realizada: {cantidad}x {producto.nombre}. Saldo restante: {self.dinero_disponible}€")


if __name__ == "__main__":
    print("--- APERTURA DEL SUPERMERCADO ---\n")

    ps5 = Producto("PlayStation 5", 500, 10)
    pepito = Cliente("Pepito", 1200)

    print(f"Producto: {ps5}")
    print(f"Cliente: {pepito.nombre} tiene {pepito.dinero_disponible}€\n")

    print("--- Intento 1: Pepito compra 2 consolas ---")
    try:
        pepito.comprar(ps5, 2)
    except Exception as e:
        print(f"Error: {e}")

    print("\n--- Intento 2: Pepito quiere otra más ---")
    try:
        pepito.comprar(ps5, 1)
    except SinDineroError as e:
        print(f"Error de Fondos: {e}")

    print("\n--- Intento 3: Entra Ricachón ---")
    ricachon = Cliente("Ricachón", 50000)

    try:
        ricachon.comprar(ps5, 20)
    except StockInsuficienteError as e:
        print(f"Error de Stock: {e}")

    print("\n--- ESTADO FINAL DE LA TIENDA ---")
    print(ps5)