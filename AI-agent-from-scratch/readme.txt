This folder had code to create AI agents in python.
It uses anaconda to set-up & manage python environments & the VScode IDE.

#1
To set-up the ai-agents-env python environment run:
>> conda env create -f ./ai-agents-env.yml
>> conda activate ai-agents-env

#2
>> conda init
--> restart terminal
>> conda activate ai-agents-env

#3
To set-up VS code for python
--> Reach for and install the Python extension for VScode

#4
If using github codespaces, set-up API_KEYs as github secrets and check that the API KEYS are available in the codespace
>> echo $OPENAI_API_KEY
>> echo $ANTHROPIC_API_KEY

If using local machine, set-up API_KEYS in .env & use the dotenv python packahe to load & access environment variables.
*** ensure .env is listed in the .gitignore file, so that it does not get committed to github ***

