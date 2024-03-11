import Metodi

if __name__ == "__main__":
    # Richiama la funzione saluta dal modulo Metodi
    nome = "Sofia"
    saluto = Metodi.saluta(nome)
    print(saluto)

    # Richiama la funzione somma dal modulo Metodi
    risultato = Metodi.somma(3, 5)
    print("La somma di 3 e 5 è:", risultato)
