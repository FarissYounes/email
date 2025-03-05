from langraph.graph import StateGraph
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import SystemMessage, HumanMessage

# Define a state graph for chatbot flow
graph = StateGraph()

# Define a prompt template for chatbot interactions
prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
    You are a helpful AI assistant. Respond to the user's query thoughtfully.
    
    User: {user_input}
    AI:
    """
)

# Define a chatbot function using the template
def chatbot_logic(state):
    llm = ChatOpenAI()
    formatted_prompt = prompt.format(user_input=state["user_message"])
    response = llm([SystemMessage(content="You are an AI assistant."), HumanMessage(content=formatted_prompt)])
    return {"bot_response": response.content}

# Add chatbot logic to graph
graph.add_node("chatbot", chatbot_logic)

# Define input and output states
graph.set_entry_point("chatbot")
graph.set_exit_point("chatbot")

# Compile the graph
compiled_graph = graph.compile()

# Example usage
user_message = "What is the capital of France?"
result = compiled_graph.invoke({"user_message": user_message})
print(result["bot_response"])
