"""
Test Figure Generation
Tests the matplotlib/seaborn figure generation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from themis.reasoning.detector import RiskDetector
from themis.export.figures import FigureGenerator


def test_figure_generation():
    """Test all figure types."""
    print("=" * 60)
    print("TEST: Figure Generation")
    print("=" * 60)
    
    # Sample analysis
    sample_text = """
    Nossa plataforma utiliza algoritmos de machine learning para otimizar
    a gestão de estoque em tempo real. O sistema processa dados de vendas
    históricos através de redes neurais convolucionais (CNN).
    """
    
    detector = RiskDetector()
    analysis = detector.analyze(sample_text)
    
    print(f"\n📊 Generating figures for score: {analysis['innovation_score']}/100")
    
    # Generate figures
    fig_gen = FigureGenerator(output_dir="output/figures")
    figure_paths = fig_gen.generate_all(analysis, prefix="test")
    
    print(f"\n✅ Generated {len(figure_paths)} figures:")
    for path in figure_paths:
        print(f"   - {path}")
    
    # Verify files exist
    all_exist = all(os.path.exists(p) for p in figure_paths)
    
    if all_exist:
        print(f"\n✅ ALL FIGURES GENERATED SUCCESSFULLY!")
        print(f"\nFigures saved to: output/figures/")
    else:
        print(f"\n❌ Some figures failed to generate")
        return False
    
    return True


if __name__ == "__main__":
    try:
        success = test_figure_generation()
        if success:
            print("\n" + "=" * 60)
            print("✅ FIGURE GENERATION TEST PASSED!")
            print("=" * 60)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
