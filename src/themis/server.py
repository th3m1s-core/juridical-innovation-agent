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
from themis.data import EditalShieldConnector, INPIConnector

detector = RiskDetector()
optimizer = VectorOptimizer()
db = EditalShieldConnector()  # Will use EDITALSHIELD_DB env var
inpi = INPIConnector()

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

@mcp.tool()
def search_precedents(sector: str = None, technology_type: str = None) -> str:
    """
    Busca projetos similares aprovados no banco do EditalShield.
    Retorna precedentes relevantes para benchmarking.
    """
    precedents = db.search_precedents(sector=sector, technology_type=technology_type, limit=5)
    
    if not precedents:
        return "⚠️ No precedents found. Database may be unavailable or empty."
    
    output = f"📚 PRECEDENTS FROM EDITALSHIELD DATABASE\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output += f"Found {len(precedents)} approved project(s)\n\n"
    
    for i, p in enumerate(precedents, 1):
        output += f"{i}. Memorial #{p.memorial_id}\n"
        output += f"   Sector: {p.sector} | Tech: {p.technology_type}\n"
        output += f"   Avg Entropy: {p.avg_entropy:.3f} | Patterns: {p.avg_patterns:.1f}\n"
        output += f"   Result: {p.result.upper()}\n\n"
    
    return output

@mcp.tool()
def get_benchmark(innovation_score: int, sector: str = None) -> str:
    """
    Compara o Innovation Score com projetos aprovados históricos.
    Retorna percentil e interpretação.
    """
    stats = db.get_percentile(innovation_score, sector=sector)
    
    output = f"📊 INNOVATION BENCHMARK\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output += f"Your Score: {innovation_score}/100\n"
    output += f"Percentile: {stats['percentile']}th\n"
    output += f"Interpretation: {stats.get('interpretation', 'Average performance')}\n"
    
    if 'note' in stats:
        output += f"\nNote: {stats['note']}\n"
    
    return output

@mcp.tool()
def check_prior_art(keywords: str) -> str:
    """
    Busca patentes existentes (Prior Art) para verificar novidade.
    [EXPERIMENTAL - Uses mock data for now]
    """
    patents = inpi.search_patents(keywords, limit=3)
    
    output = f"🔍 PRIOR ART SEARCH (INPI)\n"
    output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    output += f"Keywords: '{keywords}'\n\n"
    
    if not patents:
        output += "✅ No similar patents found. High novelty potential.\n"
    else:
        output += f"⚠️ Found {len(patents)} potentially similar patent(s):\n\n"
        for i, pat in enumerate(patents, 1):
            output += f"{i}. {pat['patent_id']}\n"
            output += f"   Title: {pat['title']}\n"
            output += f"   Applicant: {pat['applicant']}\n"
            output += f"   Relevance: {pat['relevance']:.0%}\n\n"
    
    return output


def main():
    mcp.run()

if __name__ == "__main__":
    main()
