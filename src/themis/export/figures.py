"""
Figure Generator for Themis Analysis Papers
Creates publication-quality visualizations.
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
import seaborn as sns

# Set publication-quality style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 13


class FigureGenerator:
    """
    Generates publication-ready figures for Themis analysis papers.
    """
    
    def __init__(self, output_dir: str = "output/figures"):
        """
        Initialize figure generator.
        
        Args:
            output_dir: Directory to save figures
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Color scheme (professional)
        self.colors = {
            'primary': '#2E86AB',    # Blue
            'secondary': '#A23B72',  # Purple
            'accent': '#F18F01',     # Orange
            'success': '#06A77D',    # Green
            'warning': '#D62246',    # Red
            'neutral': '#6C757D'     # Gray
        }
    
    def generate_all(self, analysis: Dict, prefix: str = "fig") -> List[str]:
        """
        Generate all figures for an analysis.
        
        Args:
            analysis: Themis analysis result
            prefix: Filename prefix
        
        Returns:
            List of generated figure paths
        """
        figures = []
        
        # 1. Innovation Vector 3D
        fig_path = self.plot_innovation_vector_3d(
            analysis['vector'],
            filename=f"{prefix}_vector_3d.png"
        )
        figures.append(fig_path)
        
        # 2. Component Radar Chart
        fig_path = self.plot_component_radar(
            analysis['vector'],
            filename=f"{prefix}_radar.png"
        )
        figures.append(fig_path)
        
        # 3. Risk Heatmap (if patterns found)
        if analysis.get('patterns_found'):
            fig_path = self.plot_risk_heatmap(
                analysis['patterns_found'],
                filename=f"{prefix}_risk_heatmap.png"
            )
            figures.append(fig_path)
        
        # 4. Score Gauge
        fig_path = self.plot_score_gauge(
            analysis['innovation_score'],
            filename=f"{prefix}_score_gauge.png"
        )
        figures.append(fig_path)
        
        return figures
    
    def plot_innovation_vector_3d(
        self,
        vector: Dict[str, float],
        filename: str = "vector_3d.png"
    ) -> str:
        """
        Create 3D visualization of innovation vector.
        
        Args:
            vector: Dict with H, Z, C components
            filename: Output filename
        
        Returns:
            Path to saved figure
        """
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        
        # Origin
        origin = [0, 0, 0]
        
        # Vector components
        H, Z, C = vector['H'], vector['Z'], vector['C']
        
        # Plot vector
        ax.quiver(0, 0, 0, H, Z, C, 
                 color=self.colors['primary'],
                 arrow_length_ratio=0.1,
                 linewidth=3,
                 label='Innovation Vector')
        
        # Plot component projections
        ax.plot([0, H], [0, 0], [0, 0], 'r--', alpha=0.5, linewidth=1.5, label='H (Entropy)')
        ax.plot([0, 0], [0, Z], [0, 0], 'g--', alpha=0.5, linewidth=1.5, label='Z (Zipf)')
        ax.plot([0, 0], [0, 0], [0, C], 'b--', alpha=0.5, linewidth=1.5, label='C (Compliance)')
        
        # Plot point
        ax.scatter([H], [Z], [C], color=self.colors['accent'], s=100, marker='o')
        
        # Axes
        ax.set_xlabel('H (Information Density)', fontweight='bold')
        ax.set_ylabel('Z (Technical Sophistication)', fontweight='bold')
        ax.set_zlabel('C (Legal Compliance)', fontweight='bold')
        ax.set_title('Innovation Vector in 3D Space', fontweight='bold', pad=20)
        
        # Set limits
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        ax.set_zlim([0, 1])
        
        # Grid
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left')
        
        # Save
        output_path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_component_radar(
        self,
        vector: Dict[str, float],
        filename: str = "radar.png"
    ) -> str:
        """
        Create radar chart of vector components.
        
        Args:
            vector: Dict with H, Z, C components
            filename: Output filename
        
        Returns:
            Path to saved figure
        """
        categories = ['Information\nDensity (H)', 'Technical\nSophistication (Z)', 'Legal\nCompliance (C)']
        values = [vector['H'], vector['Z'], vector['C']]
        
        # Number of variables
        N = len(categories)
        
        # Compute angle for each axis
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        values += values[:1]  # Complete the circle
        angles += angles[:1]
        
        # Plot
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        
        # Draw the plot
        ax.plot(angles, values, 'o-', linewidth=2, color=self.colors['primary'], label='Current Score')
        ax.fill(angles, values, alpha=0.25, color=self.colors['primary'])
        
        # Draw ideal (all 1.0)
        ideal = [1.0] * (N + 1)
        ax.plot(angles, ideal, '--', linewidth=1.5, color=self.colors['success'], alpha=0.7, label='Ideal (1.0)')
        
        # Fix axis to go from 0 to 1
        ax.set_ylim(0, 1)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=10)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], size=9)
        ax.grid(True, alpha=0.3)
        
        # Title and legend
        ax.set_title('Innovation Vector Components', size=13, fontweight='bold', pad=20)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        
        # Save
        output_path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_risk_heatmap(
        self,
        patterns_found: Dict[str, List[str]],
        filename: str = "risk_heatmap.png"
    ) -> str:
        """
        Create heatmap of detected risk patterns.
        
        Args:
            patterns_found: Dict of pattern categories and matches
            filename: Output filename
        
        Returns:
            Path to saved figure
        """
        # Prepare data
        categories = list(patterns_found.keys())
        counts = [len(matches) for matches in patterns_found.values()]
        
        if not categories:
            return None
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, max(4, len(categories) * 0.5)))
        
        # Create heatmap data (single column)
        data = np.array(counts).reshape(-1, 1)
        
        # Plot
        sns.heatmap(data, 
                   annot=True, 
                   fmt='d',
                   cmap='YlOrRd',
                   cbar_kws={'label': 'Occurrences'},
                   yticklabels=[cat.replace('_', ' ').title() for cat in categories],
                   xticklabels=['Risk Level'],
                   ax=ax)
        
        ax.set_title('Detected Risk Patterns by Category', fontweight='bold', pad=15)
        ax.set_ylabel('Pattern Category', fontweight='bold')
        
        # Save
        output_path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_score_gauge(
        self,
        score: int,
        filename: str = "score_gauge.png"
    ) -> str:
        """
        Create gauge chart for innovation score.
        
        Args:
            score: Innovation score (0-100)
            filename: Output filename
        
        Returns:
            Path to saved figure
        """
        fig, ax = plt.subplots(figsize=(8, 5), subplot_kw={'projection': 'polar'})
        
        # Gauge parameters
        theta = np.linspace(0, np.pi, 100)
        
        # Background arc (0-100)
        ax.plot(theta, [1] * len(theta), color='lightgray', linewidth=20, alpha=0.3)
        
        # Score arc
        score_theta = np.linspace(0, np.pi * (score / 100), 100)
        
        # Color based on score
        if score >= 75:
            color = self.colors['success']
        elif score >= 50:
            color = self.colors['accent']
        else:
            color = self.colors['warning']
        
        ax.plot(score_theta, [1] * len(score_theta), color=color, linewidth=20)
        
        # Remove radial ticks
        ax.set_yticks([])
        ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
        ax.set_xticklabels(['0', '25', '50', '75', '100'])
        
        # Score text in center
        ax.text(np.pi/2, 0.5, f'{score}', 
               ha='center', va='center',
               fontsize=48, fontweight='bold', color=color)
        ax.text(np.pi/2, 0.2, 'Innovation Score', 
               ha='center', va='center',
               fontsize=14, color='gray')
        
        ax.set_ylim(0, 1.2)
        ax.grid(False)
        ax.spines['polar'].set_visible(False)
        
        # Save
        output_path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        
        return str(output_path)
    
    def plot_score_comparison(
        self,
        before_score: int,
        after_score: int,
        filename: str = "score_comparison.png"
    ) -> str:
        """
        Create before/after score comparison chart.
        
        Args:
            before_score: Score before optimization
            after_score: Score after optimization
            filename: Output filename
        
        Returns:
            Path to saved figure
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        
        categories = ['Before\nOptimization', 'After\nOptimization']
        scores = [before_score, after_score]
        colors_list = [self.colors['warning'], self.colors['success']]
        
        bars = ax.bar(categories, scores, color=colors_list, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar, score in zip(bars, scores):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{score}',
                   ha='center', va='bottom', fontsize=16, fontweight='bold')
        
        # Add improvement arrow
        improvement = after_score - before_score
        if improvement > 0:
            ax.annotate('', xy=(1, after_score), xytext=(0, before_score),
                       arrowprops=dict(arrowstyle='->', lw=2, color=self.colors['success']))
            ax.text(0.5, (before_score + after_score) / 2, f'+{improvement}',
                   ha='center', fontsize=12, color=self.colors['success'], fontweight='bold')
        
        ax.set_ylabel('Innovation Score', fontweight='bold')
        ax.set_ylim(0, 105)
        ax.set_title('Score Improvement After Optimization', fontweight='bold', pad=15)
        ax.grid(axis='y', alpha=0.3)
        
        # Save
        output_path = self.output_dir / filename
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
