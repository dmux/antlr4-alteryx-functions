# antlr4-alteryx-functions

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmux/antlr4-alteryx-functions/HEAD)

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

## Status de Conversão

Abaixo estão listadas as expressões condicionais e funções de conversão do Alteryx que estão sendo convertidas para Python.

### Expressões Condicionais - Alteryx

### Funções de Conversão - Alteryx

| Nome da Expressão | Descrição Breve                                                         | Link de Referência                                                                                          | Status de Conversão |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------- |
| `BinToInt`        | Converte um número binário para inteiro.                                | [BinToInt](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#bintoint)         | Em Progresso        |
| `Bool`            | Converte um valor em um tipo booleano.                                  | [Bool](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#bool)                 | Pronto              |
| `Byte`            | Converte um valor em um tipo byte.                                      | [Byte](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#byte)                 | Em Progresso        |
| `CharToInt`       | Converte um caractere para o valor inteiro correspondente.              | [CharToInt](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#chartoint)       | Pronto              |
| `Date`            | Converte um valor em um tipo de data.                                   | [Date](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#date)                 | Em Progresso        |
| `DateTime`        | Converte um valor em um tipo de data e hora.                            | [DateTime](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#datetime)         | Em Progresso        |
| `FixedDecimal`    | Converte um número em um tipo decimal fixo com a precisão especificada. | [FixedDecimal](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#fixeddecimal) | Em Progresso        |
| `Float`           | Converte um valor em um número de ponto flutuante.                      | [Float](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#float)               | Em Progresso        |
| `Int16`           | Converte um valor para um inteiro de 16 bits.                           | [Int16](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#int16)               | Em Progresso        |
| `Int32`           | Converte um valor para um inteiro de 32 bits.                           | [Int32](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#int32)               | Em Progresso        |
| `Int64`           | Converte um valor para um inteiro de 64 bits.                           | [Int64](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#int64)               | Em Progresso        |
| `String`          | Converte um valor em uma string.                                        | [String](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#string)             | Pronto              |
| `ToLowerCase`     | Converte uma string para letras minúsculas.                             | [ToLowerCase](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#tolowercase)   | Em Progresso        |
| `ToUpperCase`     | Converte uma string para letras maiúsculas.                             | [ToUpperCase](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#touppercase)   | Em Progresso        |
| `WString`         | Converte um valor em uma string Unicode.                                | [WString](https://help.alteryx.com/20241/en/designer/functions/conversion-functions.html#wstring)           | Em Progresso        |

**Legenda do Status de Conversão**:

- **Pronto**: Converte com sucesso e está documentado.
- **Em Progresso**: Está sendo implementado.

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
