# Strategy Pattern

The Strategy Pattern is a design pattern that allows an object to change its behavior at runtime by switching between different algorithms or strategies. This pattern is often used in situations where a class has a single method that needs to be implemented in multiple ways.

In a fantasy RPG game, the Strategy Pattern can be used to model the behavior of different characters, such as warriors, mages, and archers. Each character class has a unique set of abilities and attack patterns, but they all share a common interface for performing actions.

The Strategy Pattern can be implemented in Python by defining an interface or abstract class that defines the method(s) that the strategies must implement. For example, in our RPG game, we could define an interface called "Character" that has a method called "attack".
