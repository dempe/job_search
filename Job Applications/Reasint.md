---
type: job
applied: 
interviews: 
  - 2023-11-17 10:00
  - 2023-11-29 14:00
  - 2023-11-29 15:00
  - 2023-11-29 15:30
status: rejected
source: reference
job_type: fulltime
position: "Senior Software Engineer Platform"
remote: hybrid
4day: false
industry: healthcare
website: 
location: "Kansas City, MO"
company_size: medium
recruited: false
referred: true
listing: https://reasint.prismhr-hire.com/job/373803/senior-software-engineer-platform
blog: 
correspondence:
title: Reasint
date_created: "2023-11-17 08:16"
date_modified: "2025-05-31 13:30"
---

## Application

I was referred by a friend of Sophie's.

## Interview 1

Reasint is a medical imaging tech company.

They mention they need someone to work with Java and JS. They are using React. The guy has seen my LI profile, so I'm pretty sure he must know that I'm not a FE guy. I'd be fine learning and dipping my toes in the water, though.

I also have not worked with a graph DB. I've worked with relational DBs (obviously), document DBs (ES), columnar DBs (Cassandra and HBase), and briefly key/value stores (Redis). Working with a graph DB would great to add to my resume and would something I would love to learn, though!

**Questions to ask**:

- What are you using neo4j for? What problems does it solve that a relational or document-based DB can't solve?

### Retro

**Cons**

- I hadn't talked to anyone on the phone recently, so was still I bit nervous. I hope it didn't show through too much.
- I need to work on my "pitch". It feels sloppy, haphazard, *unnatural*, like I'm reading from a script.

**Pros**

- Asked good questions about tech
- Didn't give too much info as has been a problem in the past (see Ninjacat)
- Sent resume soon after as I had mentioned

Overall, it went really well I think. He wants a follow-up interview after Thanksgiving. It will be a single, two hour interview.

## Interview 2

**Preparation**

Need to ask Cameron what the interview will exactly consist of. Or maybe I could just wait until he schedules it. If he doesn't schedule it by next Monday (after Thanksgiving), then I will send a follow-up message. I think it's at least better to get the interview scheduled before asking what will be on it. Asking about the format, content, etc. Is a natural follow-up question after being scheduled.

The question then becomes — what should I assume will be on the interview? What should I study?

- Self introduction for one. Make it sound more natural. Less filler and more important details.
- Review Kafka as they use it heavily
- System design
- Maybe work through one or two algorithm problems. Not that I think they will be on the interview, but because they are a good programming warm up.

**Update**

Cameron just replied to me saying that the technical portion will not have any live coding sessions but consist of a series of questions probing my knowledge of Java and OOP.

In that case,

- work through a few algorithm problems in Java each day just to get warmed back up.
- Study Java's new features, hopefully trying them out yourself
- Study Kafka
- Study the Quastor Archives
- Write out your "story" for each of your jobs so that you explain what you did and what you learned
- Do a few practice interviews. Ask Sophie's opinion.
- make sure you're familiar with everything they mention in the job description

### Preparation

#### Questions to Ask

- What are your data sources? How does data make it into the system?
- Where do you get new customers? (the website seemed a bit bare)
- Will I need to visit the office occasionally? If so, how often and where can I stay?
- How are the teams structured?
- Oncall?
- What are your expectations of me?

#### Java

#### Object -Oriented Programming (OOP) Concepts

