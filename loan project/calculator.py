class TicketBookingChatbot:
    def __init__(self):
        self.user_name = None
        self.ticket_type = None
        self.num_tickets = None
        self.booking_date = None
        self.confirmation_number = None

    def greet_user(self):
        print("Hi! Welcome to TicketBookingBot.")
        self.user_name = input("What's your name? ")

    def get_ticket_details(self):
        print(f"Nice to meet you, {self.user_name}!")
        self.ticket_type = input("What type of ticket would you like to book? ")
        self.num_tickets = int(input("How many tickets do you need? "))
        self.booking_date = input("When would you like to book the tickets? ")

    def confirm_booking(self):
        print("Great! Let me confirm your booking:")
        print(f"Ticket Type: {self.ticket_type}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Booking Date: {self.booking_date}")

        confirm = input("Is everything correct? (yes/no) ").lower()
        if confirm == "yes":
            self.confirmation_number = "ABC123"  # Generate a confirmation number
            print(f"Your booking is confirmed! Confirmation Number: {self.confirmation_number}")
        else:
            print("Booking canceled. Please try again.")

    def run(self):
        self.greet_user()
        self.get_ticket_details()
        self.confirm_booking()


if __name__ == "__main__":
    booking_bot = TicketBookingChatbot()
    booking_bot.run()
