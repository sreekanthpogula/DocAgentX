from fastapi import FastAPI
from pydantic import BaseModel
from agent import DoctorAppointmentAgent
from langchain_core.messages import HumanMessage
import os

os.environ.pop("SSL_CERT_FILE", None)


app = FastAPI()

# Define the Pydantic model for the request body.
# The UserQuery class specifies the expected input structure for the API endpoint.
# It includes an integer id_number and a string messages field representing the user's query.
# Pydantic ensures that incoming data matches this schema for validation and type safety.
class UserQuery(BaseModel):
    id_number: int
    messages: str

agent = DoctorAppointmentAgent()

@app.post("/execute")
def execute_agent(user_input: UserQuery):
    app_graph = agent.workflow()
    
    # Prepare agent state as expected by the workflow
    # Convert user input messages into a format suitable for the agent
    # Here, we assume user_input.messages is a string that needs to be wrapped in a HumanMessage
    # If user_input.messages is already a list of messages, you can adjust this
    # accordingly to fit your application's needs.
    # For example, if user_input.messages is a single string, we wrap it in a HumanMessage.
    # If it's a list of messages, you might need to convert each message to HumanMessage format.
    # The HumanMessage class is used to encapsulate the user's input in a format that the
    # agent can process. This is important for maintaining the context of the conversation
    # and ensuring that the agent can understand and respond appropriately to the user's query.
    input = [
        HumanMessage(content=user_input.messages)
    ]
    query_data = {
        "messages": input,
        "id_number": user_input.id_number,
        "next": "",
        "query": "",
        "current_reasoning": "",
    }
    # Invoke the agent with the prepared data
    # Adjust recursion limit if necessary
    # Note: The recursion limit is set to 50, which should be sufficient for most workflows.
    # If you encounter issues with recursion depth, you can increase this limit.
    # However, be cautious with very high limits as it may lead to infinite loops.
    # The recursion limit is set to 50 to prevent infinite loops in the agent's reasoning
    # and to ensure that the agent can handle complex queries without running into recursion depth errors.

    response = app_graph.invoke(query_data,config={"recursion_limit": 50})
    return {"messages": response["messages"]}
