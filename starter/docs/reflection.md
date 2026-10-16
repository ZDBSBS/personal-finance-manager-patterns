# Design Pattern Reflection

## Singleton

The Singleton pattern was selected for the `Balance` class because the application requires a single, shared representation of the current financial state. All transactions, observers, and commands operate on the same balance instance, ensuring consistency across the application.

A key benefit of this approach is the existence of a single source of truth for balance information. A trade-off is that shared state must be carefully managed during testing because state changes can affect subsequent test cases. This was addressed by resetting the balance between tests.

## Adapter

The Adapter pattern was used to integrate external transaction data without modifying the internal transaction model. External payment providers may expose transaction information in formats that differ from the application's domain model. The adapter converts these external representations into standard `Transaction` objects used by the application.

This approach improves flexibility and allows additional external transaction sources to be supported with minimal impact on existing code. The trade-off is the need to create and maintain adapter implementations for each incompatible external format.

## Observer

The Observer pattern was chosen to handle notifications related to balance changes. Whenever the balance changes, registered observers are notified automatically. This enables features such as balance reporting and low-balance alerts without embedding notification logic directly into the balance implementation.

The main advantage is loose coupling between the balance component and notification behaviors. New observers can be added without modifying the balance class itself. The trade-off is the added complexity of managing observer registration and notification workflows.

## Command

The Command pattern was selected to represent financial operations as independent command objects. Each command encapsulates a balance operation and supports execution, undo, and redo functionality. This keeps transaction processing separate from history management and provides a structured mechanism for tracking user actions.

The primary benefit is support for reversible operations while maintaining a clear and extensible design. The trade-off is the introduction of additional classes and the requirement that each command defines both execution and reversal logic.

Together, the Singleton, Adapter, Observer, and Command patterns address different architectural concerns while maintaining clear separation of responsibilities, flexibility, and maintainability.

## Challenges and Trade-offs

One of the primary design goals was achieving modularity while maintaining simplicity. Dependency injection was used to reduce coupling between components and improve testability. Dependencies such as observers and commands are supplied externally rather than being created internally, making components easier to replace, extend, and test in isolation.

Another challenge involved testing a Singleton-based architecture. Because the balance instance is shared throughout the application, test cases require explicit state management to ensure independence and repeatability.

Overall, the combination of Singleton, Adapter, Observer, and Command patterns resulted in a modular, maintainable, and testable architecture. The design supports future extensions, such as additional transaction sources, notification mechanisms, or financial operations, while preserving clear separation of responsibilities.