Java is fundamentally an object-oriented language. Key concepts include classes and objects, inheritance, encapsulation, polymorphism, and abstraction.

 - **Classes and Objects**: Understand that a class is a blueprint for objects, and objects are instances of a class.
 - **Class Members**: Know about class variables (static variables), instance variables (non-static variables), methods, and constructors.
 - **Inheritance**: Grasp how one class can inherit fields and methods from another using extends keyword.
 - **Polymorphism**: Understand polymorphism (method overloading and overriding) and how it allows objects to be treated as instances of their parent class.
 - **Encapsulation**: Learn how to encapsulate data (variables) and code (methods) together into a single unit, typically by using private fields and public getters/setters.
 - **Abstraction**: Understand abstraction, creating simple models representing more complex underlying code and data, often using abstract classes and interfaces.
 - **Interfaces**: Learn how interfaces define methods that a class must implement unless the class is abstract.
 - **Abstract Classes**: Understand the role of abstract classes, which cannot be instantiated and are used to declare common characteristics of subclasses.
 - **Method Overloading**: Know how method overloading works by having multiple methods with the same name but different parameters.
 - **Method Overriding**: Understand method overriding, where a subclass provides a specific implementation of a method declared in its parent class.
 - **Constructors**: Familiarize yourself with constructors, their role in initializing objects, and how they can be overloaded.
 - **'this' Keyword:** Understand the use of this keyword to refer to the current object within an instance method or a constructor.
 - **'super' Keyword**: Know how super keyword is used to refer to parent class objects, methods, and constructors.
 - **Static Keyword**: Grasp the concept of static variables and methods and how they belong to the class, not to individual objects.
 - **Final Keyword**: Understand the use of the final keyword for declaring constants, preventing method overriding, and preventing inheritance.
 - **Access Modifiers**: Familiarize yourself with access modifiers like private, protected, public, and default, and how they control access levels.
 - **Object Cloning**: Understand object cloning in Java, using the `clone()` method of the Object class.
 - **Instanceof Operator**: Know how to use `instanceof` to check whether an object is an instance of a specific class or interface.
 - **Composition**: Understand the concept of composition as an alternative to inheritance, where one class includes another.
 - **Coupling and Cohesion**: Be aware of the principles of coupling (the degree of interdependence between classes) and cohesion (the degree to which elements of a class belong together).

#### Syntax

Being comfortable with Java syntax is crucial.

1. **Data Types**: Understand primitive (int, double, boolean, etc.) and reference data types (Objects, Arrays, Strings).
2. **Variables**: Learn about declaration, initialization, and scope.
3. **Operators**: Familiarize with arithmetic, relational, logical, assignment, and bitwise operators.
	1. **Arithmetic Operators**: Used for basic mathematical operations.

	   - `+` - Addition
	   - `-` - Subtraction
	   - `*` - Multiplication
	   - `/` - Division
	   - `%` - Modulus (remainder)

	2. **Relational Operators**: Used to compare values.

	   - `==` - Equal to
	   - `!=` - Not equal to
	   - `>` - Greater than
	   - `<` - Less than
	   - `>=` - Greater than or equal to
	   - `<=` - Less than or equal to

	3. **Logical Operators**: Used for boolean logic.

	   - `&&` - Logical AND
	   - `||` - Logical OR
	   - `!` - Logical NOT

	4. **Assignment Operators**: Used to assign values to variables.

	   - `=` - Simple assignment
	   - `+=` - Add and assign
	   - `-=` - Subtract and assign
	   - `*=` - Multiply and assign
	   - `/=` - Divide and assign
	   - `%=` - Modulus and assign

	5. **Bitwise Operators**: Operate on individual bits of integer types.

	   - `&` - Bitwise AND
	   - `|` - Bitwise OR
	   - `^` - Bitwise XOR
	   - `~` - Bitwise Complement
	   - `<<` - Left Shift
	   - `>>` - Right Shift
	   - `>>>` - Unsigned Right Shift

4. **Control Flow Statements**: Mastery of if, else, switch, for, while, do-while, break, and continue.
	1. `if`
	2. `else if`
	3. `else`
	4. `switch`
	5. `for`
	6. `while`
	7. `do-while`
	8. `break`
	9. `continue`
	10. `return`
