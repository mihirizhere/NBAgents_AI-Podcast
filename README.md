# NBAgents - AI Podcast

NBAgents is a multi-agent system designed to provide an entertaining podcast transcript on various topics concerning the National Basketball Association. The transcripts are saved to the outputs folder.
There are three agents: One moderator, one agent with a preference for the older style of play, and one agent with a preference for the modern NBA. The moderator begins the discsussion, generating
an insightful question adter choosing from a random list of topics. The project is aimed at creating an intelligent mulit-agent LLM system to generate useful dialogues using Python.

I am able to do this via accessing Mistral's LLM agents and prompting the different LLM models I have trained.

## Features

- **Moderator**: Mistral Nemo agent that specializes in consilidating discsussiona and providing thought-provoking questions.
- **Agent with Legacy Preference: Old Rick**: Mistral Large 2 agent that plays the role of an older analyst that prefers the older style of play.
- **Agent with Contemporary Preference: Young Nick**: Mistral Large 2 agent that plays the role of a younger analyst that prefers the modern NBA.
- **Podcast Transcription**: The insights are recorded and saved to an output file in the `outputs` folder.

## Future Work

Currently, we have the transcription that users can read and perform on their own. In the next iteration, to make this a true podcast, I will be researching and implementing methods to transform
the text transcript into a verbal conversation between the three characters.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mihirizhere/NBAgents_AI-Podcast.git
   pip install mistralai
   ```
2. Create your own Mistral API key:
    Go to [Mistral AI website](https://www.mistral.ai) and follow the steps to generate an API key if you do not have one Already
3. Replace the line
```
   api_key = os.environ["MISTRAL_API_KEY"]
```
  with your own API key

4. Run the program, wait a some time for the models to run and enjoy your transcript in the `outputs` folder!
