from fastmcp import FastMCP
from themis.knowledge import LegalKnowledgeBase

# Inicializa servidor MCP
mcp = FastMCP("Themis Legal Engine")

# Carrega conhecimento
kb = LegalKnowledgeBase()

@mcp.tool()
def get_legal_context() -> str:
    """Retorna o contexto jurídico (LPI, TRL) carregado na memória."""
    return kb.get_context()

@mcp.tool()
def analyze_patentability(description: str) -> str:
    """
    Analisa a patentiabilidade de uma descrição técnica baseada na LPI.
    (Mock implementation for skeleton)
    """
    return f"Analyzer initialized. Context loaded: {len(kb.documents)} docs. Analysis for: {description[:50]}..."

def main():
    mcp.run()

if __name__ == "__main__":
    main()
