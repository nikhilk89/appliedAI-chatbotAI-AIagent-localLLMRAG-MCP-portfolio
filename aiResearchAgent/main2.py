import json
from dotenv import load_dotenv
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
# import tools here
from tools import save_tool, search_tool
# import llm api key here
load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


parser = PydanticOutputParser(pydantic_object=ResearchResponse)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant. Answer the user query using tools if needed.\n"
            "Respond ONLY using this JSON schema:\n{format_instructions}",
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, save_tool]

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


if __name__ == "__main__":
    query = input("What can I help you research? ").strip()
    if not query:
        exit()

    result = agent_executor.invoke({"query": query})
    output = result.get("output", "")

    # Extract text from agent response- if in chunks
    if isinstance(output, list):
        text_parts = []
        for chunk in output:
            if isinstance(chunk, dict):
                text_parts.append(chunk.get("text", ""))
            else:
                text_parts.append(str(chunk))
        output = "".join(text_parts)

    # reformat json response - remove backtics
    if "```" in output:
        output = output.split("```")[1]
        if output.startswith("json"):
            output = output.replace("json", "", 1)
        output = output.strip()

    try:
        data = parser.parse(output)
        print("\n--- RESEARCH SUMMARY ---")
        print(f"Topic: {data.topic}")
        print(f"Summary: {data.summary}")
        print(f"Sources: {', '.join(data.sources)}")
        print(f"Tools Used: {', '.join(data.tools_used)}")
    except Exception as e:
        print(f"\nFailed to parse model output: {e}")
        print("Raw text received:", output)