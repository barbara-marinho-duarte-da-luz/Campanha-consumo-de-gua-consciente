# 💧 Monitor de Consumo de Água Consciente

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte de uma campanha de conscientização ambiental promovida pela companhia de saneamento local. O objetivo é fornecer uma ferramenta em **Python** para classificar o perfil de consumo mensal de água ($m^3$) dos imóveis e emitir alertas educativos personalizados para os moradores e comerciantes.

---

## ⚙️ Regras de Negócio e Classificação

O sistema avalia o tipo de imóvel (`comercial`, `casa` ou `apartamento`) e o volume consumido para aplicar as seguintes diretrizes:

* 🏢 **Comercial:**  
  * *Alerta:* `"Tarifa comercial aplicada – consulte o plano corporativo."`
* 🏢 **Apartamento** com consumo $< 10\ m^3$:  
  * *Alerta:* `"Consumo econômico – excelente controle de água!"`
* 🏠 **Casa** ou **Apartamento** com consumo $\le 25\ m^3$:  
  * *Alerta:* `"Consumo moderado – dentro do padrão residencial."`
* ⚠️ **Qualquer outro caso** (consumo acima do limite residencial):  
  * *Alerta:* `"Consumo excessivo – adote medidas de economia e verifique vazamentos."`

---

🚀 Como Executar o Programa
Opção 1: No Navegador via GitHub Codespaces (Sem Instalar Nada)
Na página inicial deste repositório, clique no botão verde <> Code.

Clique na aba Codespaces e depois em Create codespace on main.

Aguarde o VS Code carregar no navegador.

No terminal integrado inferior, execute os comandos:

Bash
cd consumo-agua
python3 app.py
#### 🛠️ Passo a Passo

1. Clone o repositório ou faça o download:
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
