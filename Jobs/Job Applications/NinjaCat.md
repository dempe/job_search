---
type: job
applied: 2023-06-03
interviews:
  - 2023-06-22 10:00
  - 2023-07-10 13:00
  - 2023-07-10 14:00
  - 2023-07-11 14:00
status: rejected
source: remotive
job_type: fulltime
remote: true
industry: marketing
website: https://www.ninjacat.io/
location:
company_size:
recruited: false
listing: https://remotive.com/remote-jobs/software-dev/associate-software-engineer-1701757
blog: https://www.ninjacat.io/resources/blog
correspondence: email
title: NinjaCat
date_created: "2023-06-06 15:15"
date_modified: "2025-05-31 13:30"
---

## Application

### Summary (optional)

I have a total of 6 YOE in backend engineering.

I worked at DataRank/SimplyMeasured (now SproutSocial), so I am familiar with working with marketers and marketing data. During my tenure there, I was in charge of data collection and managing our API gateway.

In my previous role I was hired as Senior Data Engineer at Dennemyer/Octimine in Munich. I got data from our data warehouse to ElasticSearch and the front-end. When I joined, the process they had for this was really janky, took days, and had almost no testing. So I started the effort to migrate everything over to a real-time, event driven system using Kafka.

I also see that Ninjacat is using Laravel! I have recently become a huge fan of Laravel after converting my personal website ([chrisdempewolf.com](chrisdempewolf.com)) to use it. It's a static website. I run the Laravel server and use wget to pull down a static version. It's not the prettiest build setup, but it's worth it to use PHP/Laravel for my site. There is no better language than PHP for HTML templating. And since I'm not using someone else's static site generator, I know how everything works and control everything. Plus, I have a nice SQLite backend that makes working with various relationships (e.g., post<->tags, a many: many relationship) muuuch simpler than without a relational DB. I'm also a huge fan of the Laravel ORM, Eloquent.

