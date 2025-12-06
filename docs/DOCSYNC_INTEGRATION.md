# 🔄 DocSync Integration

This project uses **[DocSync](https://github.com/SH1W4/docsync)** to maintain high-quality, consistent documentation aligned with Legal AI standards.

## 🛠️ Configuration

The configuration is located in `docsync.yaml`. It defines custom rules for:
- **Legal Consistency:** Ensuring terms match LPI 9.279/96.
- **TRL Alignment:** Verifying technology readiness levels.

## 🚀 Usage

To update documentation using AI:

```powershell
# 1. Activate Environment
./.venv/Scripts/Activate.ps1

# 2. Run DocSync Analysis
docsync check

# 3. Improve Specific Document
docsync improve docs/legal_refs/LPI_HIGHLIGHTS.md
```

## 🤖 MCP Integration

Since DocSync is also an MCP Server, you can chain it with Themis:
1. **Themis** analyzes a project and identifies risks.
2. **DocSync** reads the report and suggests updates to the project's internal documentation to clear those risks.
