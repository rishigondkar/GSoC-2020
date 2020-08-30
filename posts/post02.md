# ConversationalAgent RASA

## About Rasa
Rasa is an open source Conversational AI framework for building AI assistants and chatbots. One of it's unique feature is that its not tied to a prebuilt model or usecase. It can be customized according to our requirements.
Rasa has three main modules:
1. **Rasa NLU** for understanding user messages.
2. **Rasa Core** for holding conversations and deciding what to do next.
3. **Rasa Action Server** for triggering external actions like calling api's or making making external changes.

**Rasa NLU—** Here Rasa tries to undersatnd User message to detect **Intent** and **Entity** in the message. The component used by by NLU to detect intents in this project are Spacy and Tensorflow. We have created the following intents:
* start
* greet
* accept
* repeat
* reject
* goodbye
* chitchat
>The invocations for the intent are stored in the NLU.md file.

**Rasa Core—** Here Rasa helps with contextual message flow. Based on user message and intent classification by NLU it decides the response to be sent to the user. 
-The responses are selected from the actions pre-written in the domain.yml file in the template section. 
-The stories.md file contains the story templates. Rasa controls the flow of conversation between the user and chatbot according to theses templates, so for that flow, we need to train chatbot using these stories.

**Rasa Action Server—** This server handles the execution of actions defined iin actions.py file.




