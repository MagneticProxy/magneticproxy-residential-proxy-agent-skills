# Install the Magnetic Proxy product skill

Install the complete `skills/magneticproxy/` folder, including its `SKILL.md`, `references/` and `scripts/`. Install the other folders only when you want their companion workflows. Preserve folder names and relative paths.

For an agent supported by the [Skills CLI](https://github.com/vercel-labs/skills), run `npx skills add MagneticProxy/magneticproxy-residential-proxy-agent-skills --skill magneticproxy`. Use `--list` instead of `--skill magneticproxy` to preview all skills in this repository without installing them. The command installs instructions; it does not authenticate or activate a proxy.

## Any LLM or agent harness

1. Register `skills/magneticproxy/` as one skill or load its `SKILL.md` when the user asks to use or troubleshoot Magnetic Proxy.
2. Allow it to read its own references and, for code clients, run the ordinary Python 3 configuration helper when needed. Browser/computer use requires a compatible agent and an authenticated product session; the skill does not provide those capabilities itself.
3. If you also install a companion workflow, make its `SKILL.md` and `magneticproxy` available together.
4. Keep customer credentials in the product, extension, secret store or process environment; never add them to prompts, repositories, screenshots or generated files.

Starter request: `Use Magnetic Proxy to set up my Chrome profile for Spain, verify the actual exit country, and tell me whether the site I named loads through that route.`

## Optional Codex or OpenAI adapter

Each `agents/openai.yaml` file provides optional display and starter-prompt metadata. It is not required by the skill logic and can be ignored by Claude, GLM, DeepSeek, custom agents, and other compatible harnesses.

Magnetic Proxy is authenticated proxy transport, not an assumed data API or official MCP. See [COMPATIBILITY.md](COMPATIBILITY.md) for portability details.
