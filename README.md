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
| [abstract_factory](creational/abstract_factory.py) | use a generic function with specific factories |
| [borg](creational/borg.py) | a singleton with shared-state among instances |
| [builder](creational/builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](creational/factory_method.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation](creational/lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [pool](creational/pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__Structural Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](structural/3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](structural/adapter.py) | adapt one interface to another using a white-list |
| [bridge](structural/bridge.py) | a client-provider middleman to soften interface changes |
| [composite](structural/composite.py) | encapsulate and provide access to a number of different objects |
| [decorator](structural/decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](structural/facade.py) | use one class as an API to a number of others |
| [flyweight](structural/flyweight.py) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](structural/front_controller.py) | single handler requests coming to the application |
| [mvc](structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](structural/proxy.py) | an object funnels operations to something else |

__Behavioral Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [chain](behavioral/chain.py) | apply a chain of successive handlers to try and process the data |
| [catalog](behavioral/catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](behavioral/chaining_method.py) | continue callback next object method |
| [command](behavioral/command.py) | bundle a command and arguments to call later |
| [iterator](behavioral/iterator.py) | traverse a container and access the container's elements |
| [mediator](behavioral/mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](behavioral/memento.py) | generate an opaque token that can be used to go back to a previous state |
| [observer](behavioral/observer.py) | provide a callback for notification of events/changes to data |
| [publish_subscribe](behavioral/publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](behavioral/registry.py) | keep track of all subclasses of a given class |
| [specification](behavioral/specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](behavioral/strategy.py) | selectable operations over the same data |
| [template](behavioral/template.py) | an object imposes a structure but takes pluggable components |
| [visitor](behavioral/visitor.py) | invoke a callback for all items of a collection |

__Design for Testability Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [setter_injection](dft/setter_injection.py) | the client provides the depended-on object to the SUT via the setter injection (implementation variant of dependency injection) |

__Fundamental Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [delegation_pattern](fundamental/delegation_pattern.py) | an object handles a request by delegating to a second object (the delegate) |

__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [blackboard](other/blackboard.py) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](other/graph_search.py) | graphing algorithms - non gang of four pattern |
| [hsm](other/hsm/hsm.py) | hierarchical state machine - non gang of four pattern |
