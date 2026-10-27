from transformers import pipeline

pipe = pipeline(task="text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

# Entrada: clausulas de termos de saque (o dado do problema de apostas clandestinas)
clausulas = [
    "Rollover obrigatorio de 60x do saldo depositado para liberar qualquer saque. Saques antes de 60 giros serao cancelados e retidos.",
    "Taxa de Liberacao de PIX: Todo saque exige deposito previo de seguranca de 20% do valor do premio para validacao da conta.",
    "O apostador pode solicitar o resgate de seus fundos a qualquer momento via PIX sem taxas extras, conforme Portaria SPA/MF 1.475/2024."
]

# Saida: auditoria de risco de saque retido do Sentinela Clandestino
for i, c in enumerate(clausulas, 1):
    prompt = f"<|im_start|>system\nClassifique o risco de saque (ALTO ou BAIXO) e o motivo:<|im_end|>\n<|im_start|>user\nClausula: {c}<|im_end|>\n<|im_start|>assistant\n"
    res = pipe(prompt, max_new_tokens=40, return_full_text=False)
    print(f"[Clausula {i}] {c[:65]}...")
    print(f"-> Auditoria: {res[0]['generated_text'].strip()}\n")
