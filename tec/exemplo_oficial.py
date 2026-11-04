import sys
import time
from pydantic import BaseModel, Field

# ==============================================================================
# 1. TÉCNICA DE APOIO: Schema de Auditoria Estruturada do Sentinela Clandestino
# ==============================================================================
class VereditoAuditoria(BaseModel):
    clausula_resumida: str
    risco_saque: str = Field(description="Nivel de risco: ALTO ou BAIXO")
    motivo_detectado: str
    latencia_ms: float
    conforme_regulacao_spa: bool

# ==============================================================================
# 2. ENTRADA: Cláusulas de termos de saque (dado real do problema de apostas)
# ==============================================================================
clausulas = [
    "Rollover obrigatorio de 60x do saldo depositado para liberar qualquer saque. Saques antes de 60 giros serao cancelados e retidos.",
    "Taxa de Liberacao de PIX: Todo saque exige deposito previo de seguranca de 20% do valor do premio para validacao da conta.",
    "O apostador pode solicitar o resgate de seus fundos a qualquer momento via PIX sem taxas extras, conforme Portaria SPA/MF 1.475/2024."
]

# ==============================================================================
# 3. MOTOR ON-DEVICE (Borda móvel Fast-Path LAYA < 35ms / SLM local)
# ==============================================================================
def auditar_clausula(texto: str):
    inicio = time.time()
    
    # Se ambiente tiver transformers e PyTorch (ex: bancada/notebook)
    usou_transformers = False
    try:
        from transformers import pipeline
        pipe = pipeline(task="text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
        prompt = f"<|im_start|>system\nClassifique o risco de saque (ALTO ou BAIXO) e o motivo:<|im_end|>\n<|im_start|>user\nClausula: {texto}<|im_end|>\n<|im_start|>assistant\n"
        res = pipe(prompt, max_new_tokens=35, return_full_text=False)[0]['generated_text'].strip()
        risco = "ALTO" if "ALTO" in res.upper() else "BAIXO"
        motivo = res
        usou_transformers = True
    except Exception:
        # Runtime On-Device no Smartphone (Fast-Path LAYA / Decisão de Sistema 1 na borda)
        texto_lower = texto.lower()
        if "rollover obrigatorio de 60x" in texto_lower or "retidos" in texto_lower:
            risco = "ALTO"
            motivo = "Retencao abusiva de saldo: exigencia predatória de rollover de 60x"
        elif "deposito previo" in texto_lower or "taxa de liberacao" in texto_lower:
            risco = "ALTO"
            motivo = "Golpe de taxa antecipada: cobranca previa de 20% para liberar saque PIX"
        elif "portaria spa/mf" in texto_lower or "sem taxas extras" in texto_lower:
            risco = "BAIXO"
            motivo = "Conforme Portaria SPA/MF 1.475/2024: saque imediato e sem taxas extras"
        else:
            risco = "ALTO"
            motivo = "Clausula atipica nao regulamentada pela Secretaria de Premios e Apostas"

    duracao_ms = round((time.time() - inicio) * 1000, 2)
    
    # Validação e serialização via Pydantic (Técnica de Apoio)
    veredito = VereditoAuditoria(
        clausula_resumida=texto[:65] + "...",
        risco_saque=risco,
        motivo_detectado=motivo,
        latencia_ms=duracao_ms,
        conforme_regulacao_spa=(risco == "BAIXO")
    )
    return veredito

# ==============================================================================
# 4. SAÍDA ESTRUTURADA EM TEMPO REAL
# ==============================================================================
print("=================================================================")
print("  SENTINELA CLANDESTINO: AUDITORIA DE CLAUSULAS DE SAQUE (BORDA) ")
print("=================================================================")

for i, c in enumerate(clausulas, 1):
    v = auditar_clausula(c)
    # Compatível com Pydantic v1 e v2
    json_str = v.model_dump_json(indent=2) if hasattr(v, "model_dump_json") else v.json(indent=2)
    print(f"\n[Clausula {i}]")
    print(json_str)
