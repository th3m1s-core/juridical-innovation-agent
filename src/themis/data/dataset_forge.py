import json
from pathlib import Path
from themis.reasoning.detector import RiskDetector

class DatasetForge:
    """
    Transforma as análises da Themis em datasets para fine-tuning (SFT).
    Usa o modelo Themis como 'Professor' para treinar LLMs locais.
    """
    def __init__(self, output_file: str = "themis_sft_dataset.jsonl"):
        self.detector = RiskDetector()
        self.output_file = output_file

    def generate_example(self, text: str) -> dict:
        """Cria um par (Input, Output) para ajuste fino."""
        analysis = self.detector.analyze(text)
        
        # Formato ChatML (Nativo Qwen-2.5)
        example = {
            "messages": [
                {
                    "role": "system", 
                    "content": "Você é o Agente Jurídico Soberano da TH3M1S, um auditor de inovação técnica."
                },
                {
                    "role": "user", 
                    "content": f"Analise o seguinte projeto técnica quanto à inovação e conformidade: {text}"
                },
                {
                    "role": "assistant", 
                    "content": f"""A análise do Themis Engine retornou um Innovation Score de {analysis['innovation_score']}/100. 
O vetor de inovação é composto por H={analysis['vector']['H']:.3f} (Densidade), Z={analysis['vector']['Z']:.3f} (Profundidade) e C={analysis['vector']['C']:.3f} (Conformidade).
Os principais padrões detectados foram: {list(analysis['patterns_found'].keys())}. 
Sugestão: {analysis['suggestions'][0] if analysis['suggestions'] else 'Continuar pesquisa.'}"""
                }
            ]
        }
        return example

    def forge(self, source_texts: list):
        """Processa uma lista de textos e gera o arquivo JSONL."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for text in source_texts:
                example = self.generate_example(text)
                f.write(json.dump_string(example) if hasattr(json, 'dump_string') else json.dumps(example, ensure_ascii=False) + "\n")
        print(f"Dataset gerado com sucesso em {self.output_file}")

if __name__ == "__main__":
    forge = DatasetForge()
    # Exemplos para treinamento
    samples = [
        "Algoritmo de criptografia pós-quântica baseado em redes de Lattices.",
        "Sistema de bio-rastreabilidade de ativos em blockchain para agronegócio.",
        "Modelo de IA generativa para design de fármacos oncológicos."
    ]
    forge.forge(samples)
