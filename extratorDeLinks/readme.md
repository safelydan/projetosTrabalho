# extração de domínios para bloqueio a partir de pdf

este script python realiza a extração de **domínios listados em uma tabela de pdf** na coluna **"novos domínios para bloqueio"**. o conteúdo extraído é salvo em um arquivo `.txt`, preservando a ordem em que os domínios aparecem no documento.

## funcionalidades

- leitura de arquivos pdf contendo tabelas.
- extração de domínios da última coluna da tabela.
- salvamento dos domínios extraídos em um arquivo `novos_dominios.txt`.

## pré-requisitos

antes de executar o script, é necessário instalar as bibliotecas abaixo:

```bash
pip install pdfplumber
```

## como usar

1. coloque o arquivo pdf no mesmo diretório do script com o nome `links.pdf` (ou altere o nome no código).
2. execute o script python:

```bash
python extrator_dominios.py
```

3. o arquivo `novos_dominios.txt` será gerado com os domínios extraídos, um por linha.

## estrutura esperada da tabela no pdf

a tabela deve conter três colunas, sendo a última intitulada ou contendo os **novos domínios para bloqueio**, como no exemplo abaixo:

| marca pirata | domínios já bloqueados | novos domínios para bloqueio |
|--------------|------------------------|-------------------------------|
| ...          | ...                    | exemplo.com                   |

## autor

**daniel araujo leal**
