python-patterns
===============

A collection of design patterns and idioms in Python.

When an implementation is added or modified, be sure to update this file and
rerun `append_output.sh` (eg. ./append_output.sh borg.py) to keep the output
comments at the bottom up to date.

Current Patterns:

__Creational Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](abstract_factory.py) | use a generic function with specific factories |
| [borg](borg.py) | a singleton with shared-state among instances |
| [builder](builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](factory_method.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation](lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [pool](pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__Structural Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](adapter.py) | adapt one interface to another using a white-list |
| [bridge](bridge.py) | a client-provider middleman to soften interface changes |
| [composite](composite.py) | encapsulate and provide access to a number of different objects |
| [decorator](decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](facade.py) | use one class as an API to a number of others |
| [flyweight](flyweight.py) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](front_controller.py) | single handler requests coming to the application |
| [mvc](mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](proxy.py) | an object funnels operations to something else |

__Behavioral Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [chain](chain.py) | apply a chain of successive handlers to try and process the data |
| [catalog](catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](chaining_method.py) | continue callback next object method |
| [command](command.py) | bundle a command and arguments to call later |
| [mediator](mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](memento.py) | generate an opaque token that can be used to go back to a previous state |
| [observer](observer.py) | provide a callback for notification of events/changes to data |
| [publish_subscribe](publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](registry.py) | keep track of all subclasses of a given class |
| [specification](specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](strategy.py) | selectable operations over the same data |
| [template](template.py) | an object imposes a structure but takes pluggable components |
| [visitor](visitor.py) | invoke a callback for all items of a collection |


__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [graph_search](graph_search.py) | (graphing algorithms, not design patterns) |
