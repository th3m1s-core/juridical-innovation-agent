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

from themis.reasoning.detector import RiskDetector

detector = RiskDetector()

@mcp.tool()
def analyze_risk(text: str) -> str:
    """
    Analisa o risco de exposição de PI e complexidade técnica.
    Retorna score (0-100), padrões encontrados e sugestões.
    """
    result = detector.analyze(text)
    
    # Format output for LLM consumption
    output = f"🛡️ Risk Analysis (Score: {result['risk_score']}/100)\n"
    output += f"- Type: {result['section_type']}\n"
    output += f"- Tech Density (Zipf): {result['zipf_score']:.2f}\n"
    
    if result['patterns_found']:
        output += "\n🔍 Sensitive Patterns Detected:\n"
        for cat, matches in result['patterns_found'].items():
            output += f"  - {cat.upper()}: {', '.join(matches)}\n"
    
    if result['suggestions']:
        output += "\n💡 Suggestions:\n"
        for sug in result['suggestions']:
            output += f"  - {sug}\n"
            
    return output

def main():
    mcp.run()

if __name__ == "__main__":
    main()