5. **Arrays**: Usage of single and multi-dimensional arrays, including iteration.
6. **Strings**: Knowledge of String class methods, StringBuilder, and StringBuffer.

	- The two mutable alternatives to `String`
	- `StringBuffer` is synchronized (thread safe)
	- `StringBuidler` is the faster but unsynchronized alternative (and should be preferred in most cases)

7. **Methods**: Understand method definition, arguments, return types, and overloading.
8. **Classes and Objects**: Grasp the structure of classes and object instantiation.
9. **Inheritance**: Concepts of superclass, subclass, and use of 'extends' keyword.
10. **Encapsulation**: Implement encapsulation using private modifiers and getters/setters.
11. **Polymorphism**: Use method overriding and object polymorphism.
12. **Interfaces**: Understand interfaces and their implementation.
13. **Abstract Classes**: Differentiate between abstract classes and methods.
14. **Exception Handling**: Mastery of try, catch, finally, throw, and throws.
15. **Java API**: Familiarity with commonly used classes in java.util, java.io, etc.
16. **Generics**: Understand the use of generic types and methods.
17. **Collections Framework**: Knowledge of List, Set, Map, and their implementations.
18. **Lambda Expressions**: Grasp functional interfaces and lambda expressions.
19. **Streams API**: Understand the use of Java streams for collections.
20. **Annotations**: Familiarity with built-in annotations and how to create custom annotations.

#### Core APIs

You should also be familiar with core APIs like `java.lang`, ` java.util`, `java.io` and others for various operations.

#### Exception Handling

Java's approach to error handling through try, catch, throw, throws, and finally constructs is a fundamental aspect of the language.

#### Java Memory Management

Understanding how Java manages memory, including the stack and the heap, garbage collection, and how to write memory-efficient code.

#### Concurrency

Java's model for multi-threading and concurrency, using threads, the Executor framework, and synchronization, is important, especially for high-performance applications.

#### Java Collections Framework

Knowledge of collection classes and interfaces, including List, Set, Map, and Queue, and how to choose the appropriate collection type.

#### Generics

The use of generics in Java for type safety and reducing runtime errors.

#### Java I/O and NIO

Familiarity with Java's Input/Output (I/O) for data streaming, as well as the New I/O (NIO) for more efficient I/O operations.

#### Java 8 and Newer Features

If you've been out of the Java world for a while, catching up on the newer features introduced in Java 8 and later, like lambda expressions, Stream API, new Date/Time API, Optional class, and more, would be beneficial.

#### Design Patterns and Best Practices

Understanding common design patterns (like Singleton, Factory, Observer, and Decorator) and best practices in Java programming for maintainable and scalable code.

#### JVM Internals

Basic knowledge of Java Virtual Machine (JVM) internals, including Just-In-Time (JIT) compilation, classloaders, and JVM options can be valuable, especially for performance tuning.

#### Frameworks and Libraries

Familiarity with popular Java frameworks and libraries like Spring (especially Spring Boot), Hibernate, or Apache Commons, depending on what the job entails.

#### Testing

Knowledge of testing frameworks like JUnit and Mockito, and the concept of Test-Driven Development (TDD).

#### Build Tools and Version Control

Experience with build tools like Maven or Gradle and version control systems like Git.

#### Kafka

#### 1. Kafka Basics and Architecture

- Understanding Kafka's publisher-subscriber model.
- Kafka as a distributed streaming platform.
- Architecture: Brokers, Topics, Partitions, Producers, and Consumers.

#### 2. Kafka Producers and Consumers

- Producing and consuming messages in Kafka.
- Producer APIs and Consumer APIs.
- Configurations, serialization, and deserialization.

#### 3. Kafka Topics and Partitions

- Topic creation and configuration.
- Role of partitions in scalability and parallelism.
- Log compaction and retention policies.

#### 4. Kafka Streams

- Stream processing basics.
- Kafka Streams API.
- Stateful operations and windowing.

#### 5. Kafka Connect

- Integration with external data sources and sinks.
- Configuring and using Kafka Connectors.

