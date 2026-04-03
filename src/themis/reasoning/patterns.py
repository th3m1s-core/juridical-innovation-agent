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
    "lpi_patent": [
        r"\bnovidade.?(?:absoluta)?\b",
        r"\batividade.?(?:inventiva)?\b",
        r"\baplicação.?(?:industrial)?\b",
        r"\bestado.?(?:da.?)?técnica\b",
        r"\breivindicação.?independente\b",
    ],
    "software_law": [
        r"\bcódigo.?(?:fonte|objeto)\b",
        r"\bregistro.?(?:di?o.?)?software\b",
        r"\bobra.?(?:literária|técnica)\b",
        r"\bengenharia.?(?:reversa|interoperabilidade)\b",
    ],
    "tax_incentive": [
        r"\blei.?(?:di?o.?)?bem\b",
        r"\bsubvenção.?(?:econômica)?\b",
        r"\bPD&I\b",
        r"\bFINEP|FAPESP|CNPq\b",
    ],
    "ai_governance": [
        r"\brisco.?(?:alto|inaceitável|crítico)\b",
        r"\bexplicabilidade\b",
        r"\bviés.?(?:algorítmico)?\b",
        r"\btransparência.?(?:algorítmica)?\b",
        r"\bintervenção.?(?:humana)?\b",
    ],
    "lgpd_privacy": [
        r"\bdados?.?(?:pessoais|sensíveis)\b",
        r"\btitular.?(?:di?os.?)?dados?\b",
        r"\banonimização\b",
        r"\bfinalidade.?(?:do.?)?tratamento\b",
        r"\bencarregado.?DPO\b",
    ],
    "innovation_law": [
        r"\blei.?(?:da.?)?inovação\b",
        r"\bICT.?pública\b",
        r"\bencomenda.?(?:tecnológica)?\b",
        r"\bcompartilhamento.?(?:de.?)?laboratórios?\b",
    ],
}

PATTERN_WEIGHTS = {
    "algorithm": 1.0,
    "parameters": 0.8,
    "dataset": 0.6,
    "contacts": 1.0,
    "metrics": 0.7,
    "clients": 0.9,
    "lpi_patent": 0.4,
    "software_law": 0.5,
    "tax_incentive": 0.3,
    "ai_governance": 0.8,
    "lgpd_privacy": 1.0,
    "innovation_law": 0.4,
}

PROTECTION_SUGGESTIONS = {
    "algorithm": 'Substituir por: "algoritmo proprietário desenvolvido internamente"',
    "parameters": 'Remover valores específicos, usar: "parâmetros otimizados empiricamente"',
    "dataset": 'Generalizar: "base de dados representativa do mercado-alvo"',
    "contacts": "Remover informações de contato pessoal",
    "metrics": 'Usar ranges: "ROI entre 2x e 5x" ao invés de valores exatos',
    "clients": 'Substituir por: "clientes em setores estratégicos"',
    "lpi_patent": 'Verificar Art. 10 da LPI para evitar negação por abstração',
    "software_law": 'Assegurar registro no INPI para proteção de "código-objeto"',
    "tax_incentive": 'Mapear este componente para créditos da Lei do Bem',
    "ai_governance": 'Realizar Avaliação de Risco Algorítmico (PL 2338)',
    "lgpd_privacy": 'Implementar Privacy-by-Design e Anonimização de datasets',
    "innovation_law": 'Explorar parcerias com ICTs sob a Lei 10.973/04',
}
