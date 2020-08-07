#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    #FirstFlight : Source = None
    #LastFlight : Destination = None

    cache = {}
    route = []
    # first_ticket = None
    # last_ticket = None

    for i in tickets:
        cache[i.source] = i.destination

    destination = cache["NONE"]
    for j in range(len(tickets)):
        route.append(destination)
        destination = cache[destination]
    


    # route.append(last_ticket)

    return route



tickets = [
    Ticket("PIT", "ORD" ),
    Ticket( "XNA", "CID" ),
    Ticket( "SFO", "BHM" ),
    Ticket( "FLG", "XNA" ),
    Ticket( "NONE", "LAX" ),
    Ticket( "LAX", "SFO" ),
    Ticket( "CID", "SLC" ),
    Ticket( "ORD", "NONE" ),
    Ticket( "SLC", "PIT" ),
    Ticket( "BHM", "FLG" )
]

# {
#     "PIT": "ORD",
#     "XNA": "CID",
#     "SFO": "BHM",
#     "FLG": "XNA"
# }
print(reconstruct_trip(tickets, len(tickets)))