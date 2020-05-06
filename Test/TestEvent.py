from Event.Event import Event, EventType
lst = []

event1 = Event()
event1.setEventType(EventType.NEW_HIGH_DIF)
event1.setEventIndex(0)

lst.append(event1)
print(lst)
event2 = Event()
event2.setEventType(EventType.NEW_HIGH_DIF)
event2.setEventIndex(2)
lst.append(event2)

print(lst[len(lst)-1].getEventIndex())

print(event1 == event2)

