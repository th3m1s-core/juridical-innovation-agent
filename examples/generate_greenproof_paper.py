"""
GreenProof × Themis: Scientific Paper Generator
Generates publication-ready figures and paper config from Trinity Consensus analysis.

Usage:
    cd juridical-innovation-agent
    python examples/generate_greenproof_paper.py
"""

import sys
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from themis.export.paper_exporter import PaperExporter
try:
    from themis.export.figures import FigureGenerator
    HAS_FIGURES = True
except ImportError:
    print("⚠️ Warning: seaborn or matplotlib not found. Figure generation will be skipped.")
    HAS_FIGURES = False


# ─────────────────────────────────────────────────────────────────
# GreenProof Trinity Consensus Analysis (Vetor [H, Z, C])
# Based on Themis audit scores from expert_audit_report.md
# ─────────────────────────────────────────────────────────────────
GREENPROOF_ANALYSIS = {
    "innovation_score": 78,
    "vector": {
        "H": 0.89,   # Entropy: ZK-SNARKs + Groth16 + CCIP = high technical density
        "Z": 0.84,   # Zipf: specialized vocabulary (Groth16, NDVI, RWA, ERC-721)
        "C": 0.61,   # Compliance: requires Art.10 linguistic pivot (done via README update)
    },
    "patterns_found": {
        "juridical_pivot_required": ["software_as_such", "esg_platform_framing"],
        "strong_technical_claims": ["zk_snarks", "distributed_consensus", "cryptographic_proof"],
        "regulatory_alignment": ["sfdr_compatible", "csrd_compliant"],
    },
    "suggestions": [
        "Frame as 'cryptographic method' not 'ESG software' (LPI Art.8 vs Art.10)",
        "Emphasize privacy-preserving property of ZK proofs for INPI filing",
        "Highlight tri-oracle independence as novel distributed validation mechanism",
        "Reference Groth16 pairing-based arguments in technical claims",
    ],
}

GREENPROOF_TEXT = """
GreenProof implements a cryptographic method for environmental attestation of Real-World Assets
via Trinity Consensus — a distributed multi-oracle protocol requiring a 2/3 quorum across
Physical (IoT/Satellite), Juridical (Th3m1s), and Ethical (SEVE) verification shards.
Upon consensus, a Groth16 zero-knowledge proof is generated, enabling on-chain certification
without exposing proprietary industrial telemetry. The resulting ERC-721 certificate is
portable across EVM chains via Chainlink CCIP.
"""

PAPER_AUTHORS = [
    {
        "name": "Symbeon Labs Research Team",
        "affiliation": "Symbeon Labs — Sovereign Innovation Infrastructure",
        "email": "research@symbeon.io",
    }
]

PAPER_TITLE = (
    "A Cryptographic Method for Real-World Asset Environmental Attestation "
    "via Distributed Multi-Oracle Consensus and Zero-Knowledge Proofs"
)


def main():
    print("🦅 GreenProof × Themis: Paper Generator")
    print("=" * 55)

    # ── 1. Generate Figures ────────────────────────────────────────
    if HAS_FIGURES:
        print("\n📊 Generating publication figures...")
        fig_gen = FigureGenerator(output_dir="output/greenproof_figures")
        figures = fig_gen.generate_all(GREENPROOF_ANALYSIS, prefix="greenproof")
        print(f"   ✅ {len(figures)} figures saved to output/greenproof_figures/")
        for f in figures:
            print(f"      → {Path(f).name}")
    else:
        print("\n📊 Skipping figure generation (missing dependencies)...")
        figures = []

    # ── 2. Generate Paper Config ───────────────────────────────────
    print("\n📄 Generating paper configuration...")
    exporter = PaperExporter(GREENPROOF_ANALYSIS, original_text=GREENPROOF_TEXT)
    paper_config = exporter.to_paper_config(
        title=PAPER_TITLE,
        authors=PAPER_AUTHORS,
    )
    # Inject GreenProof-specific references
    paper_config["references"] += [
        {
            "id": "groth2016",
            "type": "inproceedings",
            "title": "On the Size of Pairing-Based Non-Interactive Arguments",
            "author": "Groth, J.",
            "venue": "EUROCRYPT",
            "year": 2016,
        },
        {
            "id": "ben-sasson2014",
            "type": "inproceedings",
            "title": "Succinct Non-Interactive Arguments for a von Neumann Architecture",
            "author": "Ben-Sasson et al.",
            "venue": "USENIX Security",
            "year": 2014,
        },
        {
            "id": "chainlink-ccip",
            "type": "misc",
            "title": "Chainlink Cross-Chain Interoperability Protocol (CCIP) Documentation",
            "author": "Chainlink Foundation",
            "year": 2024,
            "url": "https://docs.chain.link/ccip",
        },
    ]
    paper_config["metadata"]["keywords"] += [
        "Zero-Knowledge Proofs",
        "Real-World Assets",
        "Chainlink",
        "Trinity Consensus",
    ]

    # ── 3. Save Paper Config ───────────────────────────────────────
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    config_path = output_dir / "greenproof_paper_config.json"
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(paper_config, f, indent=2, ensure_ascii=False)
    print(f"   ✅ Paper config saved → {config_path}")

    # ── 4. Print Summary ───────────────────────────────────────────
    print("\n" + "=" * 55)
    print("✅ DONE — GreenProof paper assets generated!")
    print(f"   📊 Figures:      output/greenproof_figures/ ({len(figures)} files)")
    print(f"   📄 Paper config: {config_path}")
    print(f"   🎯 Themis Score: {GREENPROOF_ANALYSIS['innovation_score']}/100")
    print("\nNext: Feed config to Academic Paper Gen to compile LaTeX → PDF")
    print("=" * 55)


if __name__ == "__main__":
    main()
