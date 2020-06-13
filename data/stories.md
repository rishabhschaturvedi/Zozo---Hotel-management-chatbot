## happy path
* greet
  - utter_greet
* chitchat
  - utter_feelings
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* chitchat
  - utter_feelings

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_wellwish

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
## say welcome
* thank_you
  - utter_welcome
  
## Handle FAQs
* greet
  - utter_greet
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
  - action_faqs
  
## Handle FAQs 2
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
  - action_faqs
  
## book_room 1
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
	- form{"name": null}
* thank_you
  - utter_welcome
  - utter_happy

## book_room 2
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
	- form{"name": null}
* thank_you
  - utter_welcome
  - utter_happy
  
## book_room 3
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
	- form{"name": null}
	
## book_room 4
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
	- form{"name": null}

## book_room + faqs 
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
	- form{"name": null}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
  - action_faqs
  
## book_room + faqs in between
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue
* affirm
	- book_room_form
	- form{"name": null}

## book_room + faqs in between
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue
* deny
	- action_deactivate_form
	- form{"name": null}
	- utter_happy

## book_room + faqs in between
* greet
  - utter_greet
* book_room
	- book_room_form
	- form{"name": "book_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue
* affirm
	- book_room_form
	- form{"name": null}	
	
## clean_room1
* greet
	- utter_greet
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
	- form{"name": null}
* thank_you
  - utter_welcome
  - utter_happy
  
## clean_room2
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
	- form{"name": null}
* thank_you
  - utter_welcome
  - utter_happy

## clean_room3
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
	- form{"name": null}

## clean_room + faqs 
* greet
  - utter_greet
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
	- form{"name": null}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
  - action_faqs
  
## clean_room + faqs in between
* greet
  - utter_greet
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue2
* affirm
	- clean_room_form
	- form{"name": null}

## clean_room + faqs in between
* greet
  - utter_greet
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue2
* deny
	- action_deactivate_form
	- form{"name": null}
	- utter_happy

## clean_room + faqs in between
* greet
  - utter_greet
* clean_room
	- clean_room_form
	- form{"name": "clean_room_form"}
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue2
* FAQ_Check_in OR FAQ_Check_out OR FAQ_cancel_reservation OR FAQ_cancellation_policy OR FAQ_restaurant OR FAQ_breakfast_availability OR FAQ_breakfast_timings OR FAQ_restaurant_timings
	- action_faqs
	- utter_ask_continue2
* affirm
	- clean_room_form
	- form{"name": null}