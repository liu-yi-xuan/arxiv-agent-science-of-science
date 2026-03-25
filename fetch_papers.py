#!/usr/bin/env python3
"""
Daily ArXiv Paper Fetcher — AI Agents x Science of Science.

Searches ArXiv for recent papers at the intersection of AI agents and
the scientific research process. Classifies, generates TLDRs, and
auto-updates the README.md.
"""

import arxiv
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────────

QUERIES = {
    "AI Agents for Scientific Discovery": [
        # Agents doing science — hypothesis, experiments, labs
        "ti:agent AND ti:scientific AND ti:discovery",
        "ti:LLM AND ti:scientific AND ti:discovery",
        "ti:agent AND ti:hypothesis AND cat:cs.AI",
        "ti:agent AND ti:experiment AND cat:cs.AI",
        "ti:AI AND ti:scientist",
        "ti:agent AND ti:drug AND ti:discovery",
        "ti:agent AND ti:chemistry AND cat:cs.AI",
        "ti:agent AND ti:mathematics AND ti:reasoning",
        "ti:autonomous AND ti:research AND cat:cs.AI",
        "ti:LLM AND ti:laboratory",
    ],
    "Research Workflow Agents": [
        # Agents for literature review, writing, peer review, knowledge extraction
        "ti:agent AND ti:literature AND ti:review",
        "ti:agent AND ti:research AND ti:idea",
        "ti:LLM AND ti:peer AND ti:review",
        "ti:agent AND ti:paper AND ti:writing",
        "ti:LLM AND ti:knowledge AND ti:extraction AND cat:cs.CL",
        "ti:agent AND ti:summarization AND ti:scientific",
        "ti:LLM AND ti:survey AND ti:generation",
        "ti:agent AND ti:tool AND ti:use AND cat:cs.CL",
        "ti:LLM AND ti:agent AND ti:planning",
        "ti:autonomous AND ti:agent AND cat:cs.CL",
    ],
    "Multi-Agent Scientific Collaboration": [
        # Multi-agent systems for research teams, debate, collaborative discovery
        "ti:multi-agent AND ti:scientific",
        "ti:multi-agent AND ti:research",
        "ti:agent AND ti:debate AND cat:cs.AI",
        "ti:agent AND ti:collaboration AND ti:scientific",
        "ti:multi-agent AND cat:cs.AI AND ti:reasoning",
        "ti:generative AND ti:agent AND ti:simulation",
        "ti:multi-agent AND ti:framework AND cat:cs.AI",
        "ti:agent AND ti:communication AND cat:cs.CL",
    ],
    "Computational Science of Science": [
        # Citation dynamics, research trends, scientometrics, knowledge diffusion
        "ti:science AND ti:science AND cat:cs.DL",
        "ti:scientometrics",
        "ti:citation AND ti:analysis AND cat:cs.DL",
        "ti:research AND ti:dynamics AND cat:cs.DL",
        "ti:knowledge AND ti:diffusion AND ti:scientific",
        "ti:citation AND ti:prediction",
        "ti:research AND ti:impact AND cat:cs.DL",
        "ti:scientific AND ti:knowledge AND ti:graph",
        "ti:scholarly AND ti:communication",
        "ti:meta-research",
        "ti:bibliometric",
    ],
    "Benchmarks & Evaluation for Research Agents": [
        # Measuring agent capabilities in scientific contexts
        "ti:agent AND ti:benchmark AND ti:scientific",
        "ti:agent AND ti:evaluation AND ti:science",
        "ti:agent AND ti:benchmark AND cat:cs.AI",
        "ti:agent AND ti:reproducibility",
        "ti:LLM AND ti:evaluation AND ti:research",
        "ti:agent AND ti:benchmark AND cat:cs.CL",
    ],
}

CATEGORY_EMOJI = {
    "AI Agents for Scientific Discovery": "🔬",
    "Research Workflow Agents": "📖",
    "Multi-Agent Scientific Collaboration": "🧠",
    "Computational Science of Science": "📊",
    "Benchmarks & Evaluation for Research Agents": "🛠️",
}

MAX_RESULTS_PER_QUERY = 10
LOOKBACK_DAYS = 3  # Look back 3 days to catch papers from weekends


