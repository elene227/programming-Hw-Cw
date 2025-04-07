def number(bus_stops):
    people_on_bus = 0
    for on, off in bus_stops:
        people_on_bus += on - off
    return people_on_bus