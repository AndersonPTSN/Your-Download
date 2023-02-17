# Your-Download

## Introdução 
Your-Download é um programa criado para baixar vídeos ou musicas do [YouTube]( https://www.youtube.com/), seja em um único vídeo ou uma playlist e salvar em uma pasta.

<div align="center">

![image](https://user-images.githubusercontent.com/26872755/219540987-3b41c7d9-4a98-4626-80cb-9b9380edfacd.png)

</div>

Nesse projeto foram utilizadas as seguintes bibliotecas: 
- PySimpleGUI para criação de uma interface
- Pytube para utilização das funções de manipulação de vídeos do YouTube
- Threading para diminuir o tempo de execução 
- OS para criação de diretórios

## Como Executar
Para poder rodar esse arquivo em sua máquina, e necessário instalar o [Python]( https://www.python.org/downloads/), eu utilizei o Python 3.8.10, contudo, versões posteriores podem rodá-lo.
Ao instalar o Python, é necessário instala as demais bibliotecas utilizadas no projeto com as linhas:
```
pip install pysimplegui
```
```
pip install pytube
```
>**Observação:** As bibliotecas *Threading* e *OS* por padrão já estão instaladas quando você instala o Python.

Por fim, você poderá executar o arquivo .py via terminal, certifique-se que o arquivo .py se encontra no mesmo diretório na qual você esteja executando.

<div align="center">

![image](https://user-images.githubusercontent.com/26872755/219539822-7a592dd3-f5f7-4a1d-b70d-8382a142fb56.png)

</div> 

## Geração do arquivo Executável
No diretório que criei o [Frame-Cutter]( https://github.com/AndersonPTSN/Frame-Cutter) eu mostro o passo-a-passo de como pegar um arquivo Python como esse e transforma-lo em um executável, caso queira deixarei o [Link aqui.](https://github.com/AndersonPTSN/Frame-Cutter#gera%C3%A7%C3%A3o-do-arquivo-execut%C3%A1vel)

## Referências
[PySimpleGUI](https://www.pysimplegui.org)

[Pytube]( https://pytube.io)

[OS](https://docs.python.org/3/library/os.html)
