"""Core agent execution logic for the Researcher agent."""

import os
from pathlib import Path


def get_system_prompt() -> str:
    """Load the system prompt from the prompts directory."""
    prompt_path = Path(__file__).parent / "prompts" / "system.md"
    return prompt_path.read_text()


def run_agent(session_id: str, problem: str) -> dict:
    """Run the researcher agent.

    This function is called by the CLI and executes the research task.
    When running under Claude Code, the actual research is performed by Claude
    following the system prompt instructions.

    Args:
        session_id: The session ID for context
        problem: The problem statement to research

    Returns:
        dict with research results
    """
    # The actual execution happens via Claude Code
    # This Python code provides the structure and Mem0 integration
    # Claude reads the CLAUDE.md and system prompt to understand what to do

    system_prompt = get_system_prompt()

    # When run via Claude Code, the agent will:
    # 1. Use WebSearch to research market trends
    # 2. Analyze customer pain points
    # 3. Return structured results

    # For now, return a placeholder that indicates Claude should execute
    return {
        "phase": "researcher",
        "session_id": session_id,
        "problem": problem,
        "status": "pending_claude_execution",
        "system_prompt_loaded": bool(system_prompt),
        "instructions": "This agent should be run via Claude Code CLI"
    }
