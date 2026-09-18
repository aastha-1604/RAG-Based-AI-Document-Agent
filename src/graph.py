from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from src.rag import answer_from_document
from src.web_search import answer_from_web

class AgentState(TypedDict):

    question: str

    document_id: str

    answer: str

    source: str

def document_node(state: AgentState):

    answer = answer_from_document(
        state["question"],
        state["document_id"]
    )

    return {
        "answer": answer,
        "source": "document"
    }

def web_node(state: AgentState):

    question = state["question"]

    answer = answer_from_web(
        question
    )

    return {
        "answer": answer,
        "source": "web"
    }

def route_answer(state: AgentState):

    answer = state["answer"]

    if "INSUFFICIENT_CONTEXT" in answer:

        return "web"

    return "end"

def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node(
        "document",
        document_node
    )

    builder.add_node(
        "web",
        web_node
    )

    builder.add_edge(
        START,
        "document"
    )

    builder.add_conditional_edges(
        "document",
        route_answer,
        {
            "web": "web",
            "end": END
        }
    )

    builder.add_edge(
        "web",
        END
    )

    graph = builder.compile()

    return graph