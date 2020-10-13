## sad path 1 situation 4  
* start
  - action_link_talking
  - utter_greet 
  - action_set_situation
  - slot{"situation": "four"}
  - utter_turn_sit_4     
  - action_link_waiting         
* reject
  - action_link_talking            
  - utter_again_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting




## sad path 2 situation 4  
* start
  - action_link_talking
  - utter_greet 
  - action_set_situation
  - slot{"situation": "four"}
  - utter_turn_sit_4     
  - action_link_waiting         
* reject
  - action_link_talking            
  - utter_again_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting

## sad path 3 situation 4  
* start
  - action_link_talking
  - utter_greet 
  - action_set_situation
  - slot{"situation": "four"}
  - utter_turn_sit_4     
  - action_link_waiting         
* reject
  - action_link_talking            
  - utter_again_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustrated_sit_4
  - action_link_waiting