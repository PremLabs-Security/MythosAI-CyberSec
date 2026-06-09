from typing import List, Dict, Any

class ThreatDB:
    """A local database of common cybersecurity threats and vulnerabilities."""

    def __init__(self):
        # Sample data - in a real app, this might be a JSON file or a real database
        self.threats = [
            {
                "id": "T001",
                "name": "SQL Injection",
                "description": "Injection of malicious SQL queries into input fields.",
                "mitigation": "Use prepared statements and parameterized queries."
            },
            {
                "id": "T002",
                "name": "Cross-Site Scripting (XSS)",
                "description": "Injection of malicious scripts into web pages viewed by other users.",
                "mitigation": "Sanitize user input and use Content Security Policy (CSP)."
            },
            {
                "id": "T003",
                "name": "Broken Authentication",
                "description": "Vulnerabilities in login mechanisms that allow attackers to gain unauthorized access.",
                "mitigation": "Implement multi-factor authentication and secure session management."
            }
        ]

    def get_all_threats(self) -> List[Dict[str, Any]]:
        return self.threats

    def search_threats(self, query: str) -> List[Dict[str, Any]]:
        return [t for t in self.threats if query.lower() in t["name"].lower() or query.lower() in t["description"].lower()]
