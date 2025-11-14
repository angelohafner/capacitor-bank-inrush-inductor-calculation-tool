# Capacitor Bank Inrush Inductor Calculation Tool  
Ferramenta profissional para cálculo de corrente de energização (inrush) em bancos de capacitores, com versão completa em **PT-BR** e **EN-US**.

---

# 🇧🇷 Versão PT-BR

## 📘 Visão Geral

Esta ferramenta calcula a **corrente de energização (inrush)** em bancos de capacitores de média tensão, permitindo avaliar a necessidade de reatores limitadores segundo:

- **IEEE Std C37.012**
- **IEC 62271-100 – Tabela 9**

O sistema simula cenários **isolados** e **back-to-back**, gera gráficos dinâmicos (Plotly) e produz automaticamente um **relatório técnico em PDF via LaTeX**, incluindo conclusões baseadas nas normas.

---

## 🎯 Objetivos do Projeto

- Calcular correntes de energização em diferentes topologias.
- Determinar indutâncias equivalentes.
- Estimar frequência de oscilação transitória.
- Verificar limites normativos automaticamente.
- Gerar relatório técnico completo com gráficos + conclusões.

---

## 🧠 Modelo Matemático Utilizado

### Capacitância equivalente  
$$
C = \frac{1}{\omega X}
$$

### Indutância equivalente para energização isolada  
\[
L_{eq} = L_{curto} + L_{banco}
\]

### Frequência transitória  
\[
f_{osc} = \frac{\omega}{2\pi}
\]

### Corrente de pico inicial  
\[
i_{pico} = F_C \cdot \frac{V\sqrt{2}}{L_{eq}\,\omega}
\]

---

## 📂 Estrutura do Projeto

```
capacitor-bank-inrush-inductor-calculation-tool/
│
├── main.py
├── config.py
├── inputs_layout.py
├── funcoes_auxiliares.py
├── relatorio.py
├── dicionarios.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── TEMPLATE_Relatorio_Inrush_DAX_xx.tex
```

---

## 🚀 Como Executar Localmente

```bash
pip install -r requirements.txt
streamlit run main.py
```

A interface abrirá no navegador.

---

## 🐳 Executar com Docker

### Build pelo Cloud Build (Google Cloud)
```bash
gcloud builds submit   --tag gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool   --project=apps-dax-energy
```

### Rodar localmente
```bash
docker run -p 8080:8080 gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool
```

Acesse em:  
**http://localhost:8080**

---

## 📑 Relatório PDF

O projeto contém:

- Templates LaTeX customizados  
- Geração automática via xelatex  
- Inclusão de figuras, equações e conclusão  
- Textos multilíngues PT/EN/ES/DE/FR/CN

---

## 👨‍💻 Autor

**Eng. Angelo Alfredo Hafner**  
Engenheiro Eletricista – DAX-Energy  
aah@dax.energy  

---

---

# 🇺🇸 EN-US Version

## 📘 Overview

This tool computes the **inrush current** of medium-voltage capacitor banks, evaluating the need for limiting reactors according to:

- **IEEE Std C37.012**
- **IEC 62271-100 – Table 9**

It simulates **isolated** and **back-to-back** energization scenarios, generates dynamic Plotly graphs, and automatically builds a **technical PDF report via LaTeX** based on standard compliance.

---

## 🎯 Project Goals

- Compute inrush current for multiple protection topologies.
- Determine equivalent inductances.
- Estimate transient oscillation frequency.
- Automatically verify IEEE/IEC compliance.
- Generate full professional PDF reports.

---

## 🧠 Mathematical Model

### Equivalent capacitance  
\[
C = \frac{1}{\omega X}
\]

### Equivalent inductance (isolated energization)  
\[
L_{eq} = L_{fault} + L_{bank}
\]

### Transient frequency  
\[
f_{osc} = \frac{\omega}{2\pi}
\]

### Peak inrush current  
\[
i_{peak} = F_C \cdot \frac{V\sqrt{2}}{L_{eq}\,\omega}
\]

---

## 📂 Project Structure

```
capacitor-bank-inrush-inductor-calculation-tool/
│
├── main.py
├── config.py
├── inputs_layout.py
├── funcoes_auxiliares.py
├── relatorio.py
├── dicionarios.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── TEMPLATE_Relatorio_Inrush_DAX_xx.tex
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run main.py
```

---

## 🐳 Run with Docker

### Build via Google Cloud Build
```bash
gcloud builds submit   --tag gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool   --project=apps-dax-energy
```

### Run locally
```bash
docker run -p 8080:8080 gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool
```

Open:  
**http://localhost:8080**

---

## 📑 PDF Report

Includes:

- Custom LaTeX templates  
- Automatic compilation  
- Figures, equations, and conclusions  
- Multi-language support (PT/EN/ES/DE/FR/CN)

---

## 👨‍💻 Author

**Eng. Angelo Alfredo Hafner**  
Electrical Engineer – DAX-Energy  
aah@dax.energy

---

## 📘 License

MIT License
