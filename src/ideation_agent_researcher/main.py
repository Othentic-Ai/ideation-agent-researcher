"""CLI entry point for the Researcher agent."""

import json
import click
from rich.console import Console

from .agent import run_agent
from .memory import SessionMemory

console = Console()


@click.group()
def cli():
    """Ideation Agent: Researcher - Market Trend Research & Pain Point Analysis."""
    pass


@cli.command()
@click.option("--session-id", required=True, help="Session ID for Mem0 context")
@click.option("--problem", default=None, help="Problem statement (optional, reads from Mem0 if not provided)")
@click.option("--output-json", is_flag=True, help="Output results as JSON")
def run(session_id: str, problem: str | None, output_json: bool):
    """Run the researcher agent for a given session."""
    memory = SessionMemory(session_id)

    # Get problem from Mem0 if not provided
    if not problem:
        session = memory.get_session()
        if not session:
            console.print(f"[red]Error: No session found for {session_id}[/red]")
            raise SystemExit(1)
        problem = session.get("problem")
        if not problem:
            console.print(f"[red]Error: No problem found in session {session_id}[/red]")
            raise SystemExit(1)

    console.print(f"[blue]Running researcher agent for session: {session_id}[/blue]")
    console.print(f"[dim]Problem: {problem[:100]}...[/dim]" if len(problem) > 100 else f"[dim]Problem: {problem}[/dim]")

    # Run the agent
    result = run_agent(session_id, problem)

    # Save results to Mem0
    memory.update_phase("researcher", "complete", result)

    if output_json:
        print(json.dumps(result, indent=2))
    else:
        console.print("[green]Researcher agent completed successfully[/green]")
        console.print(f"[dim]Results saved to Mem0 session: {session_id}[/dim]")


@cli.command()
@click.option("--session-id", required=True, help="Session ID to check")
def status(session_id: str):
    """Check the status of a session."""
    memory = SessionMemory(session_id)
    session = memory.get_session()

    if not session:
        console.print(f"[yellow]No session found for {session_id}[/yellow]")
    else:
        console.print(f"[green]Session found: {session_id}[/green]")
        phases = session.get("phases", {})
        researcher_status = phases.get("researcher", {}).get("status", "not started")
        console.print(f"Researcher status: {researcher_status}")


if __name__ == "__main__":
    cli()
