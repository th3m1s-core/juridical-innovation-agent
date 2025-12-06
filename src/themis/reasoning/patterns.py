"""
Padrões Sensíveis de Propriedade Intelectual (IP) e Dados Pessoais (PII).
Utilizado pelo detector de riscos do Themis Engine.
Extracted from EditalShield Core Logic.
"""

SENSITIVE_PATTERNS = {
    "algorithm": [
        r"\b[A-Z][a-zA-Z]+(?:Analyzer|Engine|Model|Net|Algorithm)\s*V?\d*\.?\d*\b",
        r"\bproprietário\b",
        r"\bpatenteado\b",
        r"\bexclusivo\b",
    ],
    "parameters": [
        r"\b(?:threshold|decay|learning.?rate|epsilon|gamma|alpha|beta)\s*[=:]\s*[\d.]+\b",
        r"\b[A-Z]\s*[=:]\s*[\d.]+\b",
        r"\bparâmetros?\s*(?:de|do|da)?\s*[\w]+\s*[=:]\s*[\d.]+",
        r"\b(?:W|K|N|M|T)\s*[=:]\s*[\d.]+\b",
    ],
    "dataset": [
        r"\b\d+[MK]?\s*(?:registros?|transações?|amostras?|dados?|clientes?)\b",
        r"\bdataset\s+(?:privado|proprietário|interno)\b",
        r"\bacurácia\s*(?:de)?\s*\d+[.,]\d+\s*%?\b",
        r"\b(?:precision|recall|f1)\s*[=:]\s*[\d.]+\b",
    ],
    "contacts": [
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
        r"\b(?:Dr\.|Prof\.|Eng\.)\s+[A-Z][a-z]+\s+[A-Z][a-z]+\b",
        r"\b\(\d{2}\)\s*\d{4,5}[-.]?\d{4}\b",
    ],
    "metrics": [
        r"\bROI\s*(?:de)?\s*\d+[.,]?\d*\s*[x%]?\b",
        r"\bCAC\s*[=:]\s*R?\$?\s*[\d.,]+\b",
        r"\bLTV\s*[=:]\s*R?\$?\s*[\d.,]+\b",
        r"\b\d+x\s*(?:retorno|crescimento|margem)\b",
    ],
    "clients": [
        r"\bclientes?\s*(?:incluem|como|são)?\s*:?\s*[A-Z][a-zA-Z]+(?:\s*,\s*[A-Z][a-zA-Z]+)*\b",
        r"\b(?:CinemaChain|RetailCorp|FinTechBR|TechVision)\b",
    ],
}

PATTERN_WEIGHTS = {
    "algorithm": 1.0,  # Critical IP
    "parameters": 0.8,  # Detailed implementation
    "dataset": 0.6,    # Data asset
    "contacts": 1.0,   # PII / Privacy
    "metrics": 0.7,    # Business intelligence
    "clients": 0.9,    # Commercial secrets
}

PROTECTION_SUGGESTIONS = {
    "algorithm": 'Substituir por: "algoritmo proprietário desenvolvido internamente"',
    "parameters": 'Remover valores específicos, usar: "parâmetros otimizados empiricamente"',
    "dataset": 'Generalizar: "base de dados representativa do mercado-alvo"',
    "contacts": "Remover informações de contato pessoal",
    "metrics": 'Usar ranges: "ROI entre 2x e 5x" ao invés de valores exatos',
    "clients": 'Substituir por: "clientes em setores estratégicos"',
}
