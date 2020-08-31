#!/usr/bin/sh

cd configuration_files

cp deployment_GSoC_conversationalAgent.xml executive_GSoC_conversationalAgent.conf conversationalAgent.conf humanObserverAgent_GUI.conf mission_GSoC_conversationalAgent.conf /home/robocomp/robocomp/components/robocomp-viriato/etcSim/

cp navigation_usecases.aggl /home/robocomp/robocomp/components/robocomp-viriato/aggl_plans/

cp path_blocked.aggt targetModelGSoC-none.aggt /home/robocomp/robocomp/components/robocomp-viriato/etc/

cd ..

python3 -m pip install --upgrade pip

sudo apt-get install gcc libpq-dev -y
sudo apt-get install python-dev  python-pip -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
pip3 install wheel

sudo apt-get install portaudio19-dev python-pyaudio
pip3 install PyAudio

sudo apt-get install festival festvox-kallpc16k

pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en


