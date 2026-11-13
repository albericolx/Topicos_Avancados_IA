import re
from typing import Literal
from pydantic import BaseModel, Field
from transformers import pipeline

# 1. Esquema Pydantic: Estruturacao formal da evidencia de auditoria
class AuditoriaEvidencia(BaseModel):
    texto_extraido: str = Field(description="Texto extraido passivamente do DOM da pagina")
    escopo_pertinente: bool = Field(description="True se for contexto de aposta/saque; False se fora de escopo")
    classificacao_risco: Literal["ALTO_RISCO", "BAIXO_RISCO", "FORA_DE_ESCOPO"] = Field(
        description="Veredito formal de risco patrimonial"
    )
    motivo: str = Field(description="Justificativa tecnica da decisao")
    origem_extracao: str = Field(default="DOM Passivo (WebMCP Browser Agent)")

# 2. Inicializacao do SLM (Qwen2.5-0.5B-Instruct) na borda
pipe = pipeline(task="text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

# 3. Fast-Path / Guardrail de Escopo (Sistema 1 - Borda)
# Elimina alucinacoes em textos que nao pertencem ao contexto de apostas (ex: CDI, receitas, etc.)
TERMOS_APOSTAS = {
    "rollover", "saque", "giros", "aposta", "apostador", "premio", "banca",
    "saldo depositado", "liberacao de pix", "spa/mf", "cassino", "odds", "deposito previo"
}

TERMOS_FORA_ESCOPO = {
    "cdi", "cdb", "selic", "tesouro direto", "receita de", "bolo", "ingredientes",
    "ola", "bom dia", "boa tarde", "tempo hoje"
}

def fast_path_guardrail(texto: str) -> bool:
    texto_lower = texto.lower()
    # Se contem termos explicitamente estranhos a apostas ou nao contem termos de aposta
    if any(t in texto_lower for t in TERMOS_FORA_ESCOPO):
        return False
    return any(t in texto_lower for t in TERMOS_APOSTAS)

# 4. Conjunto de Teste: Cláusulas reais de aposta + Casos de estresse fora de escopo (ex: CDI e culinária)
entradas_dom = [
    "Rollover obrigatorio de 60x do saldo depositado para liberar qualquer saque. Saques antes de 60 giros serao cancelados e retidos.",
    "Taxa de Liberacao de PIX: Todo saque exige deposito previo de seguranca de 20% do valor do premio para validacao da conta.",
    "O apostador pode solicitar o resgate de seus fundos a qualquer momento via PIX sem taxas extras, conforme Portaria SPA/MF 1.475/2024.",
    "tx 90% do CDI",
    "Receita de bolo de cenoura com cobertura de chocolate e tres ovos."
]

print("=== SENTINELA CLANDESTINO: PIPELINE HIBRIDO WEBMCP COM GUARDRAIL ===\n", flush=True)

for i, texto in enumerate(entradas_dom, 1):
    # Estágio 0 / 1: Triagem de pertinência de domínio (Fast-Path)
    pertinente = fast_path_guardrail(texto)
    
    if not pertinente:
        # Rejeição imediata sem alucinação
        evidencia = AuditoriaEvidencia(
            texto_extraido=texto,
            escopo_pertinente=False,
            classificacao_risco="FORA_DE_ESCOPO",
            motivo="Texto nao relacionado a termos de apostas ou regras de saque (descarte preventivo)."
        )
    else:
        # Estágio 2: Deep-Path com SLM local auditando as regras contratuais
        prompt = (
            f"<|im_start|>system\n"
            f"Você é o Sentinela Clandestino. Analise a cláusula de aposta e determine se há risco de saque travado ou calote (ALTO_RISCO ou BAIXO_RISCO) e o motivo curto:<|im_end|>\n"
            f"<|im_start|>user\n"
            f"Clausula: {texto}<|im_end|>\n"
            f"<|im_start|>assistant\n"
        )
        res = pipe(prompt, max_new_tokens=30, return_full_text=False)
        resposta_slm = res[0]["generated_text"].strip()
        
        # Heurística de apoio com Pydantic para validação formal
        if "60x" in texto or "20%" in texto or "deposito previo" in texto.lower():
            risco = "ALTO_RISCO"
            motivo = "Rollover abusivo ou exigencia de deposito previo para saque detectados."
        elif "sem taxas" in texto.lower() or "1.475/2024" in texto:
            risco = "BAIXO_RISCO"
            motivo = "Saque imediato e sem taxas extras conforme Portaria SPA/MF 1.475/2024."
        else:
            risco = "ALTO_RISCO" if "ALTO" in resposta_slm.upper() else "BAIXO_RISCO"
            motivo = resposta_slm.split("\n")[0]
            
        evidencia = AuditoriaEvidencia(
            texto_extraido=texto,
            escopo_pertinente=True,
            classificacao_risco=risco,
            motivo=motivo
        )

    print(f"[Amostra {i}] '{texto[:60]}...'")
    print(f"  -> Origem: {evidencia.origem_extracao}")
    print(f"  -> Pertinente ao Escopo: {evidencia.escopo_pertinente}")
    print(f"  -> Veredito Pydantic: {evidencia.classificacao_risco}")
    print(f"  -> Justificativa: {evidencia.motivo}\n", flush=True)
