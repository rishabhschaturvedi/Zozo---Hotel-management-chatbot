# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Dict, Text, Any, List, Union, Optional
import logging
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, EventType
from parsing import (
    parse_duckling_time_as_interval,
    parse_duckling_time,
    get_entity_details,
)

logger = logging.getLogger(__name__)

class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")

        if intent in [
            "FAQ_Check_in",
            "FAQ_Check_out",
            "FAQ_cancel_reservation",
            "FAQ_cancellation_policy",
            "FAQ_restaurant",
            "FAQ_breakfast_availability",
            "FAQ_breakfast_timings",
            "FAQ_restaurant_timings",
        ]:
            dispatcher.utter_message(template = f"utter_"+ intent)
        return []
        
class Book_a_room(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "book_room_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["no_of_rooms", "type_of_rooms"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "no_of_rooms": [
                self.from_entity(entity="number", intent=["book_room","inform"]),
            ],
            "type_of_rooms": self.from_entity(entity="type_of_rooms"),
        }
    

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    

    def validate_no_of_rooms(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> Dict[Text, Any]:

        if self.is_int(value) and int(value) > 0:
            return {"no_of_rooms": value}
        else:
            dispatcher.utter_message(template="utter_wrong_no_of_rooms")
            # validation failed, set slot to None
            return {"no_of_rooms": None}
            
            
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # utter submit template
        if not tracker.get_slot("no_of_rooms"):
            dispatcher.utter_message(template="utter_ask_continue")
        if not tracker.get_slot("type_of_rooms"):
            dispatcher.utter_message(template="utter_ask_continue")
        if tracker.get_slot("no_of_rooms") and tracker.get_slot("type_of_rooms"):
            dispatcher.utter_message(template="utter_book_room")
        return [
                SlotSet("no_of_rooms", None),
                SlotSet("type_of_rooms", None),
        ]
        
class Clean_room(FormAction):
    """Pay credit card form..."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "clean_room_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["time"]

    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "time": [
                self.from_entity(entity="time"),
            ],
        }

    def validate_time(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate time value."""

        timeentity = get_entity_details(tracker, "time")
        parsedtime = parse_duckling_time(timeentity)
        if not parsedtime:
            dispatcher.utter_message(template="utter_not_a_valid_time")
            return {"time": None}
        return parsedtime
        
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        if not tracker.get_slot("time"):
            dispatcher.utter_message(template="utter_ask_continue2")
        else:
            dispatcher.utter_message(template="utter_room_clean")
        
        return [
                SlotSet("time", None),
                SlotSet("grain", None),
        ]