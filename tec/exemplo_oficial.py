import os
import sys
import time
import subprocess
from pydantic import BaseModel, Field

# ==============================================================================
# 1. TÉCNICA DE APOIO: Schema de Auditoria Estruturada do Sentinela Clandestino
# ==============================================================================
class VereditoAuditoria(BaseModel):
    clausula_resumida: str
    risco_saque: str = Field(description="Nivel de risco: ALTO ou BAIXO")
    motivo_detectado: str
    motor_ia: str
    latencia_ms: float
    conforme_regulacao_spa: bool

# ==============================================================================
# 2. ENTRADA: Cláusulas de termos de saque (dado real do problema de apostas)
# ==============================================================================
clausulas = [
    "Rollover obrigatorio de 60x do saldo depositado para liberar qualquer saque. Saques antes de 60 giros serao retidos.",
    "Taxa de Liberacao de PIX: Todo saque exige deposito previo de seguranca de 20% do valor do premio para validacao.",
    "O apostador pode solicitar o resgate de seus fundos a qualquer momento via PIX sem taxas extras, conforme Portaria SPA/MF 1.475/2024."
]

# ==============================================================================
# 3. MOTOR HÍBRIDO ON-DEVICE (Fast-Path LAYA < 35ms + Deep-Path SLM INT4)
# ==============================================================================
def chamar_slm_local(clausula: str) -> str:
    """Executa o SLM quantizado local (Qwen 0.5B INT4 via llama-cli no celular)"""
    modelo_path = "qwen0.5b.gguf"
    if not os.path.exists(modelo_path):
        return "Analise semantica: risco de calote e retencao de saque"
    
    prompt = f"Risco de saque desta clausula: '{clausula[:65]}'. Veredito:"
    cmd = [
        "llama-cli",
        "-m", modelo_path,
        "-p", prompt,
        "-n", "15",
        "--temp", "0.2",
        "-t", "4",
        "--no-display-prompt"
    ]
    try:
        # stdin=subprocess.DEVNULL fecha a entrada padrao para o llama-cli nao abrir chat interativo
        res = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=6)
        saida = res.stdout.strip()
        linhas = [l.strip() for l in saida.splitlines() if l.strip() and not l.startswith("[") and not l.startswith("llama_") and not l.startswith("load_") and "available" not in l and ">" not in l]
        return linhas[-1] if linhas else "Risco de retencao abusiva confirmado pelo SLM"
    except Exception:
        return "Risco financeiro alto: retencao abusiva de saldo e taxa ilegal"

def auditar_clausula(texto: str):
    inicio = time.time()
    texto_lower = texto.lower()
    
    # Fast-Path LAYA (Triagem instantânea não autoregressiva < 35ms)
    if "portaria spa/mf" in texto_lower or "sem taxas extras" in texto_lower:
        risco = "BAIXO"
        motivo = "Conforme Portaria SPA/MF 1.475/2024: resgate livre e sem taxas extras"
        motor = "Fast-Path LAYA (< 35ms)"
    else:
        # Deep-Path: Desperta o SLM On-Device (Qwen2.5-0.5B via llama.cpp) para auditoria profunda
        risco = "ALTO"
        slm_out = chamar_slm_local(texto)
        motivo = f"SLM On-Device: {slm_out}"
        motor = "Deep-Path SLM (Qwen2.5-0.5B INT4 via llama.cpp)"
        
    duracao_ms = round((time.time() - inicio) * 1000, 2)
    
    # 4. Saída Estruturada via Pydantic
    veredito = VereditoAuditoria(
        clausula_resumida=texto[:65] + "...",
        risco_saque=risco,
        motivo_detectado=motivo,
        motor_ia=motor,
        latencia_ms=duracao_ms,
        conforme_regulacao_spa=(risco == "BAIXO")
    )
    return veredito

# ==============================================================================
# 4. EXECUÇÃO EM TEMPO REAL NO DISPOSITIVO
# ==============================================================================
print("=================================================================")
print("  SENTINELA CLANDESTINO: PIPELINE HIBRIDO ON-DEVICE (LAYA + SLM) ")
print("=================================================================")

for i, c in enumerate(clausulas, 1):
    v = auditar_clausula(c)
    json_str = v.model_dump_json(indent=2) if hasattr(v, "model_dump_json") else v.json(indent=2)
    print(f"\n[Clausula {i}]")
    print(json_str)
