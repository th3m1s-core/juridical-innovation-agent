"""
Paper Exporter Module
Converts Themis analysis results to Academic Paper Generator format.
"""

from typing import Dict, List
from datetime import datetime


class PaperExporter:
    """
    Exports Themis analysis results as paper-ready configuration.
    """
    
    def __init__(self, analysis_result: Dict, original_text: str = ""):
        """
        Initialize exporter with analysis results.
        
        Args:
            analysis_result: Output from detector.analyze()
            original_text: Original project description analyzed
        """
        self.analysis = analysis_result
        self.original_text = original_text
    
    def to_paper_config(self, title: str = None, authors: List[Dict] = None) -> Dict:
        """
        Convert Themis analysis to Paper Generator configuration.
        
        Args:
            title: Paper title (auto-generated if None)
            authors: List of author dicts (default: Symbeon Labs)
        
        Returns:
            Dictionary compatible with PaperConfig model
        """
        # Auto-generate title if not provided
        if not title:
            score = self.analysis.get('innovation_score', 0)
            title = f"Innovation Analysis Report: Score {score}/100"
        
        # Default authors
        if not authors:
            authors = [{
                "name": "Themis Engine",
                "affiliation": "Symbeon Labs",
                "email": "contact@symbeon.com"
            }]
        
        # Generate abstract
        abstract = self._generate_abstract()
        
        # Generate figures
        figure_paths = self._generate_figures()
        
        # Generate sections (with figures)
        sections = self._generate_sections(figure_paths)
        
        # Generate references
        references = self._generate_references()
        
        # Extract keywords
        keywords = self._extract_keywords()
        
        return {
            "metadata": {
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "keywords": keywords,
                "date": datetime.now().strftime("%B %Y")
            },
            "sections": sections,
            "references": references,
            "template": "ieee"  # Default template
        }
    
    def _generate_abstract(self) -> str:
        """Generate abstract from analysis results."""
        score = self.analysis.get('innovation_score', 0)
        vector = self.analysis.get('vector', {})
        
        abstract = f"""This report presents an automated innovation assessment using the Themis Vector Space Model (TVSM). 
The analyzed project achieved an Innovation Score of {score}/100, with vector components: 
H (Information Density) = {vector.get('H', 0):.3f}, 
Z (Technical Sophistication) = {vector.get('Z', 0):.3f}, 
C (Legal Compliance) = {vector.get('C', 0):.3f}. """
        
        # Add risk warning if applicable
        if self.analysis.get('patterns_found'):
            abstract += "The analysis identified potential legal compliance issues requiring strategic pivoting. "
        
        abstract += "This automated assessment provides quantitative metrics for innovation evaluation and strategic guidance for optimization."
        
        return abstract
    
    def _generate_figures(self) -> List[str]:
        """
        Generate all visualization figures.
        
        Returns:
            List of figure file paths (relative paths for LaTeX)
        """
        try:
            from .figures import FigureGenerator
            
            fig_gen = FigureGenerator()
            figure_paths = fig_gen.generate_all(self.analysis, prefix="themis")
            
            # Convert to relative paths for LaTeX
            return [str(p).replace('\\', '/') for p in figure_paths]
        except Exception as e:
            print(f"Warning: Could not generate figures: {e}")
            return []
    
    def _generate_sections(self, figure_paths: List[str] = None) -> List[Dict]:
        """Generate paper sections from analysis."""
        sections = []
        
        # 1. Introduction
        sections.append({
            "title": "Introduction",
            "content": self._section_introduction()
        })
        
        # 2. Methodology
        sections.append({
            "title": "Methodology: Themis Vector Space Model",
            "content": self._section_methodology()
        })
        
        # 3. Results
        result_figures = []
        if figure_paths:
            # Add figures to Results section
            for fig_path in figure_paths:
                fig_name = fig_path.split('/')[-1].replace('.png', '').replace('_', ' ').title()
                result_figures.append({
                    "path": fig_path,
                    "caption": f"Themis Analysis: {fig_name}",
                    "width": "0.8\\textwidth"
                })
        
        sections.append({
            "title": "Analysis Results",
            "content": self._section_results(),
            "figures": result_figures
        })
        
        # 4. Strategic Recommendations (if applicable)
        if self.analysis.get('suggestions'):
            sections.append({
                "title": "Strategic Recommendations",
                "content": self._section_recommendations()
            })
        
        # 5. Conclusion
        sections.append({
            "title": "Conclusion",
            "content": self._section_conclusion()
        })
        
        return sections
    
    def _section_introduction(self) -> str:
        """Generate introduction section."""
        return """Innovation assessment is critical for technology transfer, patent filing, and grant applications. 
Traditional methods rely on subjective expert evaluation, which is time-consuming and inconsistent. 
This report presents an automated analysis using the Themis Engine, a vector-based AI system that 
quantifies innovation across three dimensions: Information Density, Technical Sophistication, and Legal Compliance."""
    
    def _section_methodology(self) -> str:
        """Generate methodology section."""
        return r"""The Themis Vector Space Model (TVSM) represents innovation as a vector $\vec{I} \in \mathbb{R}^3$:

$$\vec{I} = \begin{bmatrix} \mathcal{H} \\ \mathcal{Z} \\ \mathcal{C} \end{bmatrix}$$

Where:
- $\mathcal{H}$ (Entropy): Shannon information density, normalized to [0,1]
- $\mathcal{Z}$ (Zipf): Vocabulary sophistication based on Zipf's Law
- $\mathcal{C}$ (Compliance): Inverse of legal risk patterns (LPI 9.279/96)

The Innovation Score is calculated as:

$$S_{themis} = \left( \frac{\|\vec{I}\|}{\sqrt{3}} \right) \times 100$$"""
    
    def _section_results(self) -> str:
        """Generate results section."""
        score = self.analysis.get('innovation_score', 0)
        vector = self.analysis.get('vector', {})
        patterns = self.analysis.get('patterns_found', {})
        
        content = f"""### Overall Score

The analyzed project achieved an **Innovation Score of {score}/100**.

### Vector Components

- **H (Information Density):** {vector.get('H', 0):.4f}
- **Z (Technical Sophistication):** {vector.get('Z', 0):.4f}
- **C (Legal Compliance):** {vector.get('C', 0):.4f}

### Vector Magnitude

$$\|\vec{{I}}\| = \sqrt{{{vector.get('H', 0):.4f}^2 + {vector.get('Z', 0):.4f}^2 + {vector.get('C', 0):.4f}^2}} = {(vector.get('H', 0)**2 + vector.get('Z', 0)**2 + vector.get('C', 0)**2)**0.5:.4f}$$
"""
        
        # Add risk patterns if found
        if patterns:
            content += "\n### Detected Risk Patterns\n\n"
            for category, matches in patterns.items():
                content += f"- **{category.upper()}:** {len(matches)} occurrence(s)\n"
        
        return content
    
    def _section_recommendations(self) -> str:
        """Generate recommendations section."""
        suggestions = self.analysis.get('suggestions', [])
        
        content = "Based on the vector analysis, the following strategic recommendations are provided:\n\n"
        for i, suggestion in enumerate(suggestions, 1):
            content += f"{i}. {suggestion}\n"
        
        return content
    
    def _section_conclusion(self) -> str:
        """Generate conclusion section."""
        score = self.analysis.get('innovation_score', 0)
        
        if score >= 75:
            assessment = "demonstrates strong innovation potential with high scores across all dimensions"
        elif score >= 50:
            assessment = "shows moderate innovation potential with opportunities for strategic improvement"
        else:
            assessment = "requires significant optimization to meet innovation standards"
        
        return f"""The automated Themis analysis indicates that this project {assessment}. 
The vector-based approach provides quantitative, reproducible metrics that can guide strategic decisions 
for patent filing, grant applications, and technology commercialization."""
    
    def _extract_keywords(self) -> List[str]:
        """Extract keywords from analysis."""
        keywords = ["Innovation Assessment", "Vector Space Model", "Themis Engine"]
        
        # Add pattern categories as keywords
        if self.analysis.get('patterns_found'):
            for category in self.analysis['patterns_found'].keys():
                keywords.append(category.title())
        
        return keywords[:5]  # Limit to 5 keywords
    
    def _generate_references(self) -> List[Dict]:
        """Generate bibliography."""
        return [
            {
                "id": "shannon1948",
                "type": "article",
                "title": "A Mathematical Theory of Communication",
                "author": "Shannon, C. E.",
                "venue": "Bell System Technical Journal",
                "year": 1948,
                "pages": "379-423"
            },
            {
                "id": "zipf1949",
                "type": "book",
                "title": "Human Behavior and the Principle of Least Effort",
                "author": "Zipf, G. K.",
                "year": 1949
            },
            {
                "id": "lpi1996",
                "type": "misc",
                "title": "Lei da Propriedade Industrial (LPI 9.279/96)",
                "author": "Brasil",
                "year": 1996
            }
        ]
