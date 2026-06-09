import asyncio
import click
import logging
from rich.console import Console
from rich.markdown import Markdown
from .llm_engine import LLMEngine
from .analyzer import Analyzer

console = Console()

@click.group()
def cli():
    """MythosAI-CyberSec: AI-powered cybersecurity assistant."""
    pass

@cli.command()
@click.argument('description')
@click.option('--model', default='gpt-4', help='LLM model to use')
def analyze(description, model):
    """Analyze a vulnerability description using AI."""
    async def run():
        try:
            llm = LLMEngine(model=model)
            analyzer = Analyzer(llm)
            
            console.print(f"[*] Analyzing: [bold cyan]{description}[/bold cyan]...")
            result = await analyzer.analyze_vulnerability(description)
            
            console.print("\n[bold green]Analysis Result:[/bold green]")
            console.print(Markdown(result["analysis"]))
            
            if result["related_threats"]:
                console.print("\n[bold yellow]Related Known Threats:[/bold yellow]")
                for threat in result["related_threats"]:
                    console.print(f"- {threat['name']}: {threat['description']}")
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

    asyncio.run(run())

@cli.command()
@click.argument('assets', nargs=-1)
def report(assets):
    """Generate a security report for the given assets."""
    if not assets:
        console.print("[bold red]Error: No assets provided.[/bold red]")
        return

    async def run():
        try:
            llm = LLMEngine()
            analyzer = Analyzer(llm)
            
            console.print(f"[*] Generating report for {len(assets)} assets...")
            report_text = await analyzer.generate_security_report(list(assets))
            
            console.print("\n[bold green]Security Report:[/bold green]")
            console.print(Markdown(report_text))
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

    asyncio.run(run())

def main():
    cli()

if __name__ == "__main__":
    main()