#### 6. Kafka Cluster Management

- Cluster setup and maintenance.
- Broker configuration and tuning.
- Zookeeper's role in Kafka.

#### 7. Kafka Security

- Authentication, Authorization, and Encryption.
- SSL/TLS, SASL, and ACL configurations.

#### 8. Performance Tuning and Monitoring

- Monitoring Kafka performance and health.
- Key metrics.
- Tuning producers, consumers, and brokers.

#### 9. Kafka Ecosystem and Integration

- Tools and technologies that integrate with Kafka (e.g., Apache Flink, Apache Spark, ELK stack).

#### 10. Real-world Use Cases and Best Practices

- Common patterns and anti-patterns.
- Scaling Kafka in production environments.

#### 11. Recent Updates in Kafka

- New features and significant changes in recent versions.

#### My Background

#### Neo4j

#### Serverless

Serverless computing is a cloud computing model that abstracts server management and infrastructure decisions away from the developer. It is often associated with "Function as a Service" (FaaS) platforms, but serverless extends beyond just compute resources. Here are some key aspects:

- **Event-driven and Scalable**: Serverless functions are typically event-driven, meaning they run in response to triggers (like HTTP requests, file uploads, or database events). The cloud provider automatically manages the scaling, so the function can handle many requests simultaneously without manual intervention.
- **Pay-per-use Billing Model**: In serverless computing, you only pay for the compute time you consume. There are no charges when your code is not running, which can lead to cost savings, especially for applications with variable traffic.
- **No Server Management**: Serverless removes the need for server provisioning or maintenance. The cloud provider takes care of the underlying infrastructure, including server and operating system management, capacity provisioning, automatic scaling, and patching.
- **Focus on Code**: Developers can focus solely on writing code and building features, without worrying about the underlying infrastructure.
- **Quick Deployments and Updates**: Serverless allows for faster deployments and updates. Since you're deploying functions, which are typically smaller than full applications, the deployment process is often simpler and quicker.
- **Stateless**: Serverless functions are stateless, and each function call is treated as an independent event. For maintaining state, you need to use external services like databases or cache.
- **Challenges**: While serverless offers many benefits, it also has challenges such as cold start issues (latency when a function is invoked after being idle), limited runtime (function execution time is usually capped by the provider), and potential complexities in debugging and monitoring.
- **Use Cases**: Common use cases for serverless include web applications, APIs, data processing tasks, and integrations with other cloud services.
- **Popular Platforms**: AWS Lambda, Azure Functions, and Google Cloud Functions are some of the major serverless platforms provided by cloud vendors.

### Retrospective

I think it went well. I know I've said that about pretty much all interviews I've had, though.

They asked questions about things I directly studied — mostly about horizontal scaling and Java-related questions. I felt I confidently answered all of them.

The PM asked me if I found it important to understand the customers/clients. The answer to this was pretty obvious — "Yes, of course it matters to me." and it really does. You need to understand the customer to understand the product. You need to understand the product to understand what to build and decide what matters. I didn't state it quite so succinctly in the interview, but that's more or less what I was getting at. I even backed it up with a story from my time in Germany when I had Peter set up an hour-long presentation on the 3 main personas we sold to.

The worst part of the interview was with the founders. They were weird af. The CEO has a serious fixed mindset/insecurity issue. It seemed he cared a lot more about showing off what he knew rather than asking me any questions. I think during the whole interview with them, they only asked me one question, "What motivates you?" there wasn't any follow up. I tried providing my own information since they weren't asking me anything. Every time I made a statement, the CEO would make a counter, obscurantist statement.

Some notable quotes from the CEO:

 - "We are an automation company!" — practically shouted.
 - "We are a philosophy company." — first thing he said as he sat down.
 - "We work with ideas, so it's good to see you have experience in working with ideas" — never followed up on what he meant when he said I had experience with ideas.
