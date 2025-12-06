"""
Themis Vector Optimizer
Provides strategic guidance to maximize Innovation Vector magnitude.
"""

import math
from typing import Dict, List, Tuple

class VectorOptimizer:
    """
    Analyzes the Innovation Vector [H, Z, C] and suggests targeted improvements.
    """
    
    def __init__(self):
        self.max_magnitude = 1.73205  # sqrt(3)
    
    def diagnose_bottleneck(self, vector: Dict[str, float]) -> Dict:
        """
        Identifies which dimension is limiting the Innovation Score.
        Returns the weakest component and its improvement potential.
        """
        H, Z, C = vector['H'], vector['Z'], vector['C']
        
        # Find weakest dimension
        components = {'H': H, 'Z': Z, 'C': C}
        bottleneck = min(components, key=components.get)
        current_value = components[bottleneck]
        
        # Calculate potential gain if bottleneck is fixed to 1.0
        simulated = components.copy()
        simulated[bottleneck] = 1.0
        
        current_mag = math.sqrt(H**2 + Z**2 + C**2)
        potential_mag = math.sqrt(simulated['H']**2 + simulated['Z']**2 + simulated['C']**2)
        
        gain = ((potential_mag / self.max_magnitude) - (current_mag / self.max_magnitude)) * 100
        
        return {
            'bottleneck': bottleneck,
            'current_value': current_value,
            'potential_gain': round(gain, 1),
            'priority': 'CRITICAL' if current_value < 0.3 else 'HIGH' if current_value < 0.6 else 'MEDIUM'
        }
    
    def get_improvement_strategy(self, bottleneck: str, current_value: float) -> List[str]:
        """
        Returns specific, actionable strategies to improve the weakest dimension.
        """
        strategies = {
            'H': [
                "🔬 Add quantitative metrics (e.g., '40% faster', 'reduces latency by 200ms')",
                "🔬 Include technical specifications (model architecture, data structures)",
                "🔬 Detail non-obvious implementation challenges solved",
                "🔬 Describe edge cases handled by your solution"
            ],
            'Z': [
                "📚 Replace generic terms with domain-specific jargon:",
                "   • 'analyze' → 'vectorize via TF-IDF'",
                "   • 'improve' → 'optimize via gradient descent'",
                "   • 'save' → 'persist to distributed cache'",
                "📚 Use acronyms from your field (ML: CNN, NLP, BERT; Security: PKI, HSM)",
                "📚 Reference established algorithms/methods (Dijkstra, Fourier Transform)"
            ],
            'C': [
                "⚖️ CRITICAL: Detected Art. 10 violations (Business Methods / Software-as-such)",
                "⚖️ PIVOT: Focus on the TECHNICAL effect, not the business outcome:",
                "   • Instead of: 'automates sales tracking'",
                "   • Say: 'real-time event stream processing with sub-second latency'",
                "⚖️ Emphasize: data structures, algorithms, hardware optimization",
                "⚖️ Frame as: 'Method for...' or 'System comprising...', not 'software that...'"
            ]
        }
        
        return strategies.get(bottleneck, [])
    
    def simulate_improvement(self, vector: Dict[str, float], target_dim: str, boost: float) -> Dict:
        """
        Simulates the impact of improving a specific dimension.
        
        Args:
            vector: Current [H, Z, C]
            target_dim: Which dimension to boost ('H', 'Z', or 'C')
            boost: Percentage increase (0.0 to 1.0)
        
        Returns:
            Projected new score and percentage improvement
        """
        H, Z, C = vector['H'], vector['Z'], vector['C']
        current_mag = math.sqrt(H**2 + Z**2 + C**2)
        current_score = int((current_mag / self.max_magnitude) * 100)
        
        # Apply boost (capped at 1.0)
        boosted = vector.copy()
        boosted[target_dim] = min(boosted[target_dim] * (1 + boost), 1.0)
        
        new_mag = math.sqrt(boosted['H']**2 + boosted['Z']**2 + boosted['C']**2)
        new_score = int((new_mag / self.max_magnitude) * 100)
        
        return {
            'current_score': current_score,
            'projected_score': new_score,
            'gain': new_score - current_score,
            'boosted_vector': boosted
        }
    
    def generate_optimization_report(self, vector: Dict[str, float], patterns_found: Dict) -> str:
        """
        Generates a comprehensive optimization report with actionable insights.
        """
        diagnosis = self.diagnose_bottleneck(vector)
        strategies = self.get_improvement_strategy(diagnosis['bottleneck'], diagnosis['current_value'])
        
        # Simulate 20% improvement in bottleneck
        simulation = self.simulate_improvement(vector, diagnosis['bottleneck'], 0.20)
        
        report = f"\n{'='*50}\n"
        report += f"📊 VECTOR OPTIMIZATION ANALYSIS\n"
        report += f"{'='*50}\n\n"
        
        report += f"🎯 BOTTLENECK IDENTIFIED: {diagnosis['bottleneck']}\n"
        report += f"   Current Value: {diagnosis['current_value']:.3f}\n"
        report += f"   Priority: {diagnosis['priority']}\n"
        report += f"   Potential Gain: +{diagnosis['potential_gain']}% if optimized\n\n"
        
        report += f"💡 RECOMMENDED ACTIONS:\n"
        for strategy in strategies:
            report += f"   {strategy}\n"
        
        report += f"\n📈 IMPACT SIMULATION (if {diagnosis['bottleneck']} improves 20%):\n"
        report += f"   Current Score: {simulation['current_score']}/100\n"
        report += f"   Projected Score: {simulation['projected_score']}/100\n"
        report += f"   Expected Gain: +{simulation['gain']} points\n"
        
        # If compliance is the issue and patterns were found, be specific
        if diagnosis['bottleneck'] == 'C' and patterns_found:
            report += f"\n⚠️ LEGAL BLOCKERS DETECTED:\n"
            for category, matches in patterns_found.items():
                report += f"   • {category.upper()}: {len(matches)} occurrence(s)\n"
        
        report += f"\n{'='*50}\n"
        
        return report
