**Segurança:**

**Primeiro acesso ao shell (caso não haja usuário cadastrado) :**

1. Caso não exista nenhum usuário cadastrado no MiniSO, será solicitado no shell, a criação de um usuário e com senha. A senha deve ser salva utilizando um salt e em hash (SHA-512), como foi feito no exercício de segurança.
2. Caso haja pelo menos 1 usuário cadastrado, o shell solicitará usuário e senha para login. A senha não deve aparecer enquanto o usuário a digita! (Pode ficar com asteriscos ou sem nada no lugar)
3. Caso o último usuário do MiniSO seja excluído, deve ser executado o passo 1 assim que ele seja apagado e para cada nova execução
**Operações que o shell DEVE ter:**

1. Nome do Comando: "listar" - Cria um novo processo e aloca memória para ele e executa: o equivalente ao ls do linux (dir do prompt de comando / power shell do windows)
2. Nome do Comando: "criar arquivo dir1/arquivo1.txt" - Cria um novo processo e aloca memória para ele e executa: cria o arquivo1.txt dentro do diretório dir1 com conteúdo aleatório. Caso não tenha "dir1/" antes do nome do arquivo no comando, ele será criado no diretório corrente.
3. Nome do Comando: "apagar arquivo dir1/arquivo1.txt" - Cria um novo processo e aloca memória para ele e executa: apaga o arquivo1.txt do diretório dir1. Caso não tenha "dir1/" antes do nome do arquivo no comando, ele será apagado no diretório corrente.
4. Nome do Comando: "criar diretorio dir1/dir2" - Cria um novo processo e aloca memória para ele e executa: cria o diretório dir2 vazio dentro do diretório dir1. Caso não tenha "dir1/" antes do diretório no comando, ele será criado no diretório corrente.
5. Nome do Comando: "apagar diretorio dir1/dir2" - Cria um novo processo e aloca memória para ele e executa: apaga o dir1 do diretório corrente, CASO ESTEJA VAZIO. Caso não tenha "dir1/" antes do diretório no comando, ele será apagado a partir do diretório corrente.
6. Nome do Comando: "apagar diretorio dir1/dir2 --force" - Cria um novo processo e aloca memória para ele e executa: apaga o dir1 do diretório corrente, MESMO QUE TENHA ARQUIVOS OU DIRETÓRIOS.  Caso não tenha "dir1/" antes do diretório no comando, ele será apagado a partir do diretório corrente.
**Deve ser salvo no arquivo e no diretório quem é o dono deles, para evitar que outro usuário cadastrado acesso sem permissão**

Caso o usuário 1 tenho criado o arquivo ou diretório, o usuário 2 não terá acesso a ele e receberá um erro avisando que ele não tem permissão
