# MythosAI-CyberSec

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT"/>
  <img src="https://img.shields.io/badge/AI-Cybersecurity-orange?style=for-the-badge" alt="AI Cybersecurity"/>
  <img src="https://github.com/PremLabs-Security/MythosAI-CyberSec/actions/workflows/ci.yml/badge.svg" alt="CI/CD"/>
</p>

**MythosAI-CyberSec** is an AI-powered cybersecurity assistant designed to help security researchers and analysts identify, analyze, and mitigate digital threats using Large Language Models (LLMs).

## 🛡️ Features

- **AI Threat Analysis**: Leverages LLMs to provide deep insights into vulnerability descriptions.
- **Security Reporting**: Automatically generates risk assessments for organizational assets.
- **Local Threat Knowledge**: Integrates with a local database of known vulnerabilities.
- **Extensible Architecture**: Easily plug in different LLM providers and threat databases.

## 🚀 Installation

```bash
git clone https://github.com/PremLabs-Security/MythosAI-CyberSec.git
cd MythosAI-CyberSec
pip install -r requirements.txt
pip install -e .
```

### Environment Setup

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_api_key_here
```

## 📖 Usage

### CLI Usage

Analyze a potential vulnerability:
```bash
mythosai analyze "Found an input field that doesn't sanitize single quotes in the search bar"
```

Generate a security report for assets:
```bash
mythosai report "web-server-01" "db-server-primary" "api-gateway"
```

### Python API

```python
import asyncio
from mythosai.llm_engine import LLMEngine
from mythosai.analyzer import Analyzer

async def main():
    llm = LLMEngine()
    analyzer = Analyzer(llm)
    result = await analyzer.analyze_vulnerability("Possible SQL injection in login form")
    print(result["analysis"])

asyncio.run(main())
```

## ⚠️ Ethical Use Disclaimer

This tool is intended for ethical hacking, security research, and defensive purposes only. Always obtain proper authorization before testing any systems. The developers are not responsible for any misuse.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by [Pramod Jogdand](https://github.com/Prem2868) | [PremLabs-Security](https://github.com/PremLabs-Security)**
