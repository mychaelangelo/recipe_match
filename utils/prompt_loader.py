from pathlib import Path

def load_prompt(prompt_name: str) -> str:
    """Load a prompt from the prompts directory"""
    prompt_path = Path(__file__).parent.parent / "prompts" / f"{prompt_name}.md"
    
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file {prompt_name}.md not found")
        
    return prompt_path.read_text().strip() 