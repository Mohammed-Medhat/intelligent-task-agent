from tools.search_tool import search_google
from tools.scraper_tool import scrape_and_clean
import time

def run_research(subtask):
    print(f"🔍 Searching for: {subtask}")
    search_results = search_google(subtask)

    if not search_results:
        print("⚠️ No search results found. Skipping.")
        return {"subtask": subtask, "content": "No results found."}

    top_links = [r.get('link') for r in search_results[:5] if r.get('link')]
    collected = []

    for link in top_links:
        print(f"🔗 Trying to scrape: {link}")
        retries = 3
        for attempt in range(retries):
            try:
                page_text = scrape_and_clean(link)

                # Quality check: minimal length
                if len(page_text) < 300:
                    print(f"⚠️ Skipped (too short): {link}")
                    break

                # Optional: remove excessive whitespace
                page_text = " ".join(page_text.split())

                collected.append(f"[Source: {link}]\n{page_text[:2000]}")
                break  # success, move to next link

            except Exception as e:
                print(f"❌ Attempt {attempt+1} failed for {link}: {e}")
                time.sleep(1)  # backoff

    if not collected:
        return {"subtask": subtask, "content": "No valid sources found."}

    all_content = "\n\n".join(collected)
    return {"subtask": subtask, "content": all_content}
