import os
import random
import textwrap
from datetime import datetime
from mistralai import Mistral


api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

old_head_id = "ag:f6cbe13c:20240917:oldhead-nba:aff9f336"
young_agent_id = "ag:f6cbe13c:20240917:young-bull:8c6a801c"
moderator_agent_id = "ag:f6cbe13c:20240917:untitled-agent:fce33e9e"


def call_agent(id, query):
    """Send prompt to Mistral AI agent"""
    try:
        response = client.agents.complete(
            agent_id=id,
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Request failed: {e}.")
        return None


def generate_podcast_transcript(interest, num_exchanges=2):
    """Generate a podcast transcript with randomly given topic and number of exchanges."""
    transcript = (f"Moderator: This is the NBA Times podcast, I am your host, Today, will be a fun time, "
                  f"as we're discussing {interest}. We'll hear from our two Correspondents: Old Rick and Young Nick .\n\n")

    for _ in range(num_exchanges):
        # Moderator poses a question
        mod_prompt = (f"You are the moderator for an NBA podcast between two agents. Ask a question like {topic} that "
                      f"will fuel a debate between an old school NBA fan and a modern NBA fan.")
        question = call_agent(moderator_agent_id, mod_prompt)
        transcript += f"Host: {question}\n\n"

        old_prompt = (f"You are an expert who prefers older NBA players and the way the game was played in the past. "
                      f"Respond to this: {question}")
        old_response = call_agent(old_head_id, old_prompt)
        transcript += f"Old Rick: {old_response}\n\n"

        new_prompt = (f"You are an expert who prefers current NBA players and the modern game. Respond to this "
                      f"question and address the points made by the Older expert if you can: {question}\n\n"
                      f"Old School expert's previous response: {old_response}")
        new_response = call_agent(young_agent_id, new_prompt)
        transcript += f"Young Nick: {new_response}\n\n"

    conclusion_prompt = ("You are the moderator of an NBA podcast. Provide a brief conclusion to wrap up the "
                         "discussion between the old NBA fan and modern NBA fan.")
    conclusion = call_agent(moderator_agent_id, conclusion_prompt)
    transcript += f"Moderator: {conclusion}\n\n"

    return transcript


def save(transcript, topic):
    """Save transcript to an output file in output directory"""
    os.makedirs('outputs', exist_ok=True)

    time = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = f"NBA_Times_{time}.txt"
    path = os.path.join('outputs', name)

    wrap = textwrap.fill(transcript, width=120)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"NBA Time Machine Podcast\n")
        f.write(f"Topic: {topic}\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(wrap)


topics = [
    "How the game has changed over time",
    "How the three point shot has become so important",
    "Shaquille O'Neal versus Derrick Rose",
    "The best players of all time",
    "More important: Team accomplishments vs. individual accolades"
]

topic = random.choice(topics)
outputs = generate_podcast_transcript(topic)
save(outputs, topic)
