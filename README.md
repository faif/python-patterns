python-patterns
===============

A collection of design patterns and idioms in Python.

When an implementation is added or modified, be sure to update this file and
rerun `append_output.sh` (eg. ./append_output.sh borg.py) to keep the output
comments at the bottom up to date.

Current Patterns:

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [abstract_factory](abstract_factory.py) | use a generic function with specific factories |
| [adapter](adapter.py) | adapt one interface to another using a whitelist |
| [borg](borg.py) | a singleton with shared-state among instances |
| [bridge](bridge.py) | a client-provider middleman to soften interface changes |
| [builder](builder.py) | call many little discrete methods rather than having a huge number of constructor parameters |
| [catalog](catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chain](chain.py) | apply a chain of successive handlers to try and process the data |
| [chaining_method](chaining_method.py) | continue callback next object method |
| [command](command.py) | bundle a command and arguments to call later |
| [composite](composite.py) | encapsulate and provide access to a number of different objects |
| [decorator](decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](facade.py) | use one class as an API to a number of others |
| [factory_method](factory_method.py) | delegate a specialized function/method to create instances |
| [front_controller](front_controller.py) | single handler requests coming to the application |
| [flyweight](flyweight.py) | transparently reuse existing instances of objects with similar/identical state |
| [graph_search](graph_search.py) | (graphing algorithms, not design patterns) |
| [lazy_evaluation](lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [mediator](mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](memento.py) | generate an opaque token that can be used to go back to a previous state |
| [mvc](mvc.py) | model<->view<->controller (non-strict relationships) |
| [observer](observer.py) | provide a callback for notification of events/changes to data |
| [pool](pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |
| [proxy](proxy.py) | an object funnels operations to something else |
| [publish_subscribe](publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](registry.py) | keeping track of all subclasses of a given class |
| [specification](specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](state.py) | logic is org'd into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](strategy.py) | selectable operations over the same data |
| [template](template.py) | an object imposes a structure but takes pluggable components |
| [visitor](visitor.py) | invoke a callback for all items of a collection |
