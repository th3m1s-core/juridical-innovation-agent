import os
from typing import List, Dict, Any
from themis.reasoning.detector import RiskDetector
from themis.knowledge.vector_store import LegalVectorStore

class SovereignLegalAgent:
    """
    Agente Jurídico Soberano capaz de raciocínio híbrido (Simbólico + LLM).
    Opera localmente para garantir privacidade absoluta dos dados.
    """
    def __init__(self, ollama_url: str = "http://localhost:11434/v1", model: str = "qwen2.5-coder:7b"):
        self.detector = RiskDetector()
        self.vector_store = LegalVectorStore()
        self.ollama_url = ollama_url
        self.model = model
        
        # Opcional: inicializar cliente OpenAI-compatible se disponível
        try:
            from openai import OpenAI
            self.client = OpenAI(base_url=ollama_url, api_key="ollama")
        except ImportError:
            self.client = None

    def analyze_and_chat(self, text: str) -> Dict[str, Any]:
        """
        Gera análise simbólica, recupera base legal e consulta o LLM Local
        para um parecer final humanizado.
        """
        # 1. Análise Simbólica (TVSM)
        analysis = self.detector.analyze(text)
        
        # 2. RAG: Busca Base Legal Relevante
        query_text = f"Análise de inovação: {text[:500]}"
        legal_context = self.vector_store.query(query_text, n_results=3)
        legal_refs = "\n--- \n".join(legal_context)
        
        # 3. Prompt Local (Linguistic Layer)
        system_prompt = f"""
        Você é um Auditor Jurídico Soberano da Organização TH3M1S.
        Seu objetivo é dar um parecer sobre a inovação técnica baseando-se no Hexágono Legislativo.
        
        DADOS TÉCNICOS (Themis Engine):
        - Score de Inovação: {analysis['innovation_score']}/100
        - Vetores: H={analysis['vector']['H']:.3f}, Z={analysis['vector']['Z']:.3f}, C={analysis['vector']['C']:.3f}
        
        BASE LEGAL RECUPERADA (RAG):
        {legal_refs}
        
        REGRAS:
        - Seja técnico, mas propositivo.
        - Se o Score C for baixo, aponte as violações específicas.
        - Fale em Português do Brasil de forma executiva.
        """
        
        if self.client:
            # Consulta o LLM Local (Qwen ou Llama)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Analise o seguinte projeto:\n{text}"}
                ]
            )
            report = response.choices[0].message.content
        else:
            report = "[LLM OFFLINE] Ligue o Ollama para ver o parecer humanizado."

        return {
            "analysis": analysis,
            "legal_context": legal_context,
            "sovereign_report": report
        }

if __name__ == "__main__":
    agent = SovereignLegalAgent()
    # Teste
    test_text = "Algoritmo de IA para reconhecimento facial criptografado para segurança pública."
    result = agent.analyze_and_chat(test_text)
    print(f"\n--- PARECER SOBERANO ---\n{result['sovereign_report']}")
