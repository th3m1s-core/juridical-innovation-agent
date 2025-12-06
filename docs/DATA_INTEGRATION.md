# 🗄️ Data Integration Guide

Themis can connect to external data sources for enhanced intelligence:

## 1. EditalShield Database (Historical Data)

Connect to the EditalShield PostgreSQL database to access:
- **Approved Projects:** Learn from successful memorials
- **Benchmarking:** Compare your Innovation Score with historical data
- **Precedent Search:** Find similar projects in your sector

### Setup

1. **Install database support:**
   ```bash
   pip install -e ".[database]"
   ```

2. **Set environment variable:**
   ```bash
   export EDITALSHIELD_DB="postgresql://user:password@localhost:5432/editalshield"
   ```

3. **Verify connection:**
   ```python
   from themis.data import EditalShieldConnector
   db =EditalShieldConnector()
   db.connect()
   ```

### MCP Tools
Once connected, these tools become available:

- **`search_precedents(sector, technology_type)`**: Find similar approved projects
- **`get_benchmark(innovation_score, sector)`**: Get percentile ranking
  
**Example Usage (via Claude/Cline):**
```
User: "Search for approved fintech projects"
Themis: [Calls search_precedents(sector="fintech")]
>>> Found 5 approved projects with avg entropy 0.72...
```

---

## 2. INPI API (Prior Art Search)

Search existing patents to verify novelty.

### Status
🚧 **EXPERIMENTAL** - Currently uses mock data. 

INPI doesn't have a public REST API. Full implementation would require:
- Web scraping (Selenium/BeautifulSoup)
- Or third-party APIs (PatentsView for USPTO)

### MCP Tool
- **`check_prior_art(keywords)`**: Search for similar patents

---

## 3. Custom Data Sources

To add your own database:

1. Create a connector in `src/themis/data/connectors.py`
2. Implement search/query methods
3. Expose via MCP tool in `src/themis/server.py`

### Example Template:
```python
class CustomConnector:
    def search(self, query: str) -> List[Dict]:
        # Your logic here
        return []
```
