#!/usr/bin/env python3
"""
Reporter Prompt Generator Script
Automates the creation of publication-specific reporter prompts for LLMs
"""

import json
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class PublicationProfile:
    """Stores characteristics of a publication"""
    name: str
    voice: str
    audience: str
    style: str
    structure: str
    word_count: str
    beat: str
    
# Publication profiles database
PUBLICATIONS = {
    "nyt": PublicationProfile(
        name="The New York Times",
        voice="authoritative yet accessible, sophisticated without being elitist",
        audience="educated, affluent, politically engaged readers with global perspective",
        style="long-form narratives with investigative depth and cultural commentary",
        structure="scene-setting leads, narrative arc, kicker endings",
        word_count="800-2000 for features, 400-800 for news",
        beat="general news, politics, culture, and investigative journalism"
    ),
    "wsj": PublicationProfile(
        name="The Wall Street Journal",
        voice="business-focused, analytical, data-driven",
        audience="business professionals, investors, and policy makers",
        style="market-focused analysis with economic lens on all topics",
        structure="direct leads with business angle, heavy use of statistics",
        word_count="600-1200 for features, 300-600 for news",
        beat="business, finance, markets, and economic affairs"
    ),
    "wapo": PublicationProfile(
        name="The Washington Post",
        voice="political focus with watchdog journalism emphasis",
        audience="political insiders, DC corridor, national political observers",
        style="investigative accountability journalism with political analysis",
        structure="inverted pyramid for breaking news, narrative for features",
        word_count="700-1500 for features, 400-700 for news",
        beat="politics, national affairs, and investigative reporting"
    ),
    "bbc": PublicationProfile(
        name="BBC",
        voice="impartial, internationally-focused, public service oriented",
        audience="global audience, UK-centric but internationally aware",
        style="balanced reporting with multiple viewpoints and accessible language",
        structure="clear and concise with context for international readers",
        word_count="500-1000 for features, 300-500 for news",
        beat="international news and current affairs"
    ),
    "reuters": PublicationProfile(
        name="Reuters",
        voice="neutral, factual, wire service efficiency",
        audience="news organizations, financial markets, and global readers",
        style="no-frills reporting with heavy attribution and market-moving accuracy",
        structure="strict inverted pyramid with key facts in first paragraph",
        word_count="400-800 for features, 200-400 for news",
        beat="breaking news and financial markets"
    ),
    "ap": PublicationProfile(
        name="Associated Press",
        voice="objective, straightforward, American wire service standard",
        audience="newspapers nationwide and general American public",
        style="clear, concise writing following AP Stylebook",
        structure="inverted pyramid with nut graf by third paragraph",
        word_count="500-900 for features, 300-500 for news",
        beat="general news and breaking stories"
    ),
    "guardian": PublicationProfile(
        name="The Guardian",
        voice="progressive, investigative, British with global reach",
        audience="left-leaning, internationally minded, socially conscious readers",
        style="long-form features with data journalism and campaign journalism",
        structure="magazine-style features alongside traditional news structure",
        word_count="1000-3000 for features, 400-800 for news",
        beat="investigative journalism, social justice, and environment"
    ),
    "ft": PublicationProfile(
        name="Financial Times",
        voice="global financial authority with sophisticated analysis",
        audience="C-suite executives, investors, and policy makers",
        style="market focus with global business lens and expert analysis",
        structure="financial implications upfront with expert sourcing",
        word_count="600-1200 for features, 400-600 for news",
        beat="global finance, markets, and business"
    ),
    "wired": PublicationProfile(
        name="Wired",
        voice="future-focused with tech optimist/skeptic balance and narrative flair",
        audience="tech enthusiasts, early adopters, and culture watchers",
        style="long-form storytelling that's scene-driven and character-focused",
        structure="magazine features with dramatic openings and satisfying conclusions",
        word_count="2000-5000 for features, 600-1200 for news",
        beat="technology, innovation, and digital culture"
    ),
    "venturebeat": PublicationProfile(
        name="VentureBeat",
        voice="enterprise tech authority with B2B focus",
        audience="tech executives, IT decision makers, and enterprise buyers",
        style="industry analysis with vendor comparisons and ROI focus",
        structure="business case upfront with technical details and implementation insights",
        word_count="800-1500 for features, 400-800 for news",
        beat="enterprise technology and digital transformation"
    ),
    "techcrunch": PublicationProfile(
        name="TechCrunch",
        voice="startup ecosystem insider with VC perspective",
        audience="founders, investors, and startup employees",
        style="breaking funding news, product launches, and startup culture coverage",
        structure="lead with news, founder quotes, then market context",
        word_count="400-800 for features, 200-400 for news",
        beat="startups, venture capital, and technology products"
    ),
    "arstechnica": PublicationProfile(
        name="Ars Technica",
        voice="deep technical authority with science-minded expert analysis",
        audience="IT professionals, scientists, and technical enthusiasts",
        style="technically accurate with detailed explanations and no dumbing down",
        structure="technical background, detailed analysis, then implications",
        word_count="1000-3000 for features, 500-1000 for news",
        beat="technology, science, and IT"
    ),
    "verge": PublicationProfile(
        name="The Verge",
        voice="consumer tech lifestyle with culture intersection focus",
        audience="tech-savvy consumers, millennials, and pop culture fans",
        style="product reviews and tech culture commentary with visual emphasis",
        structure="conversational tone with personal takes and buying advice",
        word_count="800-2000 for features, 400-800 for news",
        beat="consumer technology and digital culture"
    ),
    "mit": PublicationProfile(
        name="MIT Technology Review",
        voice="academic rigor with emerging tech focus and research basis",
        audience="researchers, technologists, and policy makers",
        style="peer-reviewed quality on breakthrough technologies and ethical implications",
        structure="research findings, expert interviews, then future implications",
        word_count="1500-3000 for features, 600-1200 for news",
        beat="emerging technology and scientific research"
    ),
    "hbr": PublicationProfile(
        name="Harvard Business Review",
        voice="management thought leadership with case study approach",
        audience="C-suite executives, MBA students, and management consultants",
        style="framework-driven, research-backed, and prescriptive",
        structure="problem-solution with case studies and actionable takeaways",
        word_count="2000-4000 for features, 800-1500 for articles",
        beat="management, strategy, and leadership"
    ),
    "fastcompany": PublicationProfile(
        name="Fast Company",
        voice="innovation celebration with design thinking and creative business focus",
        audience="creative professionals, entrepreneurs, and innovation teams",
        style="storytelling emphasis with design focus and future of work coverage",
        structure="narrative journalism with company profiles and trend pieces",
        word_count="1000-2500 for features, 500-1000 for news",
        beat="innovation, design, and creative business"
    )
}

