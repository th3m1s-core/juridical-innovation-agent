# 🎯 INTEGRATION TASK: Themis ↔ Paper Generator

## 📋 Super Scope

**Objetivo:** Integrar o Themis Engine com o Academic Paper Generator para que análises de inovação possam ser automaticamente transformadas em artigos científicos publicáveis.

**Resultado Esperado:** Um agente jurídico que não apenas analisa projetos, mas também documenta suas análises em formato acadêmico, gerando papers prontos para submissão.

---

## 🗺️ Architecture Overview

```
User Input (Memorial)
    ↓
Themis Engine (Analysis)
    ├─→ Vector Analysis (H, Z, C)
    ├─→ Risk Detection
    ├─→ Optimization Suggestions
    └─→ Benchmark Data
    ↓
[NEW] Paper Generator Integration
    ├─→ Structure Results as Paper Sections
    ├─→ Generate Figures (Score plots, Vector diagrams)
    ├─→ Format References (LPI, TRL, precedents)
    └─→ Compile to LaTeX/PDF
    ↓
Output: Academic Paper (.tex + .pdf)
```

---

## ✅ TODO List

### Phase 1: Data Bridge (Themis → Paper Gen)
- [ ] 1.1 Create `export_to_paper_config()` method in Themis
- [ ] 1.2 Map Themis analysis results to Paper sections
- [ ] 1.3 Generate automatic abstract from analysis summary
- [ ] 1.4 Extract keywords from detected patterns

### Phase 2: MCP Integration
- [ ] 2.1 Add Paper Generator as MCP client in Themis
- [ ] 2.2 Create `generate_case_study_paper()` tool in Themis
- [ ] 2.3 Implement automatic template selection (IEEE for tech, ABNT for Brazil)
- [ ] 2.4 Handle errors gracefully (Paper Gen unavailable, etc.)

### Phase 3: Figure Generation
- [ ] 3.1 Create vector diagram generator (3D plot of [H, Z, C])
- [ ] 3.2 Generate score comparison chart (before/after optimization)
- [ ] 3.3 Create risk heatmap (pattern categories)
- [ ] 3.4 Save figures to `output/figures/` directory

### Phase 4: Content Enrichment
- [ ] 4.1 Auto-generate Introduction from project description
- [ ] 4.2 Create Methodology section (TVSM explanation)
- [ ] 4.3 Format Results section (scores, vectors, recommendations)
- [ ] 4.4 Generate Conclusion with strategic insights

### Phase 5: Testing & Examples
- [ ] 5.1 Create example: Generate paper from Themis analysis
- [ ] 5.2 Test with real memorial data
- [ ] 5.3 Validate LaTeX compilation
- [ ] 5.4 Create demo script/notebook

### Phase 6: Documentation
- [ ] 6.1 Update Themis README with paper generation feature
- [ ] 6.2 Create integration guide (INTEGRATION.md)
- [ ] 6.3 Add example YAML configs
- [ ] 6.4 Document MCP chain (Themis → Paper Gen)

---

## 🔧 Implementation Plan

### Step 1: Create Themis Export Module
**File:** `src/themis/export/paper_exporter.py`
**Purpose:** Convert Themis analysis to Paper Generator format

```python
class PaperExporter:
    def __init__(self, analysis_result: dict):
        self.analysis = analysis_result
    
    def to_paper_config(self) -> dict:
        """Convert Themis analysis to Paper Generator config."""
        pass
    
    def generate_figures(self) -> List[str]:
        """Create visualization figures."""
        pass
```

### Step 2: Add MCP Tool to Themis
**File:** `src/themis/server.py`
**Tool:** `generate_analysis_paper(text, template="ieee")`

### Step 3: Create Figure Generator
**File:** `src/themis/export/figures.py`
**Functions:**
- `plot_innovation_vector(H, Z, C) -> str`
- `plot_score_comparison(before, after) -> str`
- `plot_risk_heatmap(patterns) -> str`

### Step 4: Integration Testing
**File:** `examples/themis_to_paper.py`
**Demo:** End-to-end example

---

## 📊 Success Metrics

- ✅ Themis can generate a complete paper from a single analysis
- ✅ Paper includes all sections (Abstract, Intro, Methods, Results, Conclusion)
- ✅ Figures are automatically generated and embedded
- ✅ LaTeX compiles without errors
- ✅ PDF is publication-ready (IEEE/ABNT format)

---

## 🚨 Potential Challenges

1. **Figure Generation:** Matplotlib/Plotly dependency, file path management
2. **LaTeX Compilation:** Requires pdflatex installed on system
3. **MCP Communication:** Handling async calls between agents
4. **Data Mapping:** Ensuring Themis output matches Paper Gen input schema

---

## 🎯 Execution Order

1. ✅ Create TODO (this file)
2. → Implement Phase 1 (Data Bridge)
3. → Implement Phase 2 (MCP Integration)
4. → Implement Phase 3 (Figures)
5. → Test & Document
6. → Commit & Push

---

**Status:** 📝 Planning Complete - Ready for Execution
**Next Action:** Start Phase 1.1 - Create export module