def fetch_papers_for_category(category: str, queries: list[str]) -> list[dict]:
    """Fetch papers from ArXiv for a given category."""
    client = arxiv.Client()
    seen_ids = set()
    papers = []

    for query_str in queries:
        search = arxiv.Search(
            query=query_str,
            max_results=MAX_RESULTS_PER_QUERY,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        try:
            for result in client.results(search):
                paper_id = result.entry_id.split("/")[-1]
                if paper_id in seen_ids:
                    continue
                seen_ids.add(paper_id)

                # Filter: only papers from the last N days
                cutoff = datetime.now(result.published.tzinfo) - timedelta(days=LOOKBACK_DAYS)
                if result.published < cutoff:
                    continue

                papers.append({
                    "id": paper_id,
                    "title": result.title.replace("\n", " ").strip(),
                    "authors": [a.name for a in result.authors[:5]],
                    "abstract": result.summary.replace("\n", " ").strip(),
                    "url": result.entry_id,
                    "pdf_url": result.pdf_url,
                    "published": result.published.strftime("%Y-%m-%d"),
                    "categories": [c for c in result.categories],
                    "primary_category": result.primary_category,
                    "our_category": category,
                })
        except Exception as e:
            print(f"  ⚠️  Error fetching '{query_str}': {e}")

    return papers


def generate_tldr(abstract: str) -> str:
    """Generate a TLDR from the abstract.

    Uses a simple extractive approach: takes the first 1-2 sentences
    and trims to a reasonable length. For better TLDRs, you can plug
    in an LLM API here (e.g., OpenAI, Anthropic).
    """
    text = abstract.strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)

    tldr = sentences[0]
    if len(sentences) > 1 and len(tldr) < 100:
        tldr = tldr + " " + sentences[1]

    if len(tldr) > 200:
        tldr = tldr[:197] + "..."

    return tldr


def deduplicate_papers(all_papers: list[dict]) -> list[dict]:
    """Remove duplicate papers across categories, keeping first occurrence."""
    seen = set()
    unique = []
    for paper in all_papers:
        if paper["id"] not in seen:
            seen.add(paper["id"])
            unique.append(paper)
    return unique


def save_daily_json(papers: list[dict], date_str: str):
    """Save fetched papers to a JSON archive."""
    papers_dir = Path("papers")
    papers_dir.mkdir(exist_ok=True)

    filepath = papers_dir / f"{date_str}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)

    print(f"  💾 Saved {len(papers)} papers to {filepath}")
    return filepath


def update_readme(papers: list[dict], date_str: str):
    """Update README.md with today's papers."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("  ❌ README.md not found!")
        return

    content = readme_path.read_text(encoding="utf-8")

    # Build today's section
    if not papers:
        today_section = f"\n### 📅 {date_str}\n\n*No new papers found today.*\n"
    else:
        by_category: dict[str, list[dict]] = {}
        for p in papers:
            cat = p["our_category"]
            by_category.setdefault(cat, []).append(p)

        today_section = f"\n### 📅 {date_str}\n\n"
        today_section += f"**{len(papers)} new papers found**\n\n"

        for category, cat_papers in by_category.items():
            emoji = CATEGORY_EMOJI.get(category, "📄")
            today_section += f"#### {emoji} {category}\n\n"
            today_section += "| Title | Authors | TLDR |\n"
            today_section += "|-------|---------|------|\n"

            for p in cat_papers:
                title_link = f"[{p['title']}]({p['url']})"
                authors = ", ".join(p["authors"][:3])
                if len(p["authors"]) > 3:
                    authors += " et al."
                tldr = generate_tldr(p["abstract"])
                tldr = tldr.replace("|", "\\|")
                today_section += f"| {title_link} | {authors} | {tldr} |\n"

            today_section += "\n"

    # Insert after the DAILY_UPDATES_START marker
    marker_start = "<!-- DAILY_UPDATES_START -->"
    marker_end = "<!-- DAILY_UPDATES_END -->"

    if marker_start in content and marker_end in content:
        start_idx = content.index(marker_start) + len(marker_start)
        end_idx = content.index(marker_end)
        existing = content[start_idx:end_idx]

        existing = existing.replace("*Updates will appear here automatically.*", "").strip()

        new_content = (
            content[:start_idx]
            + "\n"
            + today_section
            + existing
            + "\n"
            + content[end_idx:]
        )

        readme_path.write_text(new_content, encoding="utf-8")
        print(f"  ✅ README.md updated with {len(papers)} papers")
    else:
        print("  ⚠️  Could not find update markers in README.md")


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"🔍 Fetching papers for {date_str}...")
    print(f"   Looking back {LOOKBACK_DAYS} days\n")

    all_papers = []

    for category, queries in QUERIES.items():
        print(f"  📂 {category}...")
        papers = fetch_papers_for_category(category, queries)
        print(f"     Found {len(papers)} papers")
        all_papers.extend(papers)

    # Deduplicate
    all_papers = deduplicate_papers(all_papers)
    print(f"\n📊 Total unique papers: {len(all_papers)}")

    # Save JSON archive
    save_daily_json(all_papers, date_str)

    # Update README
    update_readme(all_papers, date_str)

    print("\n✨ Done!")
    return all_papers


if __name__ == "__main__":
    main()
