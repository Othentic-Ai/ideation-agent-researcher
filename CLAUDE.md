# Ideation Agent: Researcher

This is a specialized Claude Code agent for market trend research and customer pain point analysis.

## What This Agent Does

When invoked, this agent:
1. Reads the problem/topic from Mem0 using the provided session-id
2. Researches market trends using WebSearch
3. Analyzes customer pain points
4. Writes results back to Mem0 for the orchestrator to retrieve

## How to Run

```bash
# Install dependencies
pip install -e .

# Run the agent
ideation-agent-researcher run --session-id <session-id>
```

## Environment Variables

- `ANTHROPIC_API_KEY`: Required for Claude API access
- `MEM0_API_KEY`: Required for Mem0 cloud storage

## Invocation via GitHub Actions

This agent is designed to be triggered via `repository_dispatch` webhook:

```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Othentic-Ai/ideation-agent-researcher/dispatches \
  -d '{"event_type": "run", "client_payload": {"session_id": "abc123"}}'
```

## Agent Behavior

Read the system prompt at `src/ideation_agent_researcher/prompts/system.md` for the agent's detailed behavior.
