from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import json 

def generate_itinerary(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    prompt = f"""
    Using the following preferences, create a detailed itinerary:
    {json.dumps(state['preferences'], indent=2)}

    Include sections for each day, dining options, and downtime.
    """
    try:
        result = llm.invoke([HumanMessage(content=prompt)]).content
        return {"itinerary": result.strip()}
    except Exception as e:
        return {"itinerary": "", "warning": str(e)}