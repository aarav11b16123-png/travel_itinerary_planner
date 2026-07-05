from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def packing_list_generator(state):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    prompt = f"""
    Generate a comprehensive packing list for a {state['preferences'].get('holiday_type', 'general')} holiday in {state['preferences'].get('destination', '')} during {state['preferences'].get('month', '')} for {state['preferences'].get('duration', 0)} days.
    Include essentials based on expected weather and trip type.
    """
    try:
        result = llm.invoke([HumanMessage(content=prompt)]).content
        return {"packing_list": result.strip()}
    except Exception as e:
        return {"packing_list": "", "warning": str(e)}