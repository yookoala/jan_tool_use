# Jan: Tool Using Demo

This software is to demonstrate MCP server development for a workshop.

The software is shared on GitHub: https://github.com/yookoala/jan_tool_use


## Prerequsities

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
  uv python install 3.12
  ```

  **Note:** the function "speak" depends Deepgram's official client. As of 6th Feb 
  2026, the client have problem with Python 3.14. If you want to use the tool, use
  Python 3.13 or prior.


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


## Jan Setup

### MCP Server

Add MCP server with the following information:

| Field          | Value                                            |
| -------------- | ------------------------------------------------ |
| Name           | Dummy MCP Server *(doesn't matter what you set)* |
| Transport Type | HTTP *(Streamable HTTP)*                         |
| URL            | http://localhost:8080/mcp                        |

### Jan Assistant setup

Note: This is a known working setup.

#### Instruction

(a.k.a. "System Prompt")

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

### Model Choice

- [Jan-v3-4B-base-instruct](https://huggingface.co/janhq/Jan-v3-4B-base-instruct)
- [Ministral-3-3B-instruct-2512](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512)
- [Qwen3-4B-instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)

Note: If you want to try other models, remember these:

- Models usually named with the number of parameter (e.g. "4B", "8B"). The more the
  parameters, the more video memory (VRAM) your machine need to have.
- Not all model support "tool using". The models with the name "instruct" are usually
  optimized for "tool using".


## License

This software is licensed under the MIT license. A copy of the license can be
found [here](LICENSE.md).