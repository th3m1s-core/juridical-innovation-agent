"""
Themis Data Connectors
Provides access to historical data (EditalShield DB) and public APIs (INPI).
"""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class Precedent:
    """Memorial precedent from EditalShield database."""
    memorial_id: int
    sector: str
    technology_type: str
    result: str
    avg_entropy: float
    avg_patterns: float
    similarity_score: float  # Similarity to query


class EditalShieldConnector:
    """
    Connects to EditalShield PostgreSQL database to retrieve precedents and benchmarks.
    """
    
    def __init__(self, connection_string: Optional[str] = None):
        """
        Initialize connector.
        
        Args:
            connection_string: PostgreSQL connection string, or read from ENV
        """
        self.conn_string = connection_string or os.getenv(
            'EDITALSHIELD_DB',
            'postgresql://user:password@localhost:5432/editalshield'
        )
        self.conn = None
    
    def connect(self):
        """Lazy connection to database."""
        if self.conn is None:
            try:
                import psycopg2
                self.conn = psycopg2.connect(self.conn_string)
            except ImportError:
                raise ImportError("psycopg2 not installed. Run: pip install psycopg2-binary")
            except Exception as e:
                print(f"⚠️ Could not connect to EditalShield DB: {e}")
                self.conn = None
    
    def search_precedents(
        self, 
        sector: Optional[str] = None,
        technology_type: Optional[str] = None,
        limit: int = 5
    ) -> List[Precedent]:
        """
        Search for similar approved projects in EditalShield database.
        
        Args:
            sector: Filter by sector (e.g., 'fintech', 'healthtech')
            technology_type: Filter by tech type ('software', 'hardware', 'hybrid')
            limit: Max results
        
        Returns:
            List of Precedent objects
        """
        self.connect()
        if not self.conn:
            return []
        
        try:
            cursor = self.conn.cursor()
            
            query = """
                SELECT 
                    m.memorial_id,
                    m.sector,
                    m.technology_type,
                    m.result,
                    v.avg_entropy,
                    v.avg_patterns
                FROM memorials m
                JOIN v_memorial_stats v ON m.memorial_id = v.memorial_id
                WHERE m.result = 'approved'
            """
            
            filters = []
            params = []
            
            if sector:
                filters.append("m.sector = %s")
                params.append(sector)
            
            if technology_type:
                filters.append("m.technology_type = %s")
                params.append(technology_type)
            
            if filters:
                query += " AND " + " AND ".join(filters)
            
            query += f" ORDER BY m.created_at DESC LIMIT {limit}"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            precedents = []
            for row in rows:
                precedents.append(Precedent(
                    memorial_id=row[0],
                    sector=row[1],
                    technology_type=row[2],
                    result=row[3],
                    avg_entropy=row[4] or 0.0,
                    avg_patterns=row[5] or 0.0,
                    similarity_score=0.85  # TODO: Implement semantic similarity
                ))
            
            cursor.close()
            return precedents
        
        except Exception as e:
            print(f"Error searching precedents: {e}")
            return []
    
    def get_percentile(self, innovation_score: int, sector: Optional[str] = None) -> Dict:
        """
        Calculate percentile of innovation score compared to approved projects.
        
        Args:
            innovation_score: The score to benchmark (0-100)
            sector: Optional sector filter
        
        Returns:
            Percentile and comparison stats
        """
        self.connect()
        if not self.conn:
            return {"percentile": 50, "note": "Database unavailable"}
        
        try:
            cursor = self.conn.cursor()
            
            # Simplified: Using entropy as proxy for innovation (would need to recalculate scores)
            # In production, you'd store innovation_score in memorials table
            query = """
                SELECT AVG(v.avg_entropy) as mean_entropy, STDDEV(v.avg_entropy) as std_entropy
                FROM memorials m
                JOIN v_memorial_stats v ON m.memorial_id = v.memorial_id
                WHERE m.result = 'approved'
            """
            
            if sector:
                query += " AND m.sector = %s"
                cursor.execute(query, [sector])
            else:
                cursor.execute(query)
            
            row = cursor.fetchone()
            mean = row[0] or 0.5
            std = row[1] or 0.2
            
            # Normalize innovation score to entropy scale (rough approximation)
            normalized_score = (innovation_score /100) * 1.0
            
            # Calculate Z-score and percentile
            z_score = (normalized_score - mean) / std if std > 0 else 0
            
            # Approximate percentile from Z-score (simplified)
            from math import erf
            percentile = int((1 + erf(z_score / 2**0.5)) / 2 * 100)
            
            cursor.close()
            return {
                "percentile": max(1, min(99, percentile)),
                "interpretation": self._interpret_percentile(percentile)
            }
        
        except Exception as e:
            print(f"Error calculating percentile: {e}")
            return {"percentile": 50, "note": f"Error: {e}"}
    
    def _interpret_percentile(self, percentile: int) -> str:
        if percentile >= 90:
            return "🏆 Top 10% - Exceptional innovation profile"
        elif percentile >= 75:
            return "✨ Top 25% - Strong competitive advantage"
        elif percentile >= 50:
            return "📊 Above average - Solid foundation"
        elif percentile >= 25:
            return "⚠️ Below average - Needs improvement"
        else:
            return "🚨 Bottom 25% - Critical intervention required"
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None


class INPIConnector:
    """
    Connector to INPI (Instituto Nacional da Propriedade Industrial) APIs.
    For now, this is a placeholder for future patent search integration.
    """
    
    def __init__(self):
        self.base_url = "https://busca.inpi.gov.br/pePI/servlet/PatenteServletController"
    
    def search_patents(self, keywords: str, limit: int = 3) -> List[Dict]:
        """
        Search for existing patents (Prior Art check).
        
        Note: INPI doesn't have a public REST API yet. This would require:
        - Web scraping (Selenium/BeautifulSoup)
        - Or using third-party APIs like PatentsView (USPTO)
        
        For now, returns mock data to demonstrate the concept.
        """
        # TODO: Implement actual INPI scraping or use alternative APIs
        return [
            {
                "patent_id": "BR1020210001234",
                "title": "[Mock] Sistema de processamento distribuído...",
                "applicant": "Empresa Tech Ltda",
                "relevance": 0.72
            }
        ]
