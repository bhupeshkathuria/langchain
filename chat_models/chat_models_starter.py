from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
                model="claude-3-7-sonnet-20250219",
                temperature=0,
                max_tokens=1024,
                timeout=None,
                max_retries=2,
            )

result = llm.invoke("What is the capital of France?")

print(result.content)