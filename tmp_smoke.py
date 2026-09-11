import asyncio
from backend.services.topic_search_service import synthesize_topic_content

async def main():
    result = await synthesize_topic_content("artificial intelligence", model_choice="nemotron")
    print("SUCCESS", result["success"], result.get("model_used"))
    print(result["synthesized_text"][:400])

asyncio.run(main())
