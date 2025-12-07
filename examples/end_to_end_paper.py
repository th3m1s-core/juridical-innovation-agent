#!/usr/bin/env python3
"""
End-to-End Example: Themis Analysis → Academic Paper
Demonstrates the complete workflow from project analysis to PDF generation.
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
import json


def main():
    """Complete workflow example."""
    
    print("=" * 70)
    print("THEMIS → ACADEMIC PAPER: END-TO-END EXAMPLE")
    print("=" * 70)
    
    # Project description
    project_text = """
    Nossa plataforma de gestão inteligente utiliza algoritmos avançados de 
    machine learning para otimizar processos logísticos em tempo real. O 
    sistema emprega redes neurais convolucionais (CNN) para análise preditiva 
    de demanda e processamento de linguagem natural (NLP) para automação de 
    documentação.
    """
    
    print("\n📝 PROJECT DESCRIPTION:")
    print("-" * 70)
    print(project_text.strip())
    print("-" * 70)
    
    # Step 1: Analyze
    print("\n🔍 STEP 1: ANALYZING WITH THEMIS ENGINE...")
    detector = RiskDetector()
    analysis = detector.analyze(project_text)
    
    print(f"\n✅ Innovation Score: {analysis['innovation_score']}/100")
    print(f"   Vector: H={analysis['vector']['H']:.3f}, Z={analysis['vector']['Z']:.3f}, C={analysis['vector']['C']:.3f}")
    
    # Step 2: Export
    print("\n📄 STEP 2: GENERATING PAPER CONFIGURATION...")
    exporter = PaperExporter(analysis, original_text=project_text)
    paper_config = exporter.to_paper_config(
        title="Automated Innovation Assessment: A Case Study"
    )
    
    print(f"✅ {len(paper_config['sections'])} sections generated")
    
    # Step 3: Save
    print("\n💾 STEP 3: SAVING OUTPUT...")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    config_path = output_dir / "example_paper_config.json"
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(paper_config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved to: {config_path}")
    
    # Next steps
    print("\n🚀 NEXT STEPS:")
    print("=" * 70)
    print("\n1. Generate LaTeX:")
    print(f"   $ paper-gen generate {config_path}")
    print("\n2. Compile PDF:")
    print(f"   $ pdflatex output/paper.tex")
    
    print("\n✅ COMPLETE!")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        sys.exit(1)
