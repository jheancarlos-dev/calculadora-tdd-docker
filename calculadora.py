def suma(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b

def resta(a: float, b: float) -> float:
    """Devuelve la resta de dos números."""
    return a - b

def multiplicacion(a: float, b: float) -> float:
    """Devuelve la multiplicación de dos números."""
    return a * b

def division(a: float, b: float) -> float:
    """Devuelve la división de dos números.
    
    Lanza ValueError si el divisor es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(a: float, b: float) -> float:
    """Devuelve a elevado a la potencia b."""
    return a ** b