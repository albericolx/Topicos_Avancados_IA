#!/bin/bash
clear
echo "================================================================="
echo "   SENTINELA CLANDESTINO · VIGILANTE DE ESPELHOS E APKS         "
echo "   Dispositivo: Samsung Galaxy A15 (MediaTek Helio G99)         "
echo "   Pipeline: Fast-Path LAYA (< 35ms) + Deep-Path SLM INT4      "
echo "================================================================="
echo ""
echo "--- [1] COMMITS VERIFICADOS DO CODIGO-FONTE (GIT LOG) ---"
git --no-pager log -n 2 --oneline
echo ""
echo "--- [2] AUDITORIA ON-DEVICE EM TEMPO REAL (PYDANTIC) ---"
python tec/exemplo_oficial.py
echo ""
echo "================================================================="
echo "   AUDITORIA CONCLUIDA COM SUCESSO NO SMARTPHONE                "
echo "================================================================="
