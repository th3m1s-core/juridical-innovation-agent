from pathlib import Path
from typing import Dict

class LegalKnowledgeBase:
    """
    Carrega a base de conhecimento jurídico (LPI, TRL) para contexto do Agente.
    """
    def __init__(self, base_path: Path = None):
        if base_path:
            self.docs_path = base_path
        else:
            # Caminho relativo padrão: juridical-innovation-agent/docs/legal_refs
            self.docs_path = Path(__file__).parent.parent.parent.parent / "docs" / "legal_refs"
        
        self.documents: Dict[str, str] = {}
        self._load()

    def _load(self):
        if not self.docs_path.exists():
            return
        
        for f in self.docs_path.glob("*.md"):
            self.documents[f.stem] = f.read_text(encoding="utf-8")

    def get_context(self) -> str:
        """Retorna string formatada para System Prompt."""
        context = "# 📚 LEGAL KNOWLEDGE BASE\n\n"
        for name, content in self.documents.items():
            context += f"## {name}\n{content}\n\n"
        return context
