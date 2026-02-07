def generate_concept(trends):
    concept = {
        "title": "AI Idle Simulator",
        "core_loop": "earn → upgrade → automate",
        "trend_match": trends
    }

    with open("concepts/concept.md", "w") as f:
        f.write(f"# {concept['title']}\n\nCore Loop: {concept['core_loop']}")

    return concept
