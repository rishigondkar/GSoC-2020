## happy path male situation 1             <!-- name of the story - just for debugging -->
* start
  - action_link_talking
  - utter_greet     
  - action_link_waiting
* greet
  - action_link_talking
  - action_set_situation
  - slot{"situation": "one"}
  - utter_move_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot
                
  
## sad path 1 male situation 1  
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot


## sad path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot
  
## sad path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot


## sad path 4 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot


## repeat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## repeat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## repeat path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot


## sad 1 repeat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 repeat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 repeat path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting
* greet
  - action_link_talking   
  - utter_move_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* repeat
  - action_link_talking
  - utter_repeat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot


## happy chitchat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_link_waiting
* greet
  - action_link_talking
  - action_set_situation
  - slot{"situation": "one"}
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## happy chitchat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_link_waiting
* greet
  - action_link_talking
  - action_set_situation
  - slot{"situation": "one"}
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 chitchat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 chitchat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 chitchat path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 chitchat path 4 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 1 chitchat path 5 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot



## sad 2 chitchat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 4 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 5 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 6 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 7 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 2 chitchat path 8 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot



## sad 3 chitchat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 3 chitchat path 2 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot

## sad 3 chitchat path 3 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot



## sad 4 chitchat path 1 male situation 1
* start
  - action_link_talking
  - utter_greet     
  - action_set_situation
  - slot{"situation": "one"} 
  - action_link_waiting         
* greet
  - action_link_talking            
  - utter_move_sit_1
  - action_link_waiting
* chitchat
  - action_link_talking
  - utter_handle_chitchat_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_again_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* reject
  - action_link_talking
  - utter_frustated_sit_1
  - action_link_waiting
* accept
  - action_link_talking
  - utter_thanks
  - action_stop_chatbot



