# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint, choice

class Train:

    def ticket(self, train_no, this_station, that_station):
        ticket_no = randint(555, 999999)
        print(f"Your Ticket no. {ticket_no} in train {train_no} from {this_station} to {that_station}")

    def get_status(self):
        status = choice([True, False])
        if status:
            print("Your Ticket is confirmed")
        else:
            print("Your Ticket isn't confirmed yet")

    def fare(self, train_no, this_station, that_station):
        fare = randint(200, 2000)
        print(f"Ticket fare in train {train_no} from {this_station} to {that_station} is ₹{fare}")


# Using the class
t = Train()

t.ticket(12345, "Delhi", "Mumbai")
t.get_status()
t.fare(12345, "Delhi", "Mumbai")