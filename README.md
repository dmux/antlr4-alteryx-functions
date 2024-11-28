# antlr4-alteryx-functions

Este projeto, **antlr4-alteryx-functions**, utiliza o ANTLR4 para processar expressões condicionais e funções de conversão do Alteryx Designer e transpilar essas expressões para código Python. Ele fornece uma solução automática e extensível para migrar lógicas de negócio do Alteryx para Python.

## Funcionalidades

- **Reconhecimento de Expressões Condicionais:**
  - `IF ... THEN ... ELSE ... ENDIF`
  - `IIF(condition, true_result, false_result)`
  - `SWITCH(expression, case1, result1, ..., default_result)`

- **Suporte a Funções de Conversão:**
  - `TOBOOLEAN(expression)`
  - `TODATE(expression)`
  - `TONUMBER(expression)`
  - `TOSTRING(expression)`

- **Transpilação Automática:** As expressões do Alteryx são convertidas para código Python equivalente.

## Estrutura do Projeto

- **Gramatica ANTLR:** Definição da sintaxe para reconhecer expressões do Alteryx em um arquivo `.g4`.
- **Parser e Lexer:** Gerados pelo ANTLR com base na gramática.
- **Transpiler:** Um visitante em Python que converte as expressões para Python.
- **Exemplos:** Testes e exemplos práticos de uso do sistema.

## Requisitos

- **Python:** Versão 3.12 ou superior.
- **ANTLR4:** Ferramenta para gerar o parser e o lexer.

### Dependências

As dependências necessárias estão listadas no arquivo `pyproject.toml`.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/antlr4-alteryx-functions.git
   cd antlr4-alteryx-functions
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Instale o ANTLR4 (caso não tenha):

   ```bash
   brew install antlr # Para macOS
   sudo apt install antlr4 # Para Linux (distribuições suportadas)
   ```

4. Gere os arquivos do parser e lexer:

   ```bash
   antlr4 -Dlanguage=Python3 AlteryxConditional.g4
   ```

## Uso

1. Escreva uma expressão em Alteryx:

   ```plaintext
   IF "age" > 30 THEN "old" ELSE "young" ENDIF
   ```

2. Rode o transpiler para converter para Python:

   ```python
   from transpiler import transpile_alteryx_to_python

   alteryx_expression = 'IF "age" > 30 THEN "old" ELSE "young" ENDIF'
   python_code = transpile_alteryx_to_python(alteryx_expression)
   print(python_code)  # Resultado: ("old" if "age" > 30 else "young")
   ```

## Testes

Execute testes automatizados para validar as funcionalidades:

```bash
pytest
```

## Exemplos Suportados

### Entrada 1

```plaintext
TONUMBER("42")
```

#### Saída 1

```python
float("42")
```

### Entrada 2

```plaintext
IF TOBOOLEAN("1") THEN TOSTRING(100) ELSE "False" ENDIF
```

#### Saída 2

```python
("str(100)" if bool("1") else "False")
```


## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
