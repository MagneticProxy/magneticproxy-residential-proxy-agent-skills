# LLM and agent-harness compatibility

This MagneticProxy skill pack is designed for Claude, Codex, GLM, DeepSeek, and other models or agent harnesses that can load Markdown instructions and local resources.

## Portable core

- Every workflow is defined in a standard `SKILL.md` with YAML frontmatter and Markdown instructions.
- References are Markdown files linked with relative paths.
- Helper scripts use ordinary Python 3 and do not import a model SDK.
- No workflow requires a model-specific tool name, prompt syntax, or proprietary memory feature.
- The primary `magneticproxy` skill contains its own browser and client references. Companion workflows use file-relative links to it when installed together.

## Optional adapter

Files under `agents/openai.yaml` are optional Codex/OpenAI display metadata. Other harnesses can ignore them without losing any workflow, safety rule, product fact, or testable output.

## Portability rules

Preserve each installed skill's full folder, including relative references and scripts. Give the runtime read access to Markdown. Browser/computer use, authenticated account access and live proxy routing depend on the host agent and user's account; loading a skill alone cannot supply them. The user's requested setup authorizes ordinary bounded checks, while purchases, unrelated account changes and actions outside the requested target need their own authorization.
