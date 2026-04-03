import chromadb
from pathlib import Path
from typing import List, Dict
import os

class LegalVectorStore:
    """
    Gerencia a base de conhecimento vetorial para RAG (Retrieval Augmented Generation).
    Indexa as leis em docs/legal_refs e permite busca por similaridade.
    """
    def __init__(self, persist_directory: str = None):
        if not persist_directory:
            # Default persist: juridical-innovation-agent/storage/vector_db
            base_dir = Path(__file__).parent.parent.parent.parent
            persist_directory = str(base_dir / "storage" / "vector_db")
        
        os.makedirs(persist_directory, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(name="themis_laws")

    def index_laws(self, legal_refs_path: Path):
        """Lê os arquivos .md e indexa no ChromaDB."""
        if not legal_refs_path.exists():
            return
        
        documents = []
        metadatas = []
        ids = []

        for f in legal_refs_path.glob("*.md"):
            content = f.read_text(encoding="utf-8")
            # Divide por seções (Markdown headers)
            sections = content.split("##")
            law_name = f.stem
            
            for i, section in enumerate(sections):
                if not section.strip(): continue
                
                doc_text = f"LAW: {law_name}\nSECTION: {section.strip()}"
                documents.append(doc_text)
                metadatas.append({"law": law_name, "section": i})
                ids.append(f"{law_name}_{i}")

        if documents:
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"Indexed {len(documents)} legal sections into Vector Store.")

    def query(self, query_text: str, n_results: int = 3) -> List[str]:
        """Busca os trechos de lei mais relevantes para uma consulta."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results['documents'][0] if results['documents'] else []

if __name__ == "__main__":
    # Teste de Indexação
    base_path = Path(__file__).parent.parent.parent.parent
    lb = LegalVectorStore()
    lb.index_laws(base_path / "docs" / "legal_refs")
    
    # Teste de Busca
    res = lb.query("Como patentear software no Brasil?")
    print("\nResultados da Busca Vetorial:")
    for r in res:
        print(f"--- \n{r[:200]}...")
