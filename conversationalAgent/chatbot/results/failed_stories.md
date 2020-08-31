## sad path 4 female situation 1
* greet
    - action_link_talking
    - utter_greet
    - action_set_situation
    - slot{"situation": "one"}
    - action_set_gender
    - slot{"gender": "female"}
    - utter_move_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_again_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_female_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_female_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* accept
    - action_link_talking
    - utter_thanks
    - utter_regards
    - action_link_waiting


## sad path 3 male situation 1
* greet
    - action_link_talking
    - utter_greet
    - action_set_situation
    - slot{"situation": "one"}
    - action_set_gender
    - slot{"gender": "male"}
    - utter_move_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_again_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_male_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* accept
    - action_link_talking
    - utter_thanks
    - utter_regards
    - action_link_waiting


## sad path 3 female situation 1
* greet
    - action_link_talking
    - utter_greet
    - action_set_situation
    - slot{"situation": "one"}
    - action_set_gender
    - slot{"gender": "female"}
    - utter_move_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_again_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_female_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_female_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* accept
    - action_link_talking
    - utter_thanks
    - utter_regards
    - action_link_waiting


## sad path 4 male situation 1
* greet
    - action_link_talking
    - utter_greet
    - action_set_situation
    - slot{"situation": "one"}
    - action_set_gender
    - slot{"gender": "male"}
    - utter_move_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_again_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_male_1
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_male_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* reject
    - action_link_talking
    - utter_frustated_male_1   <!-- predicted: action_link_talking -->
    - action_link_waiting
* accept
    - action_link_talking
    - utter_thanks
    - utter_regards
    - action_link_waiting


