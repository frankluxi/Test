from Event.Event import Event, EventType

event1 = Event()
event1.setEventType(EventType.GOLDEN_FORK)
event1.setEventIndex(0)

event2 = Event()
event2.setEventType(EventType.NEW_HIGH_DIF)
event2.setEventIndex(0)

print(event1 == event2)

