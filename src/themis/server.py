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
from themis.reasoning.optimizer import VectorOptimizer

detector = RiskDetector()
optimizer = VectorOptimizer()

@mcp.tool()
def analyze_innovation(text: str) -> str:
    """
    Analisa a inovação usando o Modelo Vetorial de Themis (TVSM).
    Retorna Score de Inovação, Vetores (H, Z, C) e Riscos.
    """
    result = detector.analyze(text)
    
    # Header High-Tech
    output = f"⬢ THEMIS VECTOR ANALYSIS (v1.0)\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output += f"💎 INNOVATION INDEX: {result['innovation_score']}/100\n\n"
    
    # Vector Components
    v = result['vector']
    output += f"📐 VECTOR COMPONENTS [H, Z, C]:\n"
    output += f"  • H (Entropy):    {v['H']:.4f} [Info Density]\n"
    output += f"  • Z (Zipf):       {v['Z']:.4f} [Tech Depth]\n"
    output += f"  • C (Compliance): {v['C']:.4f} [Legal Safety]\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    # Risk & Patterns
    if result['patterns_found']:
        output += f"\n⚠️ RISK DETECTED (Compliance Drop):\n"
        for cat, matches in result['patterns_found'].items():
            output += f"  - {cat.upper()}: {', '.join(matches)}\n"
    
    if result['suggestions']:
        output += "\n💡 PIVOT SUGGESTIONS:\n"
        for sug in result['suggestions']:
            output += f"  > {sug}\n"
            
    return output

@mcp.tool()
def optimize_innovation(text: str) -> str:
    """
    Analisa o texto E fornece um plano estratégico de otimização.
    Identifica o gargalo vetorial e simula melhorias específicas.
    """
    result = detector.analyze(text)
    
    # Generate strategic optimization report
    optimization_report = optimizer.generate_optimization_report(
        result['vector'], 
        result['patterns_found']
    )
    
    # Combine analysis with optimization guidance
    output = f"⬢ THEMIS STRATEGIC OPTIMIZATION\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output += f"Current Innovation Score: {result['innovation_score']}/100\n"
    output += optimization_report
    
    return output


def main():
    mcp.run()

if __name__ == "__main__":
    main()
