# Step 9: Explain your design in the STUDENT_README.md

Include setup, run, and test commands, example input/output, a link to your successful Actions run, and any coverage exclusions. Then write one or two plain sentences for each idea below, pointing to your own class or method. Short, accurate explanations are enough.

OOP ideas

| Idea | Simple meaning |
| --- | --- |
| Encapsulation | Keep related data and behavior together. Explain how the calculation holds its values and how history protects its list. |
| Abstraction | Show the promise a class makes. Calculation requires execute(). |
| Inheritance | A child class reuses shared behavior. ArithmeticCalculation inherits create(). |
| Polymorphism | Use the same method call with different implementations. Explain how commands can accept a Calculation implementation that follows the execute() contract. |
| Composition | Build an object from other pieces. A command holds a calculation; a calculation holds an operation. |

SOLID ideas

| Principle | Simple meaning |
| --- | --- |
| Single responsibility | Each part has one main job. |
| Open/closed | Add an operation without changing calculation or command execution. Register the new name in the CLI dictionary. |
| Liskov substitution | A replacement calculation must keep the same promise: return a numeric answer or raise an appropriate error. |
| Interface segregation | Keep the required interface small. Calculations need execute(), not many unrelated methods. |
| Dependency inversion | Give a command a Calculation abstraction and give a calculation an operation. Avoid hard-coding addition inside them. |

Also explain static, class, and instance methods, and identify your Factory, Command, and Strategy. Add subtraction, multiplication, and division after the addition example and explain why calculation execution does not need to change. You do not need extra classes just to mention every principle.
Next: [What to submit](11-what-to-submit.md)

---

[Back to the contents](../README.md) · [Start with forking](00-fork-and-submit.md)
