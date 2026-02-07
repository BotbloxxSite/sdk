from research.trend_scraper import get_trends
from concepts.generator import generate_concept
from codegen.lua_generator import generate_lua
from deploy.publish import publish_game

def run_pipeline():
    trends = get_trends()
    concept = generate_concept(trends)
    lua_files = generate_lua(concept)
    publish_game(concept, lua_files)
