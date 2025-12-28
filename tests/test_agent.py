"""Tests for the Researcher agent."""

import pytest
from pathlib import Path


def test_system_prompt_exists():
    """Test that the system prompt file exists."""
    prompt_path = Path(__file__).parent.parent / "src" / "ideation_agent_researcher" / "prompts" / "system.md"
    assert prompt_path.exists(), "System prompt file should exist"


def test_system_prompt_content():
    """Test that the system prompt has required sections."""
    prompt_path = Path(__file__).parent.parent / "src" / "ideation_agent_researcher" / "prompts" / "system.md"
    content = prompt_path.read_text()

    assert "# Researcher Agent" in content
    assert "Market Trends" in content
    assert "Pain Point" in content
    assert "Output Format" in content


def test_cli_import():
    """Test that CLI can be imported."""
    from ideation_agent_researcher.main import cli
    assert cli is not None


def test_agent_import():
    """Test that agent module can be imported."""
    from ideation_agent_researcher.agent import run_agent, get_system_prompt
    assert run_agent is not None
    assert get_system_prompt is not None


def test_memory_import():
    """Test that memory module can be imported."""
    from ideation_agent_researcher.memory import SessionMemory
    assert SessionMemory is not None


def test_get_system_prompt():
    """Test that get_system_prompt returns content."""
    from ideation_agent_researcher.agent import get_system_prompt
    prompt = get_system_prompt()
    assert len(prompt) > 0
    assert "Researcher" in prompt
