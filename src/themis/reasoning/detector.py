"""
Themis Engine - Risk Detector Module
Analyzer logic ported from EditalShield Core.
"""

import re
import math
from typing import Dict, List, Tuple
from .patterns import SENSITIVE_PATTERNS, PATTERN_WEIGHTS, PROTECTION_SUGGESTIONS

class RiskDetector:
    def __init__(self):
        pass

    def calculate_entropy(self, text: str) -> Tuple[float, float]:
        """Calcula Shannon entropy do texto."""
        words = text.lower().split()
        if not words:
            return 0.0, 0.0

        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        total = len(words)
        entropy = 0.0
        for freq in word_freq.values():
            p = freq / total
            if p > 0:
                entropy -= p * math.log2(p)

        # Normalize to [0, 1]
        max_entropy = math.log2(len(word_freq)) if len(word_freq) > 1 else 1
        entropy_normalized = entropy / max_entropy if max_entropy > 0 else 0

        return round(entropy, 4), round(entropy_normalized, 4)

    def calculate_zipf_score(self, text: str) -> float:
        """
        Calcula Zipfian Deviation Score.
        Mede quão técnico/raro é o vocabulário.
        """
        words = re.findall(r"\b[a-zA-ZÀ-ÿ]{3,}\b", text.lower())
        if not words:
            return 0.0

        common_words = {
            "que", "para", "com", "não", "uma", "dos", "por", "mais", "das", "como", "mas", "foi",
            "ao", "ele", "tem", "seu", "sua", "ou", "ser", "quando", "muito", "nos", "já", "está",
            "eu", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "depois", "sem",
            "mesmo", "aos", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", "tinha",
            "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", "têm", "numa", "pelos",
            "elas", "qual", "nós", "lhe", "deles", "essas", "esses", "pelas", "este", "dele",
            "tu", "te", "vocês", "vos", "lhes", "meus", "minhas", "teu", "tua", "teus", "tuas",
            "nosso", "nossa", "nossos", "nossas", "dela", "delas", "esta", "estes", "estas",
            "aquele", "aquela", "aqueles", "aquelas", "isto", "aquilo", "estou", "está",
            "estamos", "estão", "estive", "esteve", "estivemos", "estiveram", "estava",
            "estávamos", "estavam", "estivera", "estivéramos", "esteja", "estejamos",
            "estejam", "estivesse", "estivéssemos", "estivessem", "estiver", "estivermos",
            "estiverem", "hei", "há", "havemos", "hão", "houve", "houvemos", "houveram",
            "houvera", "houvéramos", "haja", "hajamos", "hajam", "houvesse", "houvéssemos",
            "houvessem", "houver", "houvermos", "houverem", "houverei", "houverá",
            "houveremos", "houverão", "houveria", "houveríamos", "houveriam", "sou",
            "somos", "são", "era", "éramos", "eram", "fui", "foi", "fomos", "foram",
            "fora", "fôramos", "seja", "sejamos", "sejam", "fosse", "fôssemos", "fossem",
            "for", "formos", "forem", "serei", "será", "seremos", "serão", "seria", "seríamos",
            "seriam", "tenho", "tem", "temos", "têm", "tinha", "tínhamos", "tinham", "tive",
            "teve", "tivemos", "tiveram", "tivera", "tivéramos", "tenha", "tenhamos",
            "tenham", "tivesse", "tivéssemos", "tivessem", "tiver", "tivermos", "tiverem",
            "terei", "terá", "teremos", "terão", "teria", "teríamos", "teriam"
        }

        rare_word_count = 0
        total_length_weight = 0

        for word in words:
            if word not in common_words:
                weight = 1.0
                if len(word) > 7: weight += 0.5
                if len(word) > 10: weight += 0.5
                rare_word_count += 1
                total_length_weight += weight

        score = (total_length_weight / len(words)) if words else 0
        return min(score, 1.0)

    def classify_section(self, text: str) -> str:
        text_lower = text.lower()
        if any(kw in text_lower for kw in ["algoritmo", "modelo", "técnic", "desenvolv", "pipeline", "api"]):
            return "technical"
        elif any(kw in text_lower for kw in ["mercado", "cliente", "tam", "receita", "pricing"]):
            return "market"
        elif any(kw in text_lower for kw in ["equipe", "ceo", "cto", "fundador", "experiência"]):
            return "team"
        elif any(kw in text_lower for kw in ["orçamento", "cronograma", "milestone", "gestão"]):
            return "admin"
        else:
            return "general"

    def detect_patterns(self, text: str) -> Dict[str, List[str]]:
        found = {}
        for category, patterns in SENSITIVE_PATTERNS.items():
            matches = []
            for pattern in patterns:
                found_matches = re.findall(pattern, text, re.IGNORECASE)
                matches.extend(found_matches)
            if matches:
                found[category] = list(set(matches))
        return found

    def analyze(self, text: str) -> dict:
        """Realiza análise completa de risco do texto."""
        entropy, entropy_norm = self.calculate_entropy(text)
        zipf_score = self.calculate_zipf_score(text)
        patterns = self.detect_patterns(text)
        section_type = self.classify_section(text)

        # Calculate score
        pattern_score = 0.0
        suggestions = []
        for category, matches in patterns.items():
            weight = PATTERN_WEIGHTS.get(category, 0.5)
            pattern_score += len(matches) * weight
            if matches:
                 suggestions.append(PROTECTION_SUGGESTIONS.get(category, ""))

        # Vector Space Model (TVSM) Calculation
        # 1. H (Entropy) is already entropy_norm [0, 1]
        H = entropy_norm
        
        # 2. Z (Zipf) is already zipf_score [0, 1]
        Z = zipf_score
        
        # 3. C (Compliance) = 1 / (1 + weighted_risk)
        # pattern_score represents raw risk sum
        C = 1.0 / (1.0 + pattern_score)
        
        # Magnitude ||v||
        magnitude = math.sqrt(H**2 + Z**2 + C**2)
        
        # Max theoretical magnitude = sqrt(1+1+1) = 1.732
        max_magnitude = 1.73205
        
        # Innovation Score (0-100)
        innovation_score = int((magnitude / max_magnitude) * 100)

        # Legacy Risk Score (Inverted Logic mostly)
        # High Innovation usually means Low Risk, but let's keep the specific calculation for UI compatibility
        base_risk = (1.0 - C) * 100 # Simple inversion of compliance
        final_risk = int(base_risk)
        
        return {
            "innovation_score": innovation_score,
            "risk_score": final_risk,
            "vector": {"H": H, "Z": Z, "C": C},
            "entropy": entropy_norm,
            "zipf_score": zipf_score,
            "section_type": section_type,
            "patterns_found": patterns,
            "suggestions": suggestions
        }
