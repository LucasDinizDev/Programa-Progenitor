# Genealogia - Consultas Genealógicas com PySWIP

Este é um programa Python que utiliza a biblioteca PySWIP para fazer consultas genealógicas em uma base de conhecimento em Prolog. O programa permite consultar informações sobre pais, mães, irmãos, tios/tias e adicionar novos membros à árvore genealógica.

## Funcionamento

O programa cria uma classe `Genealogia`, que encapsula toda a lógica de consulta e manipulação da base de conhecimento Prolog. Ao instanciar um objeto desta classe, a base de conhecimento é inicializada com os fatos genealógicos predefinidos.

Os principais métodos da classe são:
- `consulta_pai(filho)`: Consulta o pai de uma pessoa.
- `consulta_mae(filho)`: Consulta a mãe de uma pessoa.
- `consulta_irmao(pessoa)`: Consulta os irmãos de uma pessoa.
- `consulta_tio_tia(sobrinho)`: Consulta os tios/tias de uma pessoa.
- `adicionar_progenitor_filho_sexo()`: Permite adicionar um novo progenitor, filho e sexo à base de conhecimento.

Além disso, o método `main()` é responsável por apresentar um menu de opções ao usuário, permitindo que ele escolha qual tipo de consulta deseja fazer ou se deseja adicionar novos membros à árvore genealógica.

## Como Rodar o Código

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale a biblioteca PySWIP. Você pode instalar usando o seguinte comando pip:
   ```
   pip install pyswip
   ```

3. Execute o código Python `genealogia.py` em seu terminal ou prompt de comando:
   ```
   python genealogia.py
   ```

4. Siga as instruções apresentadas no menu para consultar informações genealógicas ou adicionar novos membros à árvore genealógica.

Certifique-se de ter o SWI-Prolog instalado em seu sistema, pois o PySWIP depende dele para funcionar. Você pode baixar o SWI-Prolog em [swi-prolog.org](https://www.swi-prolog.org/download/stable).
