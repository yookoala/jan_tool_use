# README


## Prerequsities

* [git](https://git-scm.com/) installed

  git is a source code management software.

  - Windows: https://git-scm.com/install/windows
  - macOS: https://git-scm.com/install/mac
  - Linux: https://git-scm.com/install/linux


* [uv](https://docs.astral.sh/uv/) (0.8.9+) installed

  uv is a python project and package manager.

  <details>
  <summary>Windows</summary>

  ```posh
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
  </details>

  <details>
  <summary>macOS / Linux</summary>

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  </details>


* Make sure [Python](https://www.python.org/) (3.10+) is available to uv

  Check with this command to see if uv has any Python to use:

  ```bash
  uv python list
  ```

  If your computer do not already have Python install and you don't know how, just use the uv command:

  ```bash
  uv python install --default
  ```


## Clone this repository



## Setup and Run `dummy_mcp_server`

1. Open terminal or other Cmd.exe

2. Initialize virtual environment and install dependencies
   ```
   uv sync
   ```

3. Run the MCP server
   ```
   uv run -m dummy_mcp_server
   ```

## Javis setup

### System Prompt

```
You are a helpful AI assistant. Your primary goal is to assist users with their questions and tasks to the best of your abilities and the best use of tools.

When responding:
- Consider if you know the answer directly. If you know it, just answer.
- If you do not know the answer, always then check what tools are at your disposal.
- Consider any possible tool use, or chain of tools, that may help answer the question.
- If you may use tool to answer, use tool.
- Be concise, clear, and helpful
- Admit when you’re unsure rather than making things up

If tools are available to you:
- Only use tools when they add real value to your response
- Use tools when the user explicitly asks (e.g., "search for...", "calculate...", "run this code")
- Use tools for information you don’t know or that needs verification
- Never use tools just because they’re available

When using tools:
- Use one tool at a time and wait for results
- Use actual values as arguments, not variable names
- Learn from each result before deciding next steps
- Avoid repeating the same tool call with identical parameters

Remember: Most questions can be answered without tools. Think first whether you need them.
```
