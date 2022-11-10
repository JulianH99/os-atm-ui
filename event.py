from typing import Dict, Callable, List, Any


EVENT_NEW_CUSTOMER = 'new_customer'

EVENT_UPDATE_LIST = 'update_list'


class EventEmitter:
    events: Dict[str, List[Callable]] = {}

    @classmethod
    def emit(cls, event_name: str, data: Any):
        if event_name in cls.events.keys():
            for handler in cls.events[event_name]:
                handler(data)

    @classmethod
    def subscribe(cls, event_name: str, callable: Callable):
        if event_name in cls.events.keys():
            if not cls.events[event_name]:
                cls.events[event_name] = [callable]
            else:
                cls.events[event_name].append(callable)
        else:
            cls.events[event_name] = [callable]