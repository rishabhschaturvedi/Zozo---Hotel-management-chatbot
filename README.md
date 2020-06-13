# Zozo: Hotel management chatbot
This is a hotel management chatbot built on rasa framework. It is capable of responding to and handling the following basic functionalities
- Book room
- Request Room Cleaning
- Handle FAQs
- Handle Greetings

Example flows for these functionalities are described in detail in the Flows section.

# Flows

Please note that the flows below are only meant as examples to demonstrate functionalities. The chatbot is capable of handling questions having the same meaning but posed in different ways.

For eg. in our Book Room example, we have the user say "I want to book a room". In this case, the bot is able to direct the user to this flow if he says something along the lines of "I would like to book a room", "I want to book a room for my stay" etc.

## Book Room

User: I want to book a room.

Bot: How many rooms would you like to book?

User: 2 rooms

Bot: What type of room would you want to book?
- Button1 - Simple 
- Button 2 - Deluxe

User: (Clicks on Button 1)

Bot: You have chosen to book 2 simple rooms

## Clean room

User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone at 5 pm?

Bot: Sure, I have scheduled a cleaning for 2020-06-13T17:00:00.000-07:00.

The above two flows are the only multi-step flows. The flows adapt themselves according to the user input. For eg., if the user says "I want to book a room for 2 people", the bot responds:
" What type of room would you want to book?
- Button1 - Simple 
- Button 2 - Deluxe".

## FAQs

### Check-in timings -
User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

### Check-out timings -
User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

### Cancel Reservation -
User: How do I cancel a reservation?

Bot: To cancel a reservation, select the “Reservations” link from the homepage.

Bot: On the Reservations page, under the heading ‘View, Change or Cancel a Reservation,’ enter your confirmation number, and either the last name on the reservation or the last four digits of the credit card used to make the reservation.

### Cancellation Policy -
User: What is your cancellation policy?

Bot: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

### Restaurant -
User: Does the hotel have a restaurant?

Bot: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

### Breakfast Availability -
User: Does the hotel offer breakfast?

Bot: The hotel provides its guests with a free made-to-order breakfast each morning.

### Breakfast timings -
User: What are the breakfast timings?

Bot: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

### Restaurant timings -
User: What are the timings of your restaurant?

Bot: Our restaurant serves a dazzling 24-hour menu.

