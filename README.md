# Projeto de consulta de número fibonacci pela posição dentro da sequência

Para rodar este projeto basta clicar em `Run` e em seguida colocar no `input` um número de posição onde se encontra o número 34 na sequencia.
Caso não acerte na primeira vez, tente novamente.

Este projeto foi codado com `python3.11`

Foi definida a função `def fibonacci(n)` que recebe um parâmetro `n`.

Verificado com `if n <= 1` se o parâmetro `n` é menor ou igual a 1.

`return n` Retorna o valor de `n` caso ele seja menor ou igual a 1, já que os primeiros dois valores da sequência Fibonacci são 0 e 1.

Em `else`, se `n` for maior que 1, o código segue para a proxima etapa.

Passando para `return fibonacci(n-1) + fibonacci(n-2)` que retorna a soma dos dois valores da sequência Fibonacci que antecedem `n`, que são obtidos através de recursão com `n-1` e `n-2`.

O `input` pede ao usuário para inserir um número inteiro que representa a posição do número na sequência Fibonacci que ele deseja visualizar.

`print` chama a função fibonacci com o valor n inserido pelo usuário e exibe o resultado da chamada junto com uma mensagem na tela.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"    *Se dermos como entrada a posição de número 50, o erro que pode acontecer é o programa demorar muito para responder,
pois se tratará de um cálculo muito longo a ser exacutado. Em um de nossos laços/processos, usamos a sequência de 
Fibonacci para fazer buscas, de modo que haja intervalo entre as buscas e evite que gere uma fila muito alta de 
requisições.*"