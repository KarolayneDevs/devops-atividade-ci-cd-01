from app.calculadora import somar

def test_somar():
    resultado = somar(2,3)

    assert resultado == 5