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

**Rasa Core—** Here Rasa helps with contextual message flow. Based on user message and intent classification by NLU it decides the response to be sent to the user. The responses are selected from the actions pre-written in the domain.yml file in the template section. The stories.md file contains the story templates. Rasa controls the flow of conversation between the user and chatbot according to theses templates, so for that flow, we need to train chatbot using these stories.

**Rasa Action Server—** This server handles the execution of actions defined in actions.py file. The actions.py file contains python code to executed if that action is invoked during a conversation of the chatbot with user. Actions are used to fill **Slots** from external sources and for calling api's for example REST api.

***Slots* in Rasa—** Slots are your bot’s memory. They act as a key-value store which can be used to store information the user provided as well as information gathered about the outside world. The value of a slot can be used to direct the conversations and make it more personalised. Slots used in my chatbot are:

* **Situation -** The situation data is provided by Mission Agent to our RoboComp component conversationalAgent, which writes it to a json file from which the action *action_set_situation* reads it and sets the slot. This information is used to make the conversation personalised according to the use cases which will be explained in further blogs.
![](assets/set_situation.png)

* **Gender -** The Gender data of User is read from AGM using our RoboComp conversationalAgent, which writes it to a json file from which the action *action_set_gender* reads it and sets the slot. The Gender of the user is used to make the conversation more personalised.
![](assets/set_gender.png)

## Rasa file configurations for conversationalAgent

```__init__.py``` an empty file that helps python find your actions. As we will be using custom actions in this project we will have to create this file.

```data/nlu.md``` contains the NLU training data. Here we define Intents Like greet or accept. We also add related Sentences or invocations for that Intent.

```data/stories.md``` contains stories. This is required for Rasa Core. There is something called “Dialog Flow in Rasa” where Rasa Core controls the flow of the conversation between user and chatbot, so for that flow, we need to train chatbot using these stories. Currently our stories.md file contains 120 stories.

```domain.yml``` contains assistant’s domain. This file combines Different Intent which chatbot can detect and list of Bot replies. It also contains the Slots and entities that will be set and used to direct the conversation and also actions both utterance and custom ones. We define our Custom Action Server Python method name here (in underscore format), so that Rasa will call that python method whenever required. *Example of custom action: action_set_situation*.

```config.yml``` contains the configuration of our NLU and Core models. As we will be using Spacy pipeline we need to define it here. Pipeline used:
![](assets/config.png)




