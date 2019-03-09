python-patterns
===============

A collection of design patterns and idioms in Python.

Current Patterns
----------------

__Creational Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](patterns/creational/abstract_factory.py) | use a generic function with specific factories |
| [borg](patterns/creational/borg.py) | a singleton with shared-state among instances |
| [builder](patterns/creational/builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](patterns/creational/factory_method.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [pool](patterns/creational/pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](patterns/creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |

__Structural Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](patterns/structural/adapter.py) | adapt one interface to another using a white-list |
| [bridge](patterns/structural/bridge.py) | a client-provider middleman to soften interface changes |
| [composite](patterns/structural/composite.py) | lets clients treat individual objects and compositions uniformly |
| [decorator](patterns/structural/decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](patterns/structural/facade.py) | use one class as an API to a number of others |
| [flyweight](patterns/structural/flyweight__py3.py) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](patterns/structural/front_controller.py) | single handler requests coming to the application |
| [mvc](patterns/structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](patterns/structural/proxy.py) | an object funnels operations to something else |

__Behavioral Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility__py3.py) | apply a chain of successive handlers to try and process the data |
| [catalog](patterns/behavioral/catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](patterns/behavioral/chaining_method.py) | continue callback next object method |
| [command](patterns/behavioral/command.py) | bundle a command and arguments to call later |
| [iterator](patterns/behavioral/iterator.py) | traverse a container and access the container's elements |
| [mediator](patterns/behavioral/mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](patterns/behavioral/memento.py) | generate an opaque token that can be used to go back to a previous state |
| [observer](patterns/behavioral/observer.py) | provide a callback for notification of events/changes to data |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](patterns/behavioral/registry__py3.py) | keep track of all subclasses of a given class |
| [specification](patterns/behavioral/specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](patterns/behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](patterns/behavioral/strategy.py) | selectable operations over the same data |
| [template](patterns/behavioral/template.py) | an object imposes a structure but takes pluggable components |
| [visitor](patterns/behavioral/visitor.py) | invoke a callback for all items of a collection |

__Design for Testability Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [dependency_injection](patterns/dependency_injection.py) | 3 variants of dependency injection |

__Fundamental Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [delegation_pattern](patterns/fundamental/delegation_pattern.py) | an object handles a request by delegating to a second object (the delegate) |

__Others__:

| Pattern | Description |
|:-------:| ----------- |
| [blackboard](patterns/other/blackboard__py3.py) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern |
| [graph_search](patterns/other/graph_search.py) | graphing algorithms - non gang of four pattern |
| [hsm](patterns/other/hsm/hsm.py) | hierarchical state machine - non gang of four pattern |


Videos
------
[Design Patterns in Python by Peter Ullrich](https://www.youtube.com/watch?v=bsyjSW46TDg)

[Sebastian Buczyński - Why you don't need design patterns in Python?](https://www.youtube.com/watch?v=G5OeYHCJuv0)

[You Don't Need That!](https://www.youtube.com/watch?v=imW-trt0i9I)

[Pluggable Libs Through Design Patterns](https://www.youtube.com/watch?v=PfgEU3W0kyU)


Contributing
------------
When an implementation is added or modified, please review the following guidelines:

##### Output
All files with example patterns have `### OUTPUT ###` section at the bottom 
(migration to OUTPUT = """...""" is in progress).

Run `append_output.sh` (e.g. `./append_output.sh borg.py`) to generate/update it.

##### Docstrings
Add module level description in form of a docstring with links to corresponding references or other useful information.

Add "Examples in Python ecosystem" section if you know some. It shows how patterns could be applied to real-world problems.

[facade.py](patterns/structural/facade.py) has a good example of detailed description,
but sometimes the shorter one as in [template.py](patterns/behavioral/template.py) would suffice.

In some cases class-level docstring with doctest would also help (see [adapter.py](patterns/structural/adapter.py))
but readable OUTPUT section is much better.


##### Python2/3 compatibility
Try to keep it (discussion is held in [issue #208](https://github.com/faif/python-patterns/issues/208))
- use new style classes (inherit from `object`)
- use `from __future__ import print_function`

##### Update README
When everything else is done - update corresponding part of README.


##### Travis CI
Please run `flake8` and `pytest` commands locally to be sure your changes will pass CI .
