import pytest
from unittest.mock import patch, MagicMock
from langchain.prompts import PromptTemplate

@pytest.fixture
def mock_chain_response():
    return {"text": "This is the revised message."}

def test_prompt_template_renders_correctly():
    prompt_template = PromptTemplate(
        template="""Please revise the following message for {use_case}: {message}""",
        input_variables=["use_case", "message"]
    )

    result = prompt_template.format(use_case="email", message="helo world")
    assert "helo world" in result
    assert "email" in result

@patch("app.LLMChain")
def test_llm_chain_invocation(mock_llm_chain_class, mock_chain_response):
    mock_chain_instance = MagicMock()
    mock_chain_instance.invoke.return_value = mock_chain_response
    mock_llm_chain_class.return_value = mock_chain_instance

    from app import prompt, chat_model
    from langchain.chains import LLMChain

    llm_chain = LLMChain(prompt=prompt, llm=chat_model)
    response = llm_chain.invoke({"use_case": "email", "message": "hi"})

    assert "revised message" in response["text"].lower()
