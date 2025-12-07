# 🔗 Themis ↔ Paper Generator Integration Guide

**Complete documentation for the automated academic paper generation from Themis analysis**

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Detailed Usage](#detailed-usage)
6. [API Reference](#api-reference)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)

---

## 🌟 Overview

The Themis-Paper Generator integration enables **automatic transformation** of innovation analysis results into publication-ready academic papers. This creates a complete workflow from project analysis to scientific documentation.

### Key Features

- ✅ **Automated Section Generation**: Introduction, Methodology, Results, Conclusion
- ✅ **Publication-Quality Figures**: 3D vectors, radar charts, score gauges
- ✅ **LaTeX Formatting**: Mathematical equations, proper citations
- ✅ **Multi-Template Support**: IEEE, ABNT, arXiv
- ✅ **MCP Integration**: Seamless agent-to-agent communication

### Workflow

```
User Input (Project Description)
    ↓
Themis Engine (Analysis)
    ├─→ Innovation Score (0-100)
    ├─→ Vector Components [H, Z, C]
    ├─→ Risk Detection
    └─→ Strategic Recommendations
    ↓
Paper Exporter (Conversion)
    ├─→ Generate Abstract
    ├─→ Create Sections
    ├─→ Generate Figures (3D, Radar, Gauge)
    └─→ Format References
    ↓
JSON Configuration
    ↓
Paper Generator (Rendering)
    ├─→ Apply Template (IEEE/ABNT/arXiv)
    ├─→ Embed Figures
    └─→ Compile LaTeX
    ↓
Output: Academic Paper (PDF)
```

---

## 🏗️ Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    Themis Engine                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ RiskDetector │  │   Optimizer  │  │  Knowledge   │  │
│  │              │  │              │  │     Base     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              Export Module (NEW)                        │
│  ┌──────────────┐  ┌──────────────┐                     │
│  │PaperExporter │  │FigureGenerator│                    │
│  │              │  │              │                     │
│  │ • Sections   │  │ • 3D Vector  │                     │
│  │ • Abstract   │  │ • Radar      │                     │
│  │ • References │  │ • Gauge      │                     │
│  └──────────────┘  └──────────────┘                     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│           Academic Paper Generator                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Templates   │  │   Renderer   │  │   Compiler   │  │
│  │ • IEEE       │  │   (Jinja2)   │  │  (pdflatex)  │  │
│  │ • ABNT       │  │              │  │              │  │
│  │ • arXiv      │  │              │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Data Flow

```python
# 1. Analysis
analysis = detector.analyze(project_text)
# → {'innovation_score': 98, 'vector': {'H': 0.96, 'Z': 1.0, 'C': 1.0}, ...}

# 2. Export
exporter = PaperExporter(analysis, original_text=project_text)
paper_config = exporter.to_paper_config(title="My Paper")
# → {'metadata': {...}, 'sections': [...], 'references': [...]}

# 3. Generate Figures
figure_paths = exporter._generate_figures()
# → ['output/figures/themis_vector_3d.png', ...]

# 4. Render Paper
gen = PaperGenerator(template="ieee")
gen.config = PaperConfig(**paper_config)
gen.generate("output/paper.tex")
# → output/paper.tex

# 5. Compile PDF
gen.compile_pdf("output/paper.tex")
# → output/paper.pdf
```

---

## 📦 Installation

### Prerequisites

- Python 3.10+
- LaTeX distribution (for PDF compilation)
  - **Windows**: MiKTeX or TeX Live
  - **Linux**: `sudo apt-get install texlive-full`
  - **macOS**: MacTeX

### Step 1: Install Themis Engine

```bash
cd juridical-innovation-agent
pip install -e ".[figures]"  # Includes matplotlib, seaborn, numpy
```

### Step 2: Install Paper Generator

```bash
cd ../academic-paper-generator
pip install -e .
```

### Step 3: Verify Installation

```bash
# Test Themis
python -c "from themis.export import PaperExporter; print('✅ Themis OK')"

# Test Paper Generator
paper-gen --help

# Test Figures
python -c "from themis.export.figures import FigureGenerator; print('✅ Figures OK')"
```

---

## 🚀 Quick Start

### Option 1: Via MCP Tool (Recommended)

```python
# In Claude Desktop or Cline with Themis MCP server running

User: "Analyze this project and generate a paper"

Themis: [Calls generate_analysis_paper(text)]
>>> ✅ Paper configuration generated!
>>> Innovation Score: 73/100
>>> Config saved to: output/paper_config.json
>>> 
>>> To generate the paper, run:
>>>   paper-gen generate output/paper_config.json --template ieee
```

### Option 2: Programmatic

```python
from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
import json

# 1. Analyze
detector = RiskDetector()
analysis = detector.analyze("""
    Our platform uses machine learning algorithms to optimize
    inventory management in real-time...
""")

# 2. Export
exporter = PaperExporter(analysis)
config = exporter.to_paper_config(title="Innovation Analysis Report")

# 3. Save
with open('output/paper_config.json', 'w') as f:
    json.dump(config, f, indent=2)

# 4. Generate (via CLI)
# $ paper-gen generate output/paper_config.json --template ieee
```

### Option 3: One-Liner (Bash)

```bash
# Analyze, export, and generate in one command
python -c "
from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
import json

text = open('project_description.txt').read()
analysis = RiskDetector().analyze(text)
config = PaperExporter(analysis, text).to_paper_config()

with open('output/config.json', 'w') as f:
    json.dump(config, f, indent=2)
" && paper-gen generate output/config.json
```

---

## 📖 Detailed Usage

### Customizing Paper Metadata

```python
from themis.export import PaperExporter

exporter = PaperExporter(analysis, original_text=project_text)

config = exporter.to_paper_config(
    title="Advanced Innovation Assessment Using Vector Space Models",
    authors=[
        {
            "name": "Dr. Jane Smith",
            "affiliation": "University of Innovation",
            "email": "jane@university.edu"
        },
        {
            "name": "John Doe",
            "affiliation": "Symbeon Labs"
        }
    ]
)
```

### Generating Specific Figures

```python
from themis.export.figures import FigureGenerator

fig_gen = FigureGenerator(output_dir="custom/path")

# Generate all figures
all_figs = fig_gen.generate_all(analysis, prefix="my_paper")

# Or generate individually
vector_3d = fig_gen.plot_innovation_vector_3d(
    analysis['vector'],
    filename="custom_vector.png"
)

radar = fig_gen.plot_component_radar(
    analysis['vector'],
    filename="custom_radar.png"
)

gauge = fig_gen.plot_score_gauge(
    analysis['innovation_score'],
    filename="custom_gauge.png"
)
```

### Selecting Templates

```python
# IEEE Conference Format (default)
config = exporter.to_paper_config()
config['template'] = 'ieee'

# ABNT (Brazilian Standards)
config['template'] = 'abnt'

# arXiv Preprint
config['template'] = 'arxiv'
```

### Disabling Figure Generation

```python
# If you don't have matplotlib installed or want text-only
exporter._generate_figures = lambda: []
config = exporter.to_paper_config()
```

---

## 🔧 API Reference

### `PaperExporter`

**Class:** `themis.export.PaperExporter`

#### Constructor

```python
PaperExporter(analysis_result: Dict, original_text: str = "")
```

**Parameters:**
- `analysis_result`: Output from `detector.analyze()`
- `original_text`: Original project description (optional)

#### Methods

##### `to_paper_config()`

```python
to_paper_config(
    title: str = None,
    authors: List[Dict] = None
) -> Dict
```

Converts Themis analysis to Paper Generator configuration.

**Returns:** Dictionary with keys:
- `metadata`: Title, authors, abstract, keywords, date
- `sections`: List of section dicts (title, content, figures)
- `references`: List of bibliographic references
- `template`: Template name

##### `_generate_figures()`

```python
_generate_figures() -> List[str]
```

Generates all visualization figures.

**Returns:** List of figure file paths

---

### `FigureGenerator`

**Class:** `themis.export.figures.FigureGenerator`

#### Constructor

```python
FigureGenerator(output_dir: str = "output/figures")
```

#### Methods

##### `generate_all()`

```python
generate_all(analysis: Dict, prefix: str = "fig") -> List[str]
```

Generates all figure types for an analysis.

**Returns:** List of generated figure paths

##### `plot_innovation_vector_3d()`

```python
plot_innovation_vector_3d(
    vector: Dict[str, float],
    filename: str = "vector_3d.png"
) -> str
```

Creates 3D visualization of innovation vector.

##### `plot_component_radar()`

```python
plot_component_radar(
    vector: Dict[str, float],
    filename: str = "radar.png"
) -> str
```

Creates radar chart of vector components.

##### `plot_score_gauge()`

```python
plot_score_gauge(
    score: int,
    filename: str = "score_gauge.png"
) -> str
```

Creates gauge chart for innovation score.

---

## 💡 Examples

### Example 1: Complete Workflow

```python
#!/usr/bin/env python3
"""
Complete example: Analysis → Paper → PDF
"""

from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
from paper_gen import PaperGenerator
import json

# Sample project description
project_text = """
Our platform utilizes advanced machine learning algorithms
to optimize supply chain logistics in real-time. The system
employs convolutional neural networks (CNN) for demand forecasting
and natural language processing (NLP) for automated documentation.
"""

# Step 1: Analyze with Themis
print("🔍 Analyzing project...")
detector = RiskDetector()
analysis = detector.analyze(project_text)
print(f"✅ Innovation Score: {analysis['innovation_score']}/100")

# Step 2: Export to paper config
print("\n📄 Generating paper configuration...")
exporter = PaperExporter(analysis, original_text=project_text)
config = exporter.to_paper_config(
    title="Automated Innovation Assessment: A Case Study"
)

# Save config
with open('output/paper_config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print(f"✅ Config saved with {len(config['sections'])} sections")
print(f"✅ Generated {len([s for s in config['sections'] if s.get('figures')])} figures")

# Step 3: Generate LaTeX
print("\n📝 Generating LaTeX...")
gen = PaperGenerator(template="ieee")
# Note: Paper Generator expects YAML, so we'd need to convert or use JSON directly
# For now, save as JSON and convert manually or use paper-gen CLI

print("\n✅ Complete! Next steps:")
print("   1. paper-gen generate output/paper_config.json")
print("   2. pdflatex output/paper.tex")
```

### Example 2: Batch Processing

```python
"""
Process multiple projects and generate papers
"""

import os
from pathlib import Path
from themis.reasoning.detector import RiskDetector
from themis.export import PaperExporter
import json

# Directory with project descriptions
projects_dir = Path("projects")
output_dir = Path("output/papers")
output_dir.mkdir(parents=True, exist_ok=True)

detector = RiskDetector()

for project_file in projects_dir.glob("*.txt"):
    print(f"\n📁 Processing: {project_file.name}")
    
    # Read project
    text = project_file.read_text(encoding='utf-8')
    
    # Analyze
    analysis = detector.analyze(text)
    score = analysis['innovation_score']
    
    # Export
    exporter = PaperExporter(analysis, original_text=text)
    config = exporter.to_paper_config(
        title=f"Analysis: {project_file.stem}"
    )
    
    # Save
    output_file = output_dir / f"{project_file.stem}_config.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Score: {score}/100 → {output_file}")
```

---

## 🔧 Troubleshooting

### Issue: Figures not generating

**Symptom:** Paper config created but no figures in `output/figures/`

**Solution:**
```bash
# Install visualization dependencies
pip install matplotlib seaborn numpy

# Or install with extras
pip install -e ".[figures]"
```

### Issue: LaTeX compilation fails

**Symptom:** `pdflatex: command not found`

**Solution:**
- **Windows:** Install MiKTeX from https://miktex.org/
- **Linux:** `sudo apt-get install texlive-full`
- **macOS:** Install MacTeX from https://www.tug.org/mactex/

### Issue: ModuleNotFoundError for seaborn

**Symptom:** Import error even after installation

**Solution:**
```bash
# Ensure you're using the correct Python environment
which python  # Should point to your venv

# Reinstall in correct environment
pip uninstall seaborn
pip install seaborn
```

### Issue: Figures have wrong paths in LaTeX

**Symptom:** LaTeX can't find figure files

**Solution:**
```python
# Use relative paths from LaTeX working directory
# Figures are automatically converted to forward slashes
# Ensure figures are in output/figures/ relative to .tex file
```

---

## 📚 Additional Resources

- [Themis Engine Documentation](../README.md)
- [Paper Generator Documentation](../../academic-paper-generator/README.md)
- [Mathematical Model](../docs/MATHEMATICAL_MODEL.md)
- [MCP Integration Guide](../docs/MCP_INTEGRATION.md)

---

**Developed by [Symbeon Labs](https://github.com/symbeon-labs)**  
*Innovation Infrastructure for the Brazilian Ecosystem*