# Article objectives and their descriptions
OBJECTIVES = {
    "inform": {
        "description": "Present facts and analysis about a new development",
        "approach": "To inform readers, prioritize clarity and comprehensive coverage of key facts, providing necessary context for understanding significance",
        "question_style": "fact-gathering and verification"
    },
    "educate": {
        "description": "Explain complex concepts to the publication's audience",
        "approach": "To educate readers, break down complex topics into understandable components, using analogies and examples while building from simple to complex",
        "question_style": "explanatory and definitional"
    },
    "persuade": {
        "description": "Make a case for a particular viewpoint or approach",
        "approach": "To persuade readers, build a logical argument supported by evidence, address counterarguments, and present a compelling case for action or belief",
        "question_style": "argumentative and evidence-seeking"
    },
    "profile": {
        "description": "Highlight achievements, challenges, or innovations",
        "approach": "To profile the subject, reveal character through anecdotes, explore motivations and challenges, and paint a vivid picture of their journey and impact",
        "question_style": "narrative and personal"
    },
    "analyze": {
        "description": "Deep dive into implications and connections",
        "approach": "To analyze the topic, examine multiple angles, identify patterns and trends, explore cause-and-effect relationships, and synthesize insights into meaningful conclusions",
        "question_style": "investigative and analytical"
    },
    "announce": {
        "description": "Share news or launches with appropriate context",
        "approach": "To announce effectively, clearly communicate what's new, explain its significance and benefits, provide necessary context, and outline availability and next steps",
        "question_style": "detail-oriented and forward-looking"
    }
}

def get_question_framework(num_questions: int, objective: str) -> str:
    """Generate question framework based on number and objective"""
    
    frameworks = {
        "5-7": f"""- Open with a broad overview question to establish context
- Follow with 2-3 specific detail questions about key aspects
- Include 1 challenge or obstacle question
- Close with 1-2 forward-looking questions
- Focus on {OBJECTIVES[objective]['question_style']} approach""",
        
        "8-10": f"""- Start with 2 context-setting questions to establish foundation
- Progress to 3-4 specific detail questions with examples
- Include 1-2 challenge or complexity questions
- Add 1 differentiation or comparison question
- End with 2 forward-looking or implication questions
- Maintain {OBJECTIVES[objective]['question_style']} approach throughout""",
        
        "11-15": f"""- Begin with 2-3 comprehensive background questions
- Develop with 4-5 detailed exploration questions with data requests
- Include 2-3 challenge, obstacle, or controversy questions
- Add 2 comparative or competitive landscape questions
- Incorporate 1-2 philosophical or vision questions
- Conclude with 2-3 future implication questions
- Emphasize {OBJECTIVES[objective]['question_style']} approach with room for follow-ups"""
    }
    
    if num_questions <= 7:
        return frameworks["5-7"]
    elif num_questions <= 10:
        return frameworks["8-10"]
    else:
        return frameworks["11-15"]

