"""
Quick Test: Themis Paper Export (without figures)
Tests the integration without matplotlib dependencies.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
import json


def test_export_without_figures():
    """Test paper export without figure generation."""
    print("=" * 60)
    print("QUICK TEST: Paper Export (No Figures)")
    print("=" * 60)
    
    # Sample text
    sample_text = """
    Nossa plataforma utiliza algoritmos de machine learning para otimizar
    a gestão de estoque em tempo real. O sistema processa dados de vendas
    históricos através de redes neurais convolucionais (CNN) e aplica
    técnicas de processamento de linguagem natural (NLP) para prever demanda.
    """
    
    # Analyze
    detector = RiskDetector()
    analysis = detector.analyze(sample_text)
    
    print(f"\n✅ Analysis: {analysis['innovation_score']}/100")
    
    # Export (disable figure generation)
    exporter = PaperExporter(analysis, original_text=sample_text)
    
    # Temporarily disable figure generation
    original_method = exporter._generate_figures
    exporter._generate_figures = lambda: []  # Return empty list
    
    paper_config = exporter.to_paper_config(
        title="Quick Test Paper"
    )
    
    # Restore
    exporter._generate_figures = original_method
    
    print(f"✅ Paper Config Generated!")
    print(f"   Sections: {len(paper_config['sections'])}")
    print(f"   References: {len(paper_config['references'])}")
    
    # Save
    os.makedirs('output', exist_ok=True)
    with open('output/quick_test_config.json', 'w', encoding='utf-8') as f:
        json.dump(paper_config, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Saved to: output/quick_test_config.json")
    print("\n" + "=" * 60)
    print("✅ QUICK TEST PASSED!")
    print("=" * 60)
    print("\nNote: Figure generation requires matplotlib/seaborn")
    print("Install with: pip install matplotlib seaborn numpy")


if __name__ == "__main__":
    test_export_without_figures()
