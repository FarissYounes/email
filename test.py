import langgraph
from langgraph.graph import StateGraph
from typing import TypedDict, List

# Define memory structure
class ChatState(TypedDict):
    messages: List[HumanMessage | AIMessage]

# Define chatbot logic
def chatbot_logic(state: ChatState) -> ChatState:
    messages = state["messages"]
    user_message = messages[-1]  # Last message is from the user

    # Call LLM API with history
    response = call_llm(user_message.content, messages)
    
    messages.append(response)  # Append AI response
    return {"messages": messages}

# Create LangGraph workflow
graph = StateGraph(ChatState)
graph.add_node("chatbot", chatbot_logic)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", "chatbot")  # Loop for continued conversation

# Compile chatbot
chatbot = graph.compile()