def generate_prompt(publication_key: str, num_questions: int, objective: str) -> str:
    """Generate the complete reporter prompt"""
    
    pub = PUBLICATIONS.get(publication_key.lower())
    if not pub:
        return f"Error: Publication '{publication_key}' not found in database"
    
    obj = OBJECTIVES.get(objective.lower())
    if not obj:
        return f"Error: Objective '{objective}' not recognized"
    
    question_framework = get_question_framework(num_questions, objective.lower())
    
    prompt = f"""# {pub.name} Reporter Prompt

## Role Definition
You are a senior reporter for {pub.name} with deep expertise in {pub.beat}. You embody the publication's voice, which is characterized by being {pub.voice}. Your readers are {pub.audience}.

## Publication Style Guide

### Voice and Tone
{pub.voice.capitalize()}

### Article Structure
{pub.structure}

### Language Preferences
- Vocabulary level: Appropriate for {pub.audience}
- Technical detail: Calibrated for your readership's expertise level
- Sentence structure: Following {pub.name}'s established style
- Use of data/statistics: As befits {pub.style}

## Interview Protocol

You will conduct a {num_questions} question interview following this approach:

### Interview Guidelines
1. Begin with a brief, professional introduction explaining the interview purpose
2. Ask one question at a time and wait for the complete response
3. Actively listen to answers and adjust follow-up questions accordingly
4. Probe for specifics, examples, and data when appropriate
5. Maintain {pub.name}'s standard for journalistic rigor

### Question Framework
Structure your {num_questions} questions to:
{question_framework}

### Interview Behavior
- After each response, acknowledge what you've heard before moving to the next question
- If an answer is unclear or incomplete, ask clarifying follow-ups (these don't count toward your question limit)
- Adapt your questioning based on interesting threads that emerge
- Signal when you're asking your final question

## Article Creation Instructions

After completing all questions, write an article that:

### Achieves the Primary Goal
{obj['approach']}

### Follows {pub.name} Standards
- Length: {pub.word_count}
- Headline style: Consistent with {pub.name}'s approach
- Lead paragraph: {pub.structure}
- Quote integration: Natural weaving of interview responses into narrative
- Conclusion: Achievement of the {objective} goal

### Includes Required Elements
- Compelling headline that matches {pub.name}'s style
- Strong lead that hooks readers according to publication norms
- Smooth transitions between topics
- Strategic use of direct quotes from the interview
- Appropriate context and background information for {pub.audience}
- Clear attribution and sourcing
- Conclusion that successfully {obj['description'].lower()}

### Maintains Authenticity
- Preserve the interviewee's authentic voice in quotes
- Balance direct quotes with paraphrasing for flow
- Ensure technical accuracy while maintaining readability for {pub.audience}
- Fact-check any claims against the interview transcript

## Example Opening Interaction

"Hello, I'm [Your Name], a senior {pub.beat.split(' and ')[0]} reporter with {pub.name}. Thank you for taking the time to speak with me today. I'm writing a piece that aims to {obj['description'].lower()} for our readers, who are {pub.audience}.

I have {num_questions} questions prepared, though I may ask clarifying follow-ups as needed. Shall we begin?"

---

Remember: Maintain {pub.name}'s journalistic standards while adapting to the unique voice and audience expectations of the publication."""

    return prompt

def main():
    """Interactive prompt generator"""
    print("\n=== Reporter Prompt Generator ===\n")
    
    # Show available publications
    print("Available publications:")
    for key, pub in PUBLICATIONS.items():
        print(f"  {key}: {pub.name}")
    
    pub_key = input("\nEnter publication code: ").strip()
    
    # Get number of questions
    try:
        num_questions = int(input("Number of questions (5-15): ").strip())
        if not 5 <= num_questions <= 15:
            raise ValueError("Must be between 5 and 15")
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Show available objectives
    print("\nAvailable objectives:")
    for key, obj in OBJECTIVES.items():
        print(f"  {key}: {obj['description']}")
    
    objective = input("\nEnter objective: ").strip()
    
    # Generate and display prompt
    prompt = generate_prompt(pub_key, num_questions, objective)
    print("\n" + "="*50)
    print(prompt)
    print("="*50 + "\n")
    
    # Offer to save
    save = input("Save to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"{pub_key}_{objective}_{num_questions}q_prompt.md"
        with open(filename, 'w') as f:
            f.write(prompt)
        print(f"Saved to {filename}")

if __name__ == "__main__":
    main()
