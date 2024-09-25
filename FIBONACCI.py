def pertence_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.
    
    :param numero: Número a ser verificado
    :return: True se o número pertence à sequência, False caso contrário
    """
    a, b = 0, 1  
    fibonacci = [a, b]  
    
    
    while b < numero:
        a, b = b, a + b  
        fibonacci.append(b)  

    
    return numero in fibonacci

numero_informado = int(input("Informe um número: "))


if pertence_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
