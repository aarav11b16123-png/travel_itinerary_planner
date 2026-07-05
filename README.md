**AI Travel Itinerary Planner**

**Live Demo:** [https://your-app-url.streamlit.app](https://travelitineraryplanner-tt2bq7wuyjvtpbxbzj2fxz.streamlit.app/)

A Streamlit web app that generates personalized travel itineraries using the Gemini API. Users provide their destination, travel month, trip length, group size, and preferences, and the app generates a day-by-day itinerary along with activity suggestions, weather forecasts, packing lists, local food/culture tips, and useful travel links.

**Features**


Itinerary Generation – Creates a detailed day-by-day plan based on destination, holiday type, budget, and trip length
Activity Recommendations – Suggests activities tailored to the trip preferences
Weather Forecast – Provides a general weather outlook for the travel month
Packing List Generator – Builds a packing checklist based on destination and trip length
Food & Culture Tips – Shares local food and cultural etiquette suggestions
Useful Links – Pulls relevant travel resources using the Serper search API
PDF Export – Exports the generated itinerary as a downloadable PDF
Chat Follow-up – Lets users ask follow-up questions about their itinerary


**Tech Stack**


Frontend/UI: Streamlit
LLM: Google Gemini API (gemini-2.5-flash) via langchain-google-genai
Search: Serper API (langchain_community.utilities.GoogleSerperAPIWrapper)
Orchestration: LangGraph (used for the initial itinerary generation step)
PDF Export: fpdf


**Setup**

Clone the repo and install dependencies:

pip install -r requirements.txt

Create a .env file in the project root with:

   GOOGLE_API_KEY=your_gemini_api_key
   SERPER_API_KEY=your_serper_api_key

Get a Gemini API key from Google AI Studio
Get a Serper API key from serper.dev

Run the app:

   streamlit run travel_agent.py

Open http://localhost:8501 in your browser.

**Notes**

Each feature (itinerary, activities, weather, packing list, etc.) is implemented as an independent LLM-powered function under agents/, called directly from the Streamlit UI.


**Future Scope**

Retrieval-Augmented Generation (RAG): Embed real travel guides and destination data into a vector database so the itinerary agent retrieves grounded, up-to-date context instead of relying solely on the LLM's training knowledge.
True multi-agent orchestration: Use LangGraph's conditional routing so a supervisor agent decides which sub-agent to call based on the user's query, rather than each feature being triggered directly by a UI button.
Persistent conversation memory: Give the chat agent proper memory of past exchanges and generated itineraries using LangGraph's checkpointing, instead of resending the itinerary text on every turn.
Multi-city / multi-leg itineraries: Support trips spanning multiple destinations with automatic transit suggestions between them.
User accounts and saved trips: Allow users to save, revisit, and edit previously generated itineraries.
<img width="1920" height="916" alt="Screenshot (1655)" src="https://github.com/user-attachments/assets/26e103f1-8c9e-4fb1-99ea-00971e1e2e5e" />
<img width="1920" height="889" alt="Screenshot (1654)" src="https://github.com/user-attachments/assets/4deb787b-e044-4eb9-a739-5e335974cc9b" />

