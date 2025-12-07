# 📚 Documentation Index

**Themis Engine - Juridical Innovation Agent**

Welcome to the Themis documentation! This index helps you find the right documentation for your needs.

---

## 🚀 Getting Started

**New to Themis?** Start here:

1. **[README.md](../README.md)** - Project overview and quick start
2. **[Installation Guide](INSTALLATION.md)** - Setup instructions *(coming soon)*
3. **[Quick Start Examples](../examples/)** - Ready-to-run code

---

## 📖 Core Documentation

### Legal & Mathematical Foundation

- **[Mathematical Model](MATHEMATICAL_MODEL.md)** - Themis Vector Space Model (TVSM)
  - Vector formulation: $\vec{I} = [H, Z, C]$
  - Innovation Score calculation
  - Theoretical foundations

- **[Legal References](legal_refs/)** - Brazilian IP Law knowledge base
  - [LPI Highlights](legal_refs/LPI_HIGHLIGHTS.md) - Key articles
  - [TRL Scale](legal_refs/TRL_SCALE.md) - Technology readiness levels

### Features & Capabilities

- **[Paper Generation Guide](PAPER_GENERATION_GUIDE.md)** ⭐ **NEW in v0.2.0**
  - Complete integration documentation
  - Automated academic paper generation
  - Figure generation
  - API reference
  - Examples and troubleshooting

- **[MCP Integration](MCP_INTEGRATION.md)** *(coming soon)*
  - Model Context Protocol setup
  - Available tools
  - Claude Desktop configuration

---

## 🔧 Development

### For Contributors

- **[Integration Task](../INTEGRATION_TASK.md)** - Development roadmap
  - Architecture decisions
  - Implementation phases
  - Testing strategy

- **[Release Notes](../RELEASE_NOTES.md)** - Version history
  - v0.2.0: Paper Generation
  - v0.1.0: Initial release

### Testing

- **[Test Suite](../tests/)** - Automated tests
  - `test_integration.py` - Full integration test
  - `test_figures.py` - Figure generation
  - `test_quick.py` - Quick validation

---

## 💡 Examples

### Code Examples

Located in [`examples/`](../examples/):

- **`end_to_end_paper.py`** - Complete workflow: Analysis → Paper → PDF
- More examples coming soon!

### Use Cases

1. **Innovation Grant Applications**
   - Analyze project description
   - Generate compliance report
   - Export as academic paper

2. **Patent Strategy**
   - Assess patentability risk
   - Get strategic pivot recommendations
   - Document analysis for filing

3. **Research Documentation**
   - Automated paper generation
   - Publication-quality figures
   - LaTeX formatting

---

## 🎓 Academic Resources

### Published Papers

- **[Themis Engine Article (English)](ARTICLE.md)** - Full technical paper
- **[Artigo Themis (Português)](ARTIGO_PT.md)** - Versão em português
- **[LaTeX Source](ARTIGO.tex)** - For compilation

### Presentations

*(Coming soon)*

---

## 🔗 Related Projects

### Symbeon Labs Ecosystem

- **[Academic Paper Generator](https://github.com/symbeon-labs/academic-paper-generator)**
  - Template-based paper generation
  - Multi-format export (LaTeX, Markdown, DOCX)
  - MCP server integration

- **[EditalShield](https://github.com/symbeon-labs/editalshield)**
  - Innovation grant platform
  - PostgreSQL database integration
  - Historical precedent analysis

- **[DocSync](https://github.com/SH1W4/docsync)**
  - AI-powered documentation sync
  - Bidirectional updates
  - MCP capabilities

---

## 📞 Support

### Getting Help

- **Issues:** [GitHub Issues](https://github.com/symbeon-labs/juridical-innovation-agent/issues)
- **Discussions:** [GitHub Discussions](https://github.com/symbeon-labs/juridical-innovation-agent/discussions)
- **Email:** contact@symbeon.com

### Contributing

- **[Contributing Guide](../CONTRIBUTING.md)** *(coming soon)*
- **[Code of Conduct](../CODE_OF_CONDUCT.md)** *(coming soon)*

---

## 📋 Quick Reference

### Common Tasks

| Task | Documentation |
|------|---------------|
| Install Themis | [README.md](../README.md#installation) |
| Analyze a project | [README.md](../README.md#usage) |
| Generate a paper | [PAPER_GENERATION_GUIDE.md](PAPER_GENERATION_GUIDE.md#quick-start) |
| Create figures | [PAPER_GENERATION_GUIDE.md](PAPER_GENERATION_GUIDE.md#generating-specific-figures) |
| Understand the math | [MATHEMATICAL_MODEL.md](MATHEMATICAL_MODEL.md) |
| Use MCP tools | [README.md](../README.md#mcp-integration) |
| Run tests | [README.md](../README.md#testing) |

### API Quick Links

- **Analysis:** `RiskDetector.analyze(text)`
- **Optimization:** `VectorOptimizer.diagnose(vector)`
- **Export:** `PaperExporter.to_paper_config()`
- **Figures:** `FigureGenerator.generate_all(analysis)`

---

## 🗺️ Documentation Roadmap

### Coming Soon

- [ ] Installation Guide
- [ ] MCP Integration Guide
- [ ] API Reference (auto-generated)
- [ ] Video Tutorials
- [ ] Case Studies
- [ ] Best Practices Guide

---

**Last Updated:** December 7, 2025  
**Version:** 0.2.0  
**Maintained by:** [Symbeon Labs](https://github.com/symbeon-labs)
