# ⚖️ Themis Engine 
### Juridical Innovation Agent

<p align="center">
  <img src="docs/assets/logo.png" width="200" alt="Themis Logo">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=2000&pause=500&color=00D9FF&center=true&vCenter=true&width=800&lines=%3E+Initializing+Themis+Juridical+Core...;%3E+Loading+LPI+9.279%2F96+Knowledge+Base...;%3E+Analyzing+Innovation+Project...;%3E+Status:+PATENTABLE+WITH+MODIFICATIONS" alt="Themis Thinking" />
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

### 3. 📚 Deep Legal Context (RAG-Lite)
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
