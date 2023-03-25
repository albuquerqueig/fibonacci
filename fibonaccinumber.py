# É definida uma função que vai chamar com recursão o número fibonacci do input
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Dê input e tente encontrar o número que representa a colocação do número 34 (resultado esperado) na sequência fibonacci
n = int(input("Você deseja ver o número que está em qual posição na sequência Fibonacci? "))
print("O valor correspondente à essa posição na sequência de Fibonacci é:", fibonacci(n))



'''
    Se dermos como entrada a posição de número 50, o erro que pode acontecer é o programa demorar muito para responder,
pois se tratará de um cálculo muito longo a ser exacutado. Em um de nossos laços/processos, usamos a sequência de 
Fibonacci para fazer buscas, de modo que haja intervalo entre as buscas e evite que gere uma fila muito alta de 
requisições.
'''