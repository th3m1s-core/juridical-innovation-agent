# ⚖️ Themis Engine 
### Juridical Innovation Agent

<p align="center">
  <img src="docs/assets/banner.png" width="100%" alt="Themis AI Interface" style="border-radius: 10px; margin-bottom: 20px;">
</p>

<p align="center">
  <img src="docs/assets/logo.png" width="150" alt="Themis Logo">
</p>

<p align="center">
  <img src="docs/assets/neural_console.svg" width="100%" alt="Themis Neural Console">
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Architecture-MCP_Server-00D9FF?style=for-the-badge&logo=serverless&logoColor=black" alt="MCP"></a>
  <a href="#"><img src="https://img.shields.io/badge/Intelligence-Bayesian_%2B_Heuristic-FFD700?style=for-the-badge&logo=openai&logoColor=black" alt="AI"></a>
  <a href="#"><img src="https://img.shields.io/badge/Legal_Base-LPI_Brazil-00D9FF?style=for-the-badge&logo=law&logoColor=black" alt="Legal"></a>
</p>

---

## 🌌 Overview

**Themis Engine** is not just a validator; it's a **Juridical Co-Founder**. 

Designed by [Symbeon Labs](https://github.com/symbeon-labs), this AI agent proactively analyzes technical descriptions against Brazilian Innovation Law (LPI 9.279/96) to transform "business ideas" into **patentable technological assets**.

> *"Themis doesn't just say 'NO'. It says 'PIVOT TO THIS'."*

---

## 🧠 Cognitive Capabilities

### 1. 🛡️ Risk & Patentability Detection
It analyzes text entropy, Zipfian deviation, and sensitive patterns (RegEx) to calculate an **IP Exposure Score**.

```mermaid
graph LR
    A[Input Text] --> B(Entropy Analysis)
    A --> C(Pattern Recognition)
    A --> D(Tech Density / Zipf)
    B & C & D --> E{Themis Engine}
    E -->|Safe| F[TRL Classification]
    E -->|Risk High| G[Innovation Pivot]
```

### 2. 💡 Proactive Innovation Pivots
Detects if a project falls under **Art. 10 Constraints** (Software as such) and suggests technical framings to bypass it.

| 🚫 User Input (Risk) | ✅ Themis Suggestion (Patentable) |
| :--- | :--- |
| "A software to manage sales" | "A method for distributed transaction processing" |
| "Dashboard for metrics" | "Real-time data visualization engine optimization" |


### 3. 📐 Vector-Guided Optimization (Strategic Intelligence)

Themis doesn't just score—it **diagnoses and prescribes**.

Using a **3D Vector Space Model** ($\vec{I} = [H, Z, C]$), it identifies which dimension is limiting your Innovation Score:
- **H (Entropy):** Information density
- **Z (Zipf):** Technical vocabulary sophistication  
- **C (Compliance):** Legal safety from Art. 10 blockers

**Example Output:**
```
🎯 BOTTLENECK IDENTIFIED: C (Compliance)
   Current Value: 0.42
   Potential Gain: +23% if optimized

💡 RECOMMENDED ACTIONS:
   ⚖️ PIVOT: Focus on the TECHNICAL effect, not business outcome
   ⚖️ Instead of: 'automates sales tracking'
   ⚖️ Say: 'real-time event stream processing with sub-second latency'

📈 IMPACT SIMULATION (if C improves 20%):
   Current Score: 58/100
   Projected Score: 71/100
   Expected Gain: +13 points
```

📖 **[See Mathematical Model](docs/MATHEMATICAL_MODEL.md)** for the full vector space formulation.

### 4. 📚 Deep Legal Context (RAG-Lite)
Powered by a curated knowledge base of:
- **LPI 9.279/96** (Industrial Property Law)
- **INPI Guidelines** for Computer Implemented Inventions
- **TRL Scales** (NASA/ABNT)

---

## 🔌 Integration (Model Context Protocol)

Themis is built as an **MCP Server**, ready to plug into Claude, Cline, or any agentic workflow.

### Quick Start

```bash
# 1. Clone & Install
git clone https://github.com/symbeon-labs/juridical-innovation-agent.git
cd juridical-innovation-agent
pip install -e .

# 2. Run Inspector to Test
npx @modelcontextprotocol/inspector python -m themis.server
```

### Configuration (`claude_desktop_config.json`)

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

## 🛠️ Tech Stack

- **Core:** Python 3.10+
- **Protocol:** FastMCP (Model Context Protocol)
- **Reasoning:** Custom Heuristic Engine + Pattern Weights
- **Knowledge:** Markdown-based RAG

---

<div align="center">
  <sub>Built with 💙 by <b>Symbeon Labs</b> • <i>Innovation Infrastructure for the Brazilian Ecosystem</i></sub>
</div>
