# ⚖️ Themis: Validation Engine

---
name: themis
description: Juridical compliance, risk detection, and structural project validation.
---

## 1. Engine Mission (VALIDATION)
**Themis** acts as the supreme auditor. It ensures that the project narrative is legally defensible, technically robust, and administratively compliant with the target edital rules.

## 2. Core Technical Domain
- **Legal NLP**: Analyzing project text for risky keywords or claims that could trigger rejection.
- **Compliance Mapping**: Cross-referencing project segments with specific edital items (Anexo I, II, etc.).
- **Risk Scoring**: Generating a "Vulnerability Map" to guide the innovator.

## 3. Key Directives
- **Non-Negotiable Compliance**: If a legal requirement isn't met, flag it as CRITICAL.
- **Structured Feedback**: Avoid vague advice; provide specific suggestions for text refinement.
- **Biocybernetic Tone**: Responses should be precise, data-driven, and authoritative.

## 4. Interaction Protocol
- **Input**: Project Text + Target Edital Metadata (from EditalShield).
- **Output**: Compliance Checklist + Risk Score + Suggested Refinements.
- **Handoff**: Sends validated content to **Academic-Gen** for final formatting.

## 5. Sovereign Architecture & Neural Nexus (L1-L3)
- **Mother Protocol (L1 Hub)**: O `juridical-innovation-agent` atua como o Núcleo Atomístico determinístico.
- **Embedded Submodules**: Este motor L1 é nativamente embutido em plataformas como o **GreenProof** (via Git Submodules), garantindo que atualizações no Hexágono Legislativo se propaguem instantaneamente.
- **Neural Cortex (L3)**: Orquestrado pelo `th3m1s-sovereign-cortex`, que gerencia o fine-tuning local do modelo Qwen-2.5-Coder através do `dataset_forge`.

```mermaid
graph TD
    subgraph L3_Neural[L3: Sovereign Cortex - Inteligência]
        A[Qwen-2.5-Coder Fine-tuned]
        B[Multi-Agent Orchestrator]
    end

    subgraph L1_Atoms[L1: Protocolo Mãe - Motores]
        C[Themis TVSM Core]
        D[Juridical Innovation Agent - L1]
        E[EditalShield]
    end

    subgraph Ecosystem[Aplicações Hospedeiras]
        F[GreenProof Platform]
        G((Themis Engine Submodule))
    end

    L3_Neural -->|Orquestra| L1_Atoms
    L1_Atoms -->|Fornece L1 Engine| G
    F -->|Hospeda| G
    G -.->|Atualiza a partir de| D
```

## 6. Knowledge Path
- Core Agency: `engines/L3-Public/themis/src/agents/`
- Ruleset: `engines/L3-Public/themis/rules/compliance/`
- Neural Hub: `th3m1s-sovereign-cortex/`

---
**Component**: VALIDATION
**Architecture Layer**: L3-Public
