# Capacitor Bank Inrush Inductor Calculation Tool

## 🇧🇷 Versão PT-BR

Ferramenta técnica para cálculo de corrente de energização (inrush) em bancos de capacitores, conforme IEEE C37.012 e IEC 62271-100.  
Inclui cálculo de indutância, análises isoladas e back-to-back, frequência de oscilação, envelopes e geração automática de relatório PDF via LaTeX.

### Funcionalidades
- Interface Streamlit
- Cálculo de inrush isolado e back-to-back
- Frequência transiente de oscilação
- Conclusão automática baseada nas normas
- Geração de relatório PDF técnico
- Gráficos Plotly interativos

### Executar localmente
```
pip install -r requirements.txt
streamlit run main.py
```

### Docker
```
docker run -p 8080:8080 gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool
```

---

## 🇺🇸 EN-US Version

Technical tool for calculating capacitor bank inrush current according to IEEE C37.012 and IEC 62271-100.  
Includes inductance computation, isolated and back-to-back energization analysis, oscillation frequency, envelopes, and automatic PDF report generation using LaTeX.

### Features
- Streamlit interface
- Inrush calculation (isolated & back-to-back)
- Transient oscillation frequency
- Automatic compliance conclusion
- Technical PDF report generation
- Interactive Plotly graphs

### Run locally
```
pip install -r requirements.txt
streamlit run main.py
```

### Docker
```
docker run -p 8080:8080 gcr.io/apps-dax-energy/st-capacitor-bank-inrush-inductor-calculation-tool
```
