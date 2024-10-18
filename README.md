# Sistema de Arquivos Simulado em Python

Este projeto implementa um sistema de arquivos simples utilizando listas encadeadas para gerenciar o armazenamento de arquivos na memória. A implementação simula operações básicas de criação, leitura e exclusão de arquivos, utilizando uma memória limitada e blocos encadeados.

## Estrutura do Sistema de Arquivos

A memória é composta por blocos de tamanho fixo (3 bytes), onde cada bloco armazena um caractere e um ponteiro para o próximo bloco. Esse sistema permite armazenar arquivos em blocos dispersos na memória e gerenciar o uso de memória livre para maximizar o espaço disponível.

### Principais Componentes:

- **Disco (Memória):** Representado por uma lista de blocos, onde cada bloco contém:
  - Um caractere (parte do arquivo)
  - Um ponteiro indicando o próximo bloco ou `NULL` se for o último bloco do arquivo
- **Tabela de Arquivos:** Armazena informações sobre os arquivos criados, incluindo:
  - Nome do arquivo
  - Tamanho do arquivo (número de caracteres)
  - Endereço inicial do arquivo na memória
- **Blocos Livres:** Uma lista de índices dos blocos de memória disponíveis para alocação.

### Funcionalidades

1. **Criação de Arquivos:**
   - Divide o conteúdo do arquivo em blocos.
   - Armazena cada caractere em um bloco e faz o encadeamento entre os blocos.
   - Atualiza a tabela de arquivos com o nome, tamanho e endereço inicial do arquivo.

2. **Leitura de Arquivos:**
   - Recupera o conteúdo de um arquivo percorrendo a lista encadeada de blocos.
   - Exibe o conteúdo do arquivo na tela.

3. **Exclusão de Arquivos:**
   - Libera os blocos utilizados pelo arquivo de volta para a lista de blocos livres.
   - Remove as informações do arquivo da tabela de arquivos.

4. **Impressão do Estado do Disco:**
   - Exibe a tabela de arquivos e o estado atual dos blocos de memória (ocupados ou livres).

### Requisitos de Implementação

- A memória total usada é de 96 bytes, simulada por 32 blocos de 3 bytes cada.
- Cada bloco contém 1 caractere e 1 ponteiro (short int).
- Operações suportadas:
  - Criação de arquivo: `create_file(file_name, content)`
  - Leitura de arquivo: `read_file(file_name)`
  - Exclusão de arquivo: `delete_file(file_name)`

### Exemplo de Uso:

```python
create_file("f01.file", "PERNAMBUCO")
create_file("f02.file", "ALAGOAS")
read_file("f01.file")
delete_file("f01.file")
create_file("f03.file", "PARAIBA")
read_file("f03.file")
create_file("f04.file", "MARANHAO")
read_file("f04.file")
delete_file("f02.file")
