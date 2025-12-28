# Ideation Agent: Researcher

Market Trend Researcher & Customer Pain Point Analyst for the Ideation Pipeline.

## Overview

This agent is part of the Ideation multi-agent pipeline. It performs:
1. **Market Trend Research**: Identifies emerging trends, technological shifts, and industry patterns
2. **Pain Point Analysis**: Discovers and validates customer pain points and unmet needs

## Installation

```bash
pip install -e .
```

## Usage

### CLI

```bash
ideation-agent-researcher run --session-id <session-id>
```

### GitHub Actions (Webhook Trigger)

This agent is designed to be triggered via `repository_dispatch`:

```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Othentic-Ai/ideation-agent-researcher/dispatches \
  -d '{"event_type": "run", "client_payload": {"session_id": "abc123"}}'
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Claude API key |
| `MEM0_API_KEY` | Yes | Mem0 cloud storage key |

## Output

The agent writes its results to Mem0 under the session-id with the following structure:

```json
{
  "phase": "researcher",
  "status": "complete",
  "output": {
    "market_trends": [...],
    "pain_points": [...],
    "key_insights": [...]
  }
}
```

## Part of Ideation Pipeline

This agent is orchestrated by the [ideation-orchestrator](https://github.com/Othentic-Ai/ideation-orchestrator).

```
ideation-orchestrator
├── ideation-agent-researcher (this repo)
├── ideation-agent-market-analyst
├── ideation-agent-customer-discovery
├── ideation-agent-scoring-evaluator
├── ideation-agent-competitor-analyst
├── ideation-agent-resource-scout
├── ideation-agent-hypothesis-architect
├── ideation-agent-pivot-advisor
└── ideation-agent-report-generator
```

## License

MIT
