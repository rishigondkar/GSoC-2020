# conversationalAgent
Intro to component here

## Cloning this repository
```
git clone https://github.com/RishiGondkar/GSoC-2020.git
cd conversationalAgent
mkdir build
cd build
cmake ..
cd ..
```

## Dependencies
These Dependencies must be installed prior to run this component:
> make python3 as default using the following command
  ```
echo "alias python=python3" >> ~/.bash_aliases
source ~/.bash_aliases
  ```

```
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip3 install SpeechRecognition
sudo apt-get install python3-pyaudio
```
### Rasa Installations
```
pip3 install rasa==1.6.1
pip3 install rasa-sdk==1.6.1
```



## Configuration parameters
As any other component, *conversationalAgent* needs a configuration file to start. In
```
etc/config
```
you can find an example of a configuration file. We can find there the following lines:
```
# Endpoints for implements interfaces
AGMCommonBehavior.Endpoints=tcp -p 10258


# Endpoints for subscriptions interfaces
AGMExecutiveTopicTopic.Endpoints=tcp -p 18333


# Proxies for required interfaces
AGMExecutiveProxy = agmexecutive:tcp -h localhost -p 10198
InnerModelManagerProxy = innermodelmanager:tcp -h localhost -p 11175
LaserProxy = laser:tcp -h localhost -p 10003
OmniRobotProxy = omnirobot:tcp -h localhost -p 12238
RGBDProxy = rgbd:tcp -h localhost -p 10096



# This property is used by the clients to connect to IceStorm.
TopicManager.Proxy=IceStorm/TopicManager:default -p 9999


Ice.Warn.Connections=0
Ice.Trace.Network=0
Ice.Trace.Protocol=0

```


## Starting the component
To avoid changing the *config* file in the repository, we can copy it to the component's home directory, so changes will remain untouched by future git pulls:


- Before starting the component you must start the :
    - rcremoteserver
    - rcmanagersimple

> Create a file named .rcremote in the HOME folder, as indicated above. Add the following line to it: localhost#abcd123

- You can run the file deployment_GSoC_conversationalAgent.xml using the following command after starting the rcremoteserver:

```
rcmanagersimple deployment_GSoC_conversationalAgent.xml
```
To create config file:

```
cd <conversationalAgent's path>
```
```
cp etc/config config
```

After editing the new config file we can run the component:

```
python3 src/conversationalAgent config
```
