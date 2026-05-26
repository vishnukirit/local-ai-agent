from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool

from tools import generate_users, save_users


# Tool 1: generate users
def tool_generate():
    users = generate_users(["John", "Jane", "Mike"])
    return str(users)


# Tool 2: save users
def tool_save():
    users = generate_users(["John", "Jane", "Mike"])
    path = save_users(users)
    return f"Saved to {path}"


generate_tool = FunctionTool.from_defaults(fn=tool_generate)
save_tool = FunctionTool.from_defaults(fn=tool_save)

# Local LLM
llm = Ollama(model="tinyllama")

# Create agent
agent = ReActAgent(
    tools=[generate_tool, save_tool],
    llm=llm,
    verbose=True,
)