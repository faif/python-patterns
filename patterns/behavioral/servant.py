"""
Implementation of the Servant design pattern.

The Servant design pattern is a behavioral pattern used to offer functionality
to a group of classes without requiring them to inherit from a base class.

This pattern involves creating a Servant class that provides certain services
or functionalities. These services are used by other classes which do not need
to be related through a common parent class. It is particularly useful in
scenarios where adding the desired functionality through inheritance is impractical
or would lead to a rigid class hierarchy.

This pattern is characterized by the following:

- A Servant class that provides specific services or actions.
- Client classes that need these services, but do not derive from the Servant class.
- The use of the Servant class by the client classes to perform actions on their behalf.

References:
- https://en.wikipedia.org/wiki/Servant_(design_pattern)
"""
