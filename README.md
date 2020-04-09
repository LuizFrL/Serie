# Serie
Roda serie automaticamente.
## Como Usar:
* Listar Diretorio onde as series estão presentes.
* Para manter a ordem, a sequência correta de episódios deve estar numerada em sequencia de numeros ou 
letras (1, 2, 3 ou episodio 1, episodio 2).
* Os episódios devem estar em MP4

## Funcionamento:
*   Lista os arquivos MP4 do diretório, em nenhum momento ele ordena nada, mas o padrão é ser
ordenado pelo nome do arquivo em ordem alfabética, apos inicia uma sequencia onde identifica
a duração do vídeo espera esse tempo - 20 seg pra poder fechar o video usando o taskkill da 
tarefa (no meu caso foi ApplicationFrameHost.exe).
* Por fim, renomeia o episódio com um @ no inicio que impede sua execução, tento uma espécie
de "check point"