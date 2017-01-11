python-patterns(파이썬-패턴)
===============

A collection of design patterns and idioms in Python.
(파이썬 문법으로 구현된 디자인패턴의 모음)

When an implementation is added or modified, be sure to update this file and
rerun `append_output.sh` (eg. ./append_output.sh borg.py) to keep the output
comments at the bottom up to date(변경사항에 대해 추가하거나 수정할때, 파일을 업데이트하고 최신 코멘트를 출력하기 위해 `append_output.sh` (eg. ./append_output.sh borg.py)를 재실행 해야한다).

Current Patterns():

__Creational Patterns(생성 패턴)__:

| Pattern(패턴) | Description(설명) |
|:-------:| ----------- |
| [abstract_factory](abstract_factory.py) | use a generic function with specific factories(일반적인 기능과 특정 팩토리를 사용하는 패턴) |
| [borg](borg.py) | a singleton with shared-state among instances(인스턴스 사이의 상태를 공유하는 싱글턴 패턴) |
| [builder](builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects(여러 생성자를 사용하는 대신에 빌더오브젝트가 파라미터를 수신하고 구성된 오브젝트를 반환시키는 패턴) |
| [factory_method](factory_method.py) | delegate a specialized function/method to create instances(인스턴스를 만드는 특정한 함수/메서드를 대신하는 패턴) |
| [lazy_evaluation](lazy_evaluation.py) | lazily-evaluated property pattern in Python(파이썬에서 지연 연산된 속성패턴) |
| [pool](pool.py) | preinstantiate and maintain a group of instances of the same type(동일한 유형의 인스턴스 그룹을 미리생성하고 유지하는 패턴) |
| [prototype](prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive(새로운 인스턴스에 대한 프로토타입의 클론과 팩토리를 사용하는 패턴(인스턴스화 비용이 비싼경우)) |

__Structural Patterns(구조화 패턴)__:

| Pattern(패턴) | Description(설명) |
|:-------:| ----------- |
| [3-tier](3-tier.py) | data<->business logic<->presentation separation (strict relationships)(데이터<>비즈니스 로직<>프리젠테이션 분리 (엄격한 관계)) |
| [adapter](adapter.py) | adapt one interface to another using a white-list(white-list를 사용하여 다른 하나의 인터페이스에 맞추는 패턴) |
| [bridge](bridge.py) | a client-provider middleman to soften interface changes(사용자와 공급자 사이를 이어주는 패턴으로 인터페이스 전환을 부드럽게 해준다) |
| [composite](composite.py) | encapsulate and provide access to a number of different objects(다수의 각기다른 오브젝트들에게 엑세스를 제공하고 캡슐화해주는 패턴) |
| [decorator](decorator.py) | wrap functionality with other functionality in order to affect outputs(출력에 영향을 주기위해 다른 기능들을 묶어주는 패턴) |
| [facade](facade.py) | use one class as an API to a number of others(다수의 다른 API를 하나의 클래스처럼 사용하는 패턴) |
| [flyweight](flyweight.py) | transparently reuse existing instances of objects with similar/identical state(유사한/동일한 상태의 오브젝트와 이미 있는 인스턴스를 간단하게 재사용 하는 패턴) |
| [front_controller](front_controller.py) | single handler requests coming to the application(응용프로그램이 받는 요구를 관리하는 한개의 핸들러 패턴) |
| [mvc](mvc.py) | model<->view<->controller (non-strict relationships)(모델<>뷰<>컨트롤러(느슨한 관계)) |
| [proxy](proxy.py) | an object funnels operations to something else(다른객체 간의 객체이동을 관리하는것을 대신하는 패턴) |

__Behavioral Patterns(행위 패턴)__:

| Pattern(패턴) | Description(설명) |
|:-------:| ----------- |
| [chain](chain.py) | apply a chain of successive handlers to try and process the data(연속된 핸들러를 시도하고 데이터를 처리할 체인을 적용해주는 패턴) |
| [catalog](catalog.py) | general methods will call different specialized methods based on construction parameter(구성 매개변수에 기반하여 특정한 다른메서드를 호출하는데 쓰이는 일반적인 메서드패턴) |
| [chaining_method](chaining_method.py) | continue callback next object method(다음 객체메서드를 계속해서 호출하는 패턴) |
| [command](command.py) | bundle a command and arguments to call later(호출한뒤 쓰이는 명령과 독립변수의 묶음) |
| [mediator](mediator.py) | an object that knows how to connect other objects and act as a proxy(프록시와 다른객체간의 역할을 이어주는 방법을 알고있는 객체패턴) |
| [memento](memento.py) | generate an opaque token that can be used to go back to a previous state(예전 상태로 되돌릴 수 있는 불투명한 토큰을 생성하는 패턴) |
| [observer](observer.py) | provide a callback for notification of events/changes to data(데이터가 발생/변경을 통지하는걸 호출해주는 패턴) |
| [publish_subscribe](publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners(이벤트/데이터를 등록된 리스너들에게 전송하는 소스 신디케이트) |
| [registry](registry.py) | keep track of all subclasses of a given class(지정된 클래스의 모든 서브클래스를 찾아내는 패턴) |
| [specification](specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic(부울논리를 함께 사용하는 비즈니스규칙체인으로 재결합된 패턴) |
| [state](state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to(잠재적 상태와 다음 상태로 전환 가능한 이진수로 구성되어있는 논리패턴) |
| [strategy](strategy.py) | selectable operations over the same data(동일한 데이터에 대한 조작을 선택할수있는 패턴) |
| [template](template.py) | an object imposes a structure but takes pluggable components(접속할 수 있는 구성요소가 필요한 객체패턴) |
| [visitor](visitor.py) | invoke a callback for all items of a collection(콜렉션의 모든 항목에 대한 회신을 호출하는 패턴) |


__Others(기타)__:

| Pattern(패턴) | Description(설명) |
|:-------:| ----------- |
| [graph_search](graph_search.py) | (graphing algorithms, not design patterns)(디자인 패턴이 아닌 그래프 알고리즘) |
