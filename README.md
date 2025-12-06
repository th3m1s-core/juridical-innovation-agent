# ⚖️ Juridical Innovation Agent (Themis Engine)

**Themis** is a specialized AI agent designed to analyze technological projects, assess patentability according to Brazilian Law (LPI 9.279/96), and proactively suggest innovation pivots to increase grant success rates.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Alpha-orange" alt="Status">
  <img src="https://img.shields.io/badge/Focus-Legal_Tech-blue" alt="Focus">
  <img src="https://img.shields.io/badge/Compliance-LPI_9.279/96-green" alt="Compliance">
</p>

---

## 🚀 Capabilities

### 1. Patentability Analysis
Evaluates projects against key LPI criteria:
- **Novelty (Art. 11)**
- **Inventive Step (Art. 13)**
- **Industrial Application (Art. 15)**
- **Software Exclusions (Art. 10 - CII)**

### 2. Proactive Innovation Pivot
Instead of just rejecting, Themis suggests technical shifts:
> *"Your project focuses on business rules (Art. 10 blockage). By focusing on the data obfuscation algorithm, you reach TRL 4 and patentability."*

### 3. TRL Classification
Automatically classifies project maturity based on NASA/ABNT scales (TRL 1-9).

---

## 🛠️ Architecture

It functions as a **Model Context Protocol (MCP)** server, exposing tools to other agents (like EditalShield or Claude).

- **Core Module:** `src/themis`
- **Knowledge Base:** `docs/legal_refs` (LPI, INPI Manuals)
- **Interface:** MCP Tools (`analyze_patentability`, `suggest_pivot`)

## 📦 Installation

```bash
pip install -e .
```

## 🔌 Usage (MCP)

Configure in your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "themis": {
      "command": "python",
      "args": ["-m", "themis.server"]
    }
  }
}
```

---

**Developed by [Symbeon Labs](https://github.com/symbeon-labs)**
*Innovation Infrastructure for the Brazilian Ecosystem*
