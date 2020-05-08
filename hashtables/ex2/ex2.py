
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    route = [None] * length
    ht = {}
    source = "NONE"
    
    for ticket in tickets:
        
        ht[ticket.source] = ticket.destination
        
    for i in range(length):
        
        route[i] = ht[source]
        source = ht[source]

    return route
