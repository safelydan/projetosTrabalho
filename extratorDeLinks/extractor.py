import pdfplumber
import re

arquivo_pdf = "./links.pdf"
arquivo_saida = "dominiosExtraidos.txt"

novos_dominios = []

with pdfplumber.open(arquivo_pdf) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                if len(linha) >= 3 and linha[2]:
                    encontrados = re.findall(r'\b(?:[\w-]+\.)+(?:[a-z]{2,})\b', linha[2])
                    novos_dominios.extend(encontrados)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    for dominio in novos_dominios:
        f.write(dominio + "\n")

print("domínios salvos em", arquivo_saida)