I also have experience with Kotlin — [I wrote an SDK for the Pinterest API](https://github.com/dempe/pinterest-java) and published it on Maven Central.

It seems like we'd be a great fit! Call me? 🤙🏼

## Interview Screen Prep

### Questions to Ask the Interviewers:

1. Can you provide an example of a recent product feature or enhancement that the engineering team at NinjaCat developed? How did this impact the users?
2. What's the most challenging aspect of handling high-volume data for marketing analytics? How does NinjaCat approach these challenges?
3. Can you tell me more about the technology stack used at NinjaCat, specifically for data integrations and services? Are there any plans to adopt new technologies or frameworks?
4. How does NinjaCat ensure the scalability and maintainability of its Laravel applications? Are there specific methodologies or practices the team follows?
5. Can you describe the typical workflow of a software engineer at NinjaCat, especially in relation to collaboration with product owners, DevOps, SRE, QA engineers, and customer support?
6. How does NinjaCat support the learning and development of its engineers? What opportunities are there for skill enhancement and career growth?
7. What are the key performance indicators that NinjaCat uses to measure the success of a software engineer?
8. How does the engineering team at NinjaCat utilize AWS or other cloud services? Are there any specific challenges the team faces with cloud-based solutions?
9. NinjaCat emphasizes a unique culture built on compassion, action, and trust. Can you provide examples of how these core values are reflected in the day-to-day activities of the engineering team?
10. What is the roadmap for NinjaCat over the next year? Are there any exciting developments or challenges that the engineering team will be focusing on?

### Key Things to Study (Overview)

1. **Laravel and PHP**: Review the fundamentals of PHP and Laravel, focusing on best practices for building scalable web applications.
2. **VueJS**: Study the basics and advanced features of VueJS, and understand how it can be used to build responsive and intuitive user interfaces.
3. **MySQL**: Refresh your knowledge on MySQL, especially in terms of performance tuning and optimization. Know how to write efficient queries and how indexing works.
4. **APIs and Postman**: Review how to make API requests, and how to use Postman or similar tools to test API requests and responses. Understand the common issues in API integration.
5. **Microservices and Kubernetes**: Understand the basic concepts of microservices architecture and how Kubernetes is used for orchestration.
6. **AWS Services**: If you have experience with AWS, review the services that are commonly used in data processing and web application hosting.
7. **Data Warehousing**: If you have experience with data warehouses like Snowflake, BigQuery, or Redshift, brush up on how these tools are used for large-scale data analytics.
8. **Agile Methodologies**: Since the job description mentions working in an agile fashion, review agile principles and be prepared to discuss how you have used them in previous projects.
9. **NinjaCat's Product and Mission**: Familiarize yourself with NinjaCat's platform and mission. Understand what they do and how they serve their customers.

**Key things to study broken down**:

### Laravel and PHP

#### Laravel 's MVC Architecture

Laravel is a PHP framework that follows the MVC (Model-View-Controller) design pattern. Let's break down how Laravel uses each component of the MVC architecture:

1. **Model**: Models represent the data structure in a Laravel application. They interact with the database, handling data manipulation, storage, and retrieval. Models in Laravel correspond to tables in the database and allow you to work with query builders or the Eloquent ORM for database operations.
2. **View**: Views in Laravel are responsible for rendering the user interface. They present data to the user in a format they can understand. Laravel uses the Blade templating engine for its views. Blade is a powerful, simple, and declarative language that allows you to write HTML templates with embedded PHP code easily.
3. **Controller**: Controllers in Laravel handle the application logic. They're responsible for reacting to user input and making decisions based on that input. This often involves retrieving data from a model, packaging it up, and passing it to a view for rendering. Controllers essentially act as a middleman between the model and the view.

Together, the MVC components in Laravel enable a clean separation of concerns. Here's a simple flow:

1. The user makes a request, which is directed to a specific controller by the routing system.
2. The controller interprets the request and performs necessary validation and authorization checks.
3. If needed, the controller interacts with the relevant model(s) to retrieve or store data.
4. The controller then packages this data and sends it off to a view.
5. The view renders the final webpage, which is served back to the user.

By separating the application into these components, Laravel allows for efficient, modular, and maintainable code. Each component has a specific job and is relatively independent of the others, making it easier to develop, test, and maintain the application.

#### Routing

Sure, here's a brief explanation of each of these concepts in the context of Laravel:

1. **Routing**: Routing is the mechanism by which an HTTP request is matched with the appropriate code to run in response. In Laravel, routes are defined in route files located in the `routes` directory. These route files return routes that the Laravel router should respond to. Here is an example of a simple route definition:

    ```php
    Route::get('/hello', function () {
        return 'Hello World';
    });
    ```

    In this example, Laravel will respond with "Hello World" when someone visits `yoursite.com/hello`. The routing system is also responsible for passing parameters through the URL, binding route parameters to models, and grouping routes together for shared configuration settings.

#### Middleware

Middleware provide a way to filter HTTP requests entering your application. For example, Laravel includes a middleware that verifies if the user of your application is authenticated or not. If the user is not authenticated, the middleware will redirect the user to the login screen. However, if the user is authenticated, the middleware will allow the request to proceed further into the application. Additional middleware can be written to perform tasks like verifying the user's role or preventing certain types of content from being processed if certain conditions aren't met. Middleware can be applied globally to every request, or to specific routes.

Middleware is different from controllers in that it handles application logic that applies to **all** incoming (or outgoing) requests (e.g., authentication, authorization, CSRF protection, rate limiting). It is defined in `app/Http/Middleware`. A middleware class must implement the `handle` method. `handle` takes two arguments, the request and a `Closure` that specifies the next middleware in the chain. In this manner, a request can be passed from middleware to middleware recursively. Here is an example:

```php
namespace App\Http\Middleware;

use Closure;

class YourMiddleware
{
    public function handle($request, Closure $next)
    {
        // Perform your logic here...

        return $next($request);
    }
}
```

#### Service Providers

**Service Providers**: Service providers are the central place to configure your application. If you open the `config/app.php` file included with Laravel, you will see a `providers` array. These are all the service provider classes that will be loaded for your application. These service providers bootstrap your application by binding services in the service container, registering events, or performing any task required before your application handles a request. For example, the `RouteServiceProvider` in Laravel loads your route files.

Service providers make it easy to organize and manage the bootstrapping process of Laravel applications, whether they are reading configuration files, registering services, or routing. They are the backbone of a Laravel application, holding it together and ensuring the various parts work in harmony.

**Service providers**. As I understand it, they are a dependency injection mechanism. They load up a service based on configuration parameters. They are defined in `app/Providers`. They extend `Illuminate\Support\ServiceProvider` and implement one or both of `register()` or `boot()`.

`register()` is for creating a new service before other services are available. It binds things to Laravel's service container.

`boot()` is for after all the services have been registered. You can use it for conditional binding or filtering of services.

There are **two ways** of accessing a service once it is loaded:

1. Use Laravel's ORM
2. Call the `app()` function to access the service container.

In terms of which is more idiomatic, DI is generally the preferred method. This is because it decouples your code, makes it more easily testable, and makes it more explicit what the dependencies are for a class, because they are listed right there in the constructor.

Accessing the service container directly is only really useful if you have a dependency that is only conditionally needed.

Here's an example of using DI to access a logging service:

```php
class SomeClass {
    protected $logger;

    public function __construct(Logger $logger) {
        $this->logger = $logger;
    }
    
    public function someFunction() {
        $this->logger->info('This is an informational log');
    }
}
```

Service providers decouple service-related code from application code and make those services available to all classes that need them. This promotes a clean separation-of-concerns and makes code **more maintainable**, **more readable**, and **more testable**.

Decoupling also means that one instance of a service can be swapped out for a different instance.

**What do you do if you have multiple configurations for a service and need to load specific configurations for specific controllers?**

**Contextual binding** to the rescue! Contextual binding allows you to configure which controller gets which service instance. Let's say you have a `PaymentsGateway` with two implementations: `StripePaymentsGateway` and `PaypalPaymentsGateway`. The contextual binding for these might look like this:

```php
$this->app->when('App\Http\Controllers\StripeController')
          ->needs('App\Contracts\PaymentGateway')
          ->give('App\Services\StripePaymentGateway');

$this->app->when('App\Http\Controllers\PaypalController')
          ->needs('App\Contracts\PaymentGateway')
          ->give('App\Services\PaypalPaymentGateway');
```

#### Eloquent ORM

An ORM allows you to interact with the DB using object-oriented code instead of raw queries.

Some benefits of an ORM include:

- Abstraction away from low-level DB features allows you to focus on higher level concepts like models and relationships between them
- Being DB-agnostic means you can switch to a new DB more easily
- They add sanitization to prevent things like SQL injection
- They provide an expressive syntax that make code more readable, maintainable, and testable

**Relationships** can be expressed using any of:

- `hasMany` 1:many
- `hasManyThrough` 1:1:many
- `belongsTo` many:1
- `belongsToMany` many:many
- `hasOne` 1:1
- Etc

Eloquent provides a fluent interface **query builder** that allows you to chain methods to a model that map to SQL queries. Some examples are:

- `where`
- `limit`
- `sort`
- `join`
- Etc.

`Post::where('id', $id)->pluck('title')`

**Data retrieval and manipulation**. Eloquent provides higher level functions (higher level than the query builder) for performing common tasks related to data retrieval and manipulation. Some examples are:

- `find`
- `first`
- `create`
- `update`
- `delete`
- Etc.

#### Database Migrations

- What are DB migrations?
	- A version-controlled approach to managing DB schema changes.
- What do they do exactly?
	- Define and track changes to the DB structure over time.
- What do they make it easier to do?
	- Ensure consistency across environments
	- Collaborate with other developers
	- Manage Db updates
- How do you create a new migration for the `users` table?
	- `php artisan make:migration create_users_table`
- Where are Laravel migrations created?
	- `databases/migrations`
- What two methods does a migration implement?
	- `up()`
	- `down()`
- What does `up()` do?
	- Defines the operations needed to create or modify a table.
- What does `down()` do?
	- The reverse of `up`, it tears down the table.
- How do you apply migrations to your database?
	- `php artisan migrate`
- What do you do if you want to add a new column, `username` , to the `users` table?
	- Create a new migration: `php artisan make:migration add_username_to_users_table`

#### Dependency Injection and IoC Container

Mostly covered in the "Service Providers" section.

#### Testing in Laravel

- What testing framework does Laravel use?
	- PHPUnit
- What class does a test extend?
	- `TestCase`
- Where are tests created?
	- `tests` directory
- Can use test DB. Laravel makes this easy via seeding and migration and having separate configs for test env
- How do you run the tests?
	- `php artisan test`
- How do you test various routes and HTTP methods?
	- Using Laravel's built-in `get()`, `post()`, `json()`, etc.
- Laravel provides services for mocking and faking data and dependencies
- What does mocking do?
	- Isolates what you're testing from its dependencies
- Three types of tests (in order from less scope to more):
	- Unit
	- Integration
	- System
- Laravel provides functionality for setting up a test DB and seeding it with fake data
- For a Laravel application, a system test might involve testing the end-to-end user experience, from accessing a page, to submitting a form, to viewing the results.

#### PHP OOP Principles

The four major principles of OOP:

1. Encapsulation
	1. Encapsulation in OOP is all about hiding the internal states and functionalities of an object and only exposing the necessary parts through methods, often referred to as the object's interface.
	2. It helps to maintain the integrity of the objects by preventing external code from changing their internal state in unpredictable ways.
2. Polymorphism
	1. polymorphism is a principle that allows objects of different types to be treated as objects of a common type.
	2. **Interfaces** are one type of polymorphism
	3. **Method Overriding** (Subtyping) is another. A subclass can override a parent method's behavior.
	4. **Method overloading**. AKA function polymorphism. In java, can create new methods of the same name with different args. However, this is not supported in PHP. Instead, in PHP, you can use default args or varargs to achieve the same.
3. Inheritance
	1. allows for code reusability and a logical, hierarchical organization of code.
4. Abstraction
	1. Means only providing functionality to the user while hiding implementation details
	2. I.e., the user knows **what** the object does, not **how** it does it.
	3. Abstraction allows us to create a general concept or model that helps encapsulate and categorize more specific instances, making our code more flexible, extensible, and easy to maintain. It also promotes the concept of code reusability.

Difference between abstraction and polymorphism??

Abstraction is more about the design of your code. You make a `processPayments` method on your `PaymentGateway`. This nicely abstracts the underlying mechanism.

Polymorphism is a way of performing a single action in different ways. All implementations of `PaymentGateway` will have a `processPayments` method that function differently depending on the implementation.

In other words, polymorphism is a mechanism that allows us to make the most of our abstractions.

#### Handling Exceptions and Errors in PHP

### VueJS

   - VueJS lifecycle
   - Using Vue Router and Vuex state management
   - Component communication (props, events)
   - Directives, filters, and mixins
   - Async operations in Vue (promises, async/await)
   - Vue CLI and build process
   - Testing in VueJS

### MySQL

#### Writing Complex Queries and Joins

#### Database Normalization and Denormalization

#### Understanding Indexes and when to Use Them

#### Performance Tuning and Query Optimization

#### Transactions and ACID Properties

#### MySQL Storage Engines and Their Differences

### APIs and Postman

#### RESTful API Principles

#### HTTP Methods, Status Codes, and Headers

HTTP methods provide a standardized way to perform different operations on resources. HTTP methods include GET, POST, PUT, DELETE, HEAD, OPTIONS.  

- What is the difference between PATCH and PUT?
	- PUT is idempotent, PATCH is not
- What does it mean for an HTTP method to be "safe"?
	- It does not affect server state.
- Which methods are safe?
	- GET, HEAD, OPTIONS
- Which methods are idempotent?
	- GET, HEAD, OPTIONS, PUT, DELETE

Status codes indicate the status of how the request was received on the server. 200 — OK, 300 — moved domain (temporary or permanently), 400 — user-class errors (bad request, unauthorized, unauthenticated, pages doesn't exist, rate-limited, teapot, unacceptable entity), 500 — server class errors.

Headers are key-value pairs that indicate metadata about the request or response like content-type, language, host, encoding, authentication, caching directives, etc.

Common request headers:

- Accept
- User-Agent
- Cookie
- Authorization
- Cache-Control
- Host

Common response headers:

- Content-type
- Content-length
- Location (common in redirects)
- Set-Cookie
- Cache-Control
- Access-Control-Allow-Origin

#### JSON and XML Data Formats

#### Postman for API Testing

#### OAuth and other Authentication Methods

- What does OAuth stand for?
	- Open authentication
- What is OAuth?
	- An open standard for a user to grant third-party applications access to resources on a server without sharing credentials with those third parties.
- What is OAuth commonly used for?
	- Allowing a user to login to a service using an existing account like Google, Facebook, or Twitter.

#### Rate Limiting and other Common API Issues

### Microservices and Kubernetes

#### Microservices Architecture and Its Advantages

#### Docker and Containerization

> Docker images are a bit like blueprints, while Docker containers are the "buildings" that get constructed based on those blueprints.

  — ChatGPT

In the Docker world, an image is a lightweight, standalone, executable package that includes everything needed to run a piece of software. This includes the code, a runtime, libraries, environment variables, and config files.

A Docker container, on the other hand, is a runtime instance of an image - what the image becomes in memory when executed. Multiple containers can be run from the same image, each isolated from each other and from the host system.

Due to the ephemeral nature of Docker containers, data persistence is a big problem. To solve this, docker provides what are called **volumes**. Volumes are managed by docker and stored on the filesystem. They can be shared between containers. Can also be used to backup data or migrate data from one system to another.

Can also use **bind mounts** or **tmpfs mounts** for data persistence. Unlike volumes, these are not managed by docker. Bind mounts are stored on the filesystem, while tmpfs mounts are stored in memory. Bind mounts can be useful for making live updates to the data available to Docker. For example, if you're editing code and want the changes to be immediately available to the container.

Tmpfs mounts are useful for when you only want data to be persisted for as long as the container is running. Since they are stored in memory, the data is lost as soon as the container goes down.  

While both bind mounts and tmpfs mounts are more suitable for sensitive information than volumes, tmpfs mounts are even moreso.

There are **three** default **docker networks**:  

- Bridge
- Host
- None

Bridge is the default-default. It's a private internal network for your containers.

Host shares its network stack with the host machine, bypassing the network isolation. This is also more performant, as docker's bridge network comes with an overhead. So this might be a good choice if performance is an issue.

None is when there are no network connections. Might be useful for security or testing behavior without network access.

#### Kubernetes Architecture (Pods, Services, Deployments)

- What is k8s?
	- An open-source container orchestration platform.
- What does k8s automate?
	- The deployment, scaling, and management of containerized applications.

Docker manages single containers. K8s is about manages large numbers of containers that work together across multiple machines.

#### Kubernetes Networking, Storage, and Security Basics

#### CI/CD In a Microservices Environment

#### Monitoring and Logging in Kubernetes

### AWS Services

#### EC2

#### S3

#### RDS

#### Lambda

#### IAM for Security and Access Control

#### AWS Networking (VPC, Subnets, Security Groups)

#### AWS CLI and SDKs

#### Managed Database Services like DynamoDB

#### AWS Monitoring Tools like CloudWatch

### Data Warehousing

#### Understanding of ETL (Extract, Transform, Load) Processes

ETL processes are used for integrating and preparing data from various sources for analysis, reporting, and data warehousing.

The three parts:

- **Extract**: extract data from a heterogeneity of sources. For example, APIs, DBs, files, etc.
- **Transform**: transform all extracted data in to a **common format**. This might include cleaning, filtering, joining, aggregating, or converting data types.
- **Load**: load data into a DWH or DB where it can be **used for analytics and reporting**.

**Challenges**:

Three I mentioned:

- **Data mapping**: requires understanding the semantics of each data source and establishing a common, canonical model requires deep domain knowledge
- **Schema evolution**: keep up-to-date with changing APIs
- **Authorization and authentication**: keeping customers' creds up-to-date is important. Also dealing with rate limiting

Some others:

- **Data quality/cleaning**: data is not always "clean" and we must account fort this somehow
- **Data volume and performance**: large volumes of data must be handled in a timely manner
- **Error handling/monitoring**: errors must be caught and corrected quickly before they impact downstream processes
- **Security and compliance**: data must be handled securely and be in compliance with data protection laws
- **Scalability**: need to be able to scale ETL processes
- **Data transformation**: data transformation can be very complex
- **Historical data**: how should historical data be handled?

### Snowflake

SF is a cloud-based DWH used to store an analyze large amounts of data.

- What is so unique about SF?
	- It separates storage and computing, allowing them to scale independently
- What is this separation know as?
	- SF's multi-cluster shared architecture
- Being able to scale compute and storage separately is useful for varying workloads and data volumes
- What compute resources do you pay for?
	- Only the ones you use.
- Since compute and storage are decoupled, you don't pay for idle computation just because you needed more storage
- Multiple compute clusters can access the same storage concurrently
- Can handle a large volume of concurrent users and queries without performance degradation
- What is **over-provisioning**?
	- Paying for resources that you aren't using.
- What is **under-provisioning**?
	- Not having enough resources when you need them
- Unlike traditional DWHs, SF avoids the problems of under and over-provisioning due to its multi-cluster, shared architecture and separation of computation and storage.

#### Familiarity with Data Warehouse Architectures (star Schema, Snowflake schema)

#### Basics of Data Modeling

#### Experience with SQL for Data Analytics

#### Understanding of Columnar Databases and Their Advantages for Analytics

#### Familiarity with BI Tools and Data Visualization

### Agile Methodologies

   - Understanding of Agile principles and values
   - Knowledge of Scrum or Kanban frameworks
   - Familiarity with Agile roles and ceremonies
   - Experience with story points and velocity
   - Understanding of backlog grooming and sprint planning
   - Familiarity with Agile tools (e.g., Jira, Trello)

### NinjaCat 's Product and Mission

   - Familiarize yourself with the company's product offering
   - Understand the company's mission and core values
   - Research the company's market and competition
   - Understand the company's growth and future plans
   - Research any recent news or updates about the company
   - Understand how the role you're applying for contributes to the company's mission and goals

Remember, you don't need to be an expert in all these areas. The goal is to have a good understanding and be able to discuss these topics intelligently during your interview. Good luck!

## Interview Screen Follow-up

Overall, I feel really good about it (surprisingly).

They didn't really ask any technical questions. They just asked me to introduce myself. Then asked me to describe a project I recently worked on. I talked about my experience with Kafka. He had some follow-up questions like "how did you deploy it? Was it using containers?", "why were you guys switching to realtime? Was it for cost or otherwise?", "where was the data going?".

### What Went well

- Talked pretty fluently and confidently
- Had good questions
- Had good comments
- My experience really jives with what they are doing (marketing plus data ingestion)
- Seem like really cool folk

### What Didn't Go well

- Sound issues
	- Could not hear them at the beginning *even though I tested audio in Zoom*….
	- Luckily they were nice about it and gave me an extra 5 minutes
- My closing was really weak.
	- Andy gave me an overview of next steps/what to expect/the interview process. It actually sounded really good — no BS algorithms Qs and there will be a pairing exercise (in Java, PHP, or Typescript), meet with product, meet with team members
	- after that, I think I said, "that sounds great!" which is fine, but right after that, I said "see you guys later. And nice to meet you." I really should've added something else. Like saying **"Well, thanks so much for taking the time to meet with me today. I know you guys must be really busy, so I won't take any more of your time. It was pleasure to meet you Andy and Winnie."**
- Andy asked me about the deployment of Kafka. He asked if we used containers. I said we used them for testing only, but *that's not true*. **We did in fact deploy Kafka using Docker containers**.

## Technical Project Interview (45 min)

> A project deep dive ("Tell us about a recent project you worked on…")

This is the first part of a two-part 90 min technical interview. I already discussed Kafka in my interview with Andy and Winnie. I don't feel comfortable talking about that one for 45 minutes.

Instead, I will opt to talk about a Laravel app that I built/will build.

I think this is a good idea for the following reasons:

- They use Laravel, hence it will be good to show experience in it. Also, this pairs well with my chosen language for the pair-programming interview, Kotlin. It shows that I have experience with two of their main tech stack languages.
- I *want* to learn more about Laravel
- It's much more *recent* than my Kafka experience
- Plus, I have *control* over it — I can and will continue to develop and work on it over the next week. Unlike the Kafka project which I worked on a year ago.

I guess the only real downside is that it doesn't show any sort of team experience given that it's a solo project.

**Steps**:

1. Write blog post detailing current Laravel app and how it's deployed.
2. Create branch for non-static features
3. Add user login
4. Add basic account management
5. Add commenting/comment management
6. Add a fuzzy search feature for posts
7. Time permitting, write a follow-up blog post about full app

ChatGPT-generated Qs:

- Can you give a high-level overview of this project? What was the business need or problem that this project was addressing?
- What was your role in this project? How big was the team and how was it structured?
- How did you start this project? What were the steps taken in the planning phase?
- What were the main technologies or tools used in this project and why were they chosen?
- Can you discuss the architecture of the system you developed? What were the key components and how did they interact?
- Did you face any major challenges or obstacles during the project? How did you overcome them?
- How did you ensure the quality of your code? Did you use any testing frameworks or practices?
- How was the project managed? Did you use any project management methodologies or tools like Agile,

### Retrospective

I talked about both Kafka and Laravel — Kafka in my background story/section, Laravel as my chosen project.

#### Pros

- Laughed, smiled, joked, had a good conversation.
- Described my past experience with Kafka well.
- Think I covered my use cases for Laravel pretty nicely.
- Asked decent questions. A few technical, a few not.
	- "You mentioned that you are splitting your Laravel app out into microservices. What exactly are these microservices? APIs?"
		- Basically, when something in the Laravel app needs updating, they move it to a dedicated microservice.
	- "How do you deploy your microservices? Containers?"
		- Using K8s, Helm
	- "Is there on call?"
		- No. The infra team, possibly, but not for devs.
		- You are given a high degree of trust and responsibility to make sure your tasks are working as they should.
		- Maybe will have on call in the future.
	- "How's the feedback system? 1:1s?"
		- You set the cadence for your 1:1s!
		- They have some program that allows you to request or submit feedback for any co-worker.

#### Cons

- Should have offered to **share my screen to show Laravel app**
- I asked "how do you like NinjaCat?" Steve raised an eyebrow haha.

## Pair-programming Interview (45 min)

> A pair programming project in your choice of language - There's 3 choices - PHP, Kotlin and TypeScript. Which would you prefer? We'll send you a link to the repo beforehand and you can run it, or we can run it from our end while you tell us what to do / control the screen.

I chose Kotlin. Need to finish the Kotlin koans to learn about Kotlin idioms.

Remember to focus on communication.

### Retrospective

Fuck the task was super easy. Made some obvious blunders, though. It's like I'm docked 20 IQ points during an interview coding session. Anyways.

Couldn't get it to load on my comp, so Steve drove.

Was basically a pair programming task with three people.

[Here's](https://gitlab.com/ninjacat-public/technical-interview-exercises/kotlin-etl-exercise) the repo/explanation.

#### Pros

- Solved the problem
- Solved the "bonus" problem
- Used an extension function, which Steve mentioned he liked
- Made a separate `TransformException` class for clarity

#### Cons

- **Missed the `map` in the "fix the failing test" part** and created an unnecessary `set`. Maybe, what I need to do is just go a bit slower. Read each line. Understand each line. Like in salsa — RELA-JE-SE.
- Had a few syntactic errors come up, but they both weren't sure either.
- **Missed the `toLowercase`** in the "bonus" part to determine score. When the test failed, it should have been obvious that we missed converting to lowercase.
- I didn't have Gradle set up. Luckily, since Steve drove, it didn't matter. Not sure how big of deal this would be overall, but I do **need to learn Gradle**.

## Peer Interview (30 min)

> This is an interview with a fellow engineer on the team to learn about how you deal with engineering challenges day to day.

This sounds like a behavioral/cultural fit interview.

**Things to study**:

1. Behavioral questions
2. Culture at NinjaCat

**ChatGPT-generated Qs**:

1. **Technical Problem-Solving**:

   - How do you approach solving complex technical problems?
   - Can you describe a recent challenging problem you faced and how you resolved it?
   - What tools or strategies do you use to debug and troubleshoot issues?

2. **Collaboration and Communication**:

   - How do you effectively collaborate with teammates to tackle engineering challenges?
   - Can you give an example of a time when you had to work closely with others to overcome a technical hurdle?
   - How do you communicate technical concepts to non-technical team members or stakeholders?

3. **Decision-Making and Prioritization**:

   - How do you prioritize tasks and make decisions when faced with competing deadlines or conflicting requirements?
   - Can you discuss a situation where you had to make a trade-off between quality, speed, and resource constraints?
   - How do you approach evaluating and selecting technology or frameworks for a project?

4. **Continuous Learning and Improvement**:

   - How do you stay updated on emerging technologies and industry trends?
   - Can you describe a time when you identified an area for improvement in your technical skills or processes and took action to address it?
   - How do you encourage a culture of learning and knowledge sharing within your team?

5. **Handling Challenges and Mistakes**:

   - How do you deal with setbacks or unexpected obstacles in your work?
   - Can you share an example of a mistake or failure you encountered and how you learned from it?
   - How do you approach risk assessment and mitigation when implementing technical solutions?

**GPT4 Qs**:

- Can you tell me about a challenging technical problem you've had to solve, and what your process was to solve it?
	- My previous job had a batch processing job written in Python to process about 30 million legal documents per week. The problem was that I twas super slow. It would take multiple days to run, normally 2 or 3, but if we had a serious issue, it could overlap with the next week's job.
	- I proposed we migrate to a realtime event-driven system. There was no reason to be processing these documents in batch anyways as they came in continuously.
	- All (three) backend engineers and our infra guy met to analyze our current set up and how to proceed.
- How do you approach learning a new technology or tool?
	- I think the only way to really learn something is to start using it. This is the difference between knowledge and know-how. Just because you have knowledge of how to ride a bike, doesn't mean you can ride a bike. I find this applies to many things, engineering included.
	- For programming languages, I see if there is a set of koans to solve to become familiar with the syntax. Then I try to start programming some simple programs for example, Project Euler, Advent of Code, or LeetCode problems are nice simple, problems to get started.
	- For tools, Docker has made this quite easy. Just download an image of the tool you want to learn, find a tutorial, and start building a PoC.
	- Lastly, with the advent of ChatGPT, I like to give ChatGPT a "socratic tutor" prompt so that it asks me questions to guide my understanding, without explicitly telling me the answers. I find this is a great way to learn the "hows" and "whys".
- Can you describe a time you received critical feedback and how you dealt with it?
	- At Octimine, they mentioned that I didn't know enough on the legal side. I took this as a learning opportunity to brush up on my legal knowledge. I made a bunch of Anki flashcards about IP legal topics and started studying. It's important to **never take critical advice personal**. That gets you no where.
	- I think this is a good way to approach any sort of "failures" or shortcomings. They are great learning opportunities, a way to improve as a engineer, a person. This is called the "growth mindset".
	- Sometimes, you might be in a bad mood or someone gives you critical advice in a rude manner. If you feel yourself starting to take something personal, just meditate for 10 minutes.
- Have you ever disagreed with a team member about a technical approach? How was it resolved?
	- Try to understand their point of view. Ask them **questions** to make sure you understand perfectly. People these days ask far too few questions. A lot of disagreements can be solved by asking probing questions and making an effort to communicate and understand each other.
	- Use an evidence-based approach. Once we understand each other, weigh the pros and cons of each approach based on what we know. Don't make assumptions, don't speculate. Use what we know and go from there.
	- Maintain a focus on project goals. It's also very important to maintain a focus on the end goal. What exactly are we trying to achieve? Which approach would accomplish this goal? If it comes down to a tradeoff between speed and quality, there's always a larger goal — which approach fits better with company objectives, with **what our CUSTOMERS want**?
- Can you give an example of a technical compromise you had to make?
- Can you explain a complex technical concept to me as if I were a non-technical team member?
	- Sure, let's talk about containerization.
	- We have an app that we need to run on my machine, on your machine, in the cloud, in a variety of environments, but it needs to function exactly the same. How can we do that?
	- We can use containers. Containers a way to run an exact replica of an app in a variety of environments.
	- How do you think they might do that? For one, all containers run the Linux operating system. They're small because they only contain the code necessary to run your app, nothing more. In contrast to a virtual machine, which runs the entire operating system.
	- Since they're small, they can easily be deployed wherever you like.

### Retrospective

Overall, I think it went really well. Was basically just like a chat with friends. Felt very informal. They asked about my time in Germany. They asked what challenges I had there. I told them the problem I had at the gym (thank god they didn't ask anymore), because that was not one of my most sterling moments. **Matthew** followed up with a question — "did you experience any challenges like that at work?" I can tell now exactly what he was doing — he was trying to ask me in a roundabout, informal manner, "What challenges did you face in your previous job and how did you resolve them?" I didn't really pick up on that in the heat of the moment. I mentioned that we didn't really have any disagreements at work. Which was pretty true. At least at the time of the interview, I couldn't think of any. But now I realize I maybe could have mentioned the small conflict we had over the existence of Midlayer post-Kafka.

#### Pros

- Asked a lot of questions
- Smiled and laughed (maybe try to smile even bigger)
- Felt like a good convo
- Made a few jokes

#### Cons

- **Try to smile even bigger**. I think at one point Matthew looked at me after a joke he told. I was smiling but not super noticeably.
- Try to talk less about old workplaces. It paints you as a gossipy person who talks about others behind their backs. I think this is the biggest regret I have from this interview. I feel like I might have come off as bad talking my previous employer.
- Try to be more aware what people are really asking. Matthew was asking about challenges at my previous job, but he did so in and indirect fashion that I didn't pick up on.
- Also, have a list of stories ready to tell for these common questions. It might also help you pick up on when someone is asking something indirectly.
- My camera was off for about 10 mins. I apologized and everything was fine, but sth to check.

## Product Manager Interview (30 min)

> Interview with a PM or designer. This interview should focus on how you collaborate with product, design, and other teams.

Probably also a lot of behavioral stuff.

**Things to study**:

1. Past experiences with PMs

- Can talk about previous experience with monitoring PM at Octimine. We'll call him "Agasthya" because I don't remember his real name.
	- Old data ingestion pipeline might fail (take more than 7 days to complete). This meant monitoring emails would not be sent out correctly for that week.
	- Meant keeping Agasthya up-to-date on everything that's happening — **what** the problem is, **why** the problem is happening, **what I'm doing to fix it**, and **how long** I expect it to take
	- Emphasize that you understand the stress that PMs go through, and are appreciative of their role as interface to stakeholders.
	- Also, provide regular updates if something is not going as planned.
- Maybe talk about problem resolution if it comes up:
	- First identify all unknowns
	- Start filling in unknowns
	- Connections will start to form. If you still aren't able to figure it out, list what you known so far.
	- If you still aren't able to figure it out, go to a fellow engineer. But never blindly. Tell them everything you've tried, everything you know, and everything you don't know (and why you don't know)

### Retrospective

#### Pros

- Laughed and smiled.
- Chatted

#### Cons

- Talked too much I think. I went into a lot of details about previous projects that they didn't specifically ask about.

## Hiring Manager Interview (30 min)

> Interview with the hiring manager, Winnie. We'll cover questions that the previous rounds might have generated and dig a little more into your work history.

**Things to study**:

1. Previous interviews for NinjaCat
2. Resume

### Retrospective

#### Pros

- I asked a good question about what her expectations of me are.
- I think I gave a pretty good response for my onboarding plan: first meet the people I'll be working with by setting up 1:1s. then, pair, set up meetings, etc. To learn the projects I'll be working on. In short — acquaint myself with the people then the projects.
- I think I expressed that I enjoyed the whole interview process and meeting everyone. I mentioned how I think the culture that have at NinjaCat is really special and it shows through in the people I've spoken with.

#### Cons

- I should've taken the opportunity to ask her about her baby when it started crying. To make it a bit more personal/conversational/less formal
- A big one — I mentioned that I had other interviews when she asked me when I could start. NEVER mention that you have other interviews. The fewer details the better.
- I think you interrupted her (again). Try to avoid be too talkative (just relax) and try to avoid being too quiet (obviously).

## Interviews Follow-up Message

I said a few things I probably shouldn't have during the interviews. For example, I mentioned how my previous manager did not like to actually manage. I mentioned that I had other interviews that. I wanted to finish. Sometimes I just talk, and dumb things come out. But I still feel bad about this and want to rectify it however I can.

I was thinking about sending an email to Winnie letting her known (implicitly or explicitly) that I would accept any potential offer. Let's try.

```
Hi Winnie,

I hope you've had a great weekend and all is going well on your side. I just wanted to update you a bit on my side.

I am still very excited about the possibility of working at NinjaCat. As I mentioned on our call, I was particularly impressed with the culture and how genuine and down-to-earth everyone was. I try really hard in my personal life to cultivate a growth mindset, to learn from my mistakes and use them to continually improve. Seeing this on a company level is quite impressive!

I'm also excited about the tech side of things. I've spent my whole career as a software engineer working on data ingestion and a large part of it working in the marketing/social media industry at SimplyMeasured and SproutSocial. This background should allow me to hit the ground running, so I can hopefully focus on the deeper problems sooner and grow as an engineer.

Both culturally and technically NinjaCat aligns with what I'm looking for in my next role, and I would be delighted to be a part of the team!

Thanks for your time, and I look forward to continuing the discussion.

Have a great day,  
Chris
```

## Misc Notes

They (rightfully) place a lot of emphasis on tech. So learn that.

Even if I don't get the job, I will be *very* well prepared for future interviews.
