TOTAL_MEMORY_BYTES = 96
BLOCK_SIZE = 3
TOTAL_BLOCKS = TOTAL_MEMORY_BYTES // BLOCK_SIZE
NULL_POINTER = -1


disk = [{'char': None, 'pointer': NULL_POINTER} for _ in range(TOTAL_BLOCKS)]
file_table = {}

free_blocks = list(range(TOTAL_BLOCKS))

def create_file(file_name, content):
    content_length = len(content)

  
    if file_name in file_table:
        print(f"Erro: Arquivo '{file_name}' já existe!")
        return
    
    
    if len(free_blocks) < content_length:
        print("Erro: Memória insuficiente para armazenar o arquivo!")
        return
    
    
    start_block = free_blocks.pop(0)
    current_block = start_block
    file_table[file_name] = {'size': content_length, 'start': start_block}

    for i in range(content_length):
        
        disk[current_block]['char'] = content[i]

        if i < content_length - 1:
            next_block = free_blocks.pop(0)
            disk[current_block]['pointer'] = next_block
            current_block = next_block
        else:
            
            disk[current_block]['pointer'] = NULL_POINTER

    print(f"Arquivo '{file_name}' criado com sucesso!")
    print_disk_status()

def read_file(file_name):
    """
    Função para ler o conteúdo de um arquivo armazenado.
    :param file_name: Nome do arquivo a ser lido.
    """
    if file_name not in file_table:
        print(f"Erro: Arquivo '{file_name}' não encontrado!")
        return

    
    start_block = file_table[file_name]['start']
    current_block = start_block
    content = ""

    while current_block != NULL_POINTER:
        content += disk[current_block]['char']
        current_block = disk[current_block]['pointer']

    print(f"Conteúdo do arquivo '{file_name}': {content}")

def delete_file(file_name):
    """
    Função para excluir um arquivo do sistema.
    :param file_name: Nome do arquivo a ser excluído.
    """
    if file_name not in file_table:
        print(f"Erro: Arquivo '{file_name}' não encontrado!")
        return

   
    start_block = file_table[file_name]['start']
    current_block = start_block

    while current_block != NULL_POINTER:
        next_block = disk[current_block]['pointer']
        
        disk[current_block] = {'char': None, 'pointer': NULL_POINTER}
        free_blocks.append(current_block)
        current_block = next_block

    
    del file_table[file_name]
    
    
    free_blocks.sort()
    print(f"Arquivo '{file_name}' excluído com sucesso!")
    print_disk_status()

def print_disk_status():
    print("\n=== Estado Atual do Disco ===")
    print("Bloco | Caractere | Ponteiro")
    print("-----------------------------")
    for i, block in enumerate(disk):
        print(f" {i:<5}| {block['char'] if block['char'] is not None else 'None':^9} | {block['pointer']:>8}")

    print("\n=== Tabela de Arquivos ===")
    if file_table:
        print("Arquivo    | Tamanho | Endereço Inicial")
        print("---------------------------------------")
        for file_name, info in file_table.items():
            print(f"{file_name:<10} | {info['size']:^7}  | {info['start']:^15}")
    else:
        print("Nenhum arquivo armazenado no sistema.")

    print("\nBlocos livres:", sorted(free_blocks))
    print("-----------------------------\n")

create_file("f01.file", "PERNAMBUCO")
create_file("f02.file", "ALAGOAS")
read_file("f01.file")
delete_file("f01.file")
create_file("f03.file", "PARAIBA")
read_file("f03.file")
create_file("f04.file", "MARANHAO")
read_file("f04.file")
delete_file("f02.file")


 
