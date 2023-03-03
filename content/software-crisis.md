Title: How we control the complexity of the software over time and how do we move forward with legacy code.
Date: 2023-03-01 22:36
Category: Complex System
Tags: Complex System, Software Engineering, Software Crisis

> There is a Qt bug report dating back to 2014 and it remains open in 2023. 

Few days ago, when i was failed to add shortcut Meta+Tab to Qt application. And after hours of digging into it.
I found this to be a bug dating back to 2014, and it's still open. Obviously it needs someone to fix it, why hasn't anyone fixed it yet? I think the main reason is that the burden of legacy code maintainance grows quickly and people are tired of maintaining a lot of code let alone adding new features.

This incident made me think about software development and how the software around the world evolve over time. 

## The Software Crisis of 1970 and its Resolutions: Reflections on the Evolution of Software Development

Back to 1970 there was a software crisis. The main course of it is that computer became several orders of magnitude more powerful, but people still using the old ways to program, and with huge amount of demands expected to fullfiled by computer, the development of software soon crashed to the ground quickly.

So what happened in the past, and why do we hear so little about the software crisis now?

Hoare's paper is worth reading [How Did Software Get So Reliable Without Proof? ](https://gwern.net/doc/math/1996-hoare.pdf).

It concludes 4 points (at year of 1996) that can explain why have twenty years of pessimistic predictions been falsified. 
> Twenty years ago (at year of 1976) it was reasonable to predict that the size and ambition of software products would be severely limited by the unreliability of their component programs. Crude estimates suggest that professionally written programs delivered to the customer can contain between one and ten independently correctable errors per thousand lines of code; and any software error in principle can have spectacular effect (or worse: a subtly misleading effect) on the behaviour of the entire system. 

1. Management: The most dramatic advances in the timely delivery of dependable software are directly attributed to a wider recognition of the fact that the process of program development can be predicted, planned, managed and controlled in the same way as in any other branch of engineering.
2. Testing: When the program is implemented and passes all its tests the first time, it is almost unbelievable that there could be any inherent defect in the methods by which the program has been produced or any systematic lapse in their application. 
3. Debugging: Just correct the error and get on with the job,  analogy with the attempt to get rid of an infestation
of mosquitoes by killing the ones that bite you - so much quicker and cheaper and more satisfying than draining the swamps in which they breed.
4. Over-enigneering: The concept of a safety factor is pervasive in engineering. After calculating the worst case load on a beam, the civil engineer will try to build it ten times stronger, or at least twice as strong, whenever the extra cost is affordable.
5. Programming Methodology:  At one time, most programmers were proud of their skill in the use of jumps and labels. They regarded structured notations as unnatural and counter-intuitive. The decisive breakthrough in the adoption of structured programming by IBM was the publication of a simple result in pure programming theory, the Bohm-Jacopini theorem. And now we have data types and strict type-checking and information hiding. (The information hiding introduced by the ALGOL 60 local variable was generalised to the design of larger-scale modules and classes of object-oriented programming, introduced into ALGOL 60 by SIMULA 67.)

Linux 0.0.1 has less than 10,000 lines of code at the beginning and until year of 2020, Linux had 27,800,000 linex of code, 2780 times bigger! So I can think that somehow the software development crisis is solved because of the above 5 points, because the code base of Linux is now so huge that nobody can understand it thoroughly. Why Linux turn into a beast over years? I think these are the main sources that drive it as well as software development and complexity of our software world: 1) new requirements, 2) new circumstances, 3) new approaches. Without them, we wouldn't need to update our software anymore. (Think of library book systems, you can still use hardware and software designed 40 years ago and it will still work). And the world is like this: if a thing is done well enough to meet a certain need, it will become more and more stable and become a stepping stone for newcomers. In software we talk about reuse, in science we talk about known laws, they are the same in some way. If bug appears in software we fix(patch) it, if bug appears in theorm we ammend it. But there also a essential difference between software development and science exploration: 
> The program is proof(proving process) of specific problem can be solved by specific task or procedure using computer technology, it reveals the truth about problem solving, which is most likely man-made(we talk about software that used for officing and business mostly, except those to model and analyze natural phenomena). A theory is a proof of some scientific conjecture or hypothesis that may reveals the truch about fundamental laws of the universe, which is most likely god-made. And man's thoughts are constantly changing, but God's will is unchanging(of cause it's my personal belief).

## My Philothophy of Controlling Software Complexity(Controlled by Man-kind)

So if we agree structured programming is the main methodology of programming today, you also can agree that program can be dissected into several parts of code: Code that builds data structure(how the information is stored and how the information is piped between "scopes") and code that uses data to do side effects. And the chaos always coming from the poor orgnized information and messy pipes.

Let me explain more clearly: Structured programming emphasizes the use of control structures like loops, conditionals, and subroutines to build programs that are easier to read, understand, and maintain. Data structures are the way information is stored and manipulated in a program, and building them typically involves declaring variables, creating objects, and allocating memory. Once the data structures are in place, code can be written to perform side effects, which are actions that change the state of the program or its environment, such as printing output, reading input, or modifying files.

To avoid chaos and messy pipes, it's important to organize the data structures and their interactions with side effect code in a logical and coherent way. This can involve using well-defined interfaces between different parts of the program, following naming conventions, and commenting the code to make it easier to understand.

According to my many years of practical experience, the design of the API is always a key factor affecting the complexity of the system. And API can consider be the interaction protocol between different components and protocol between program and software engineers(human-being). If the protocol is confusing and redundant, so will the system.

So you might ask how can we design precise and concise APIs? 
**My approach to designing precise and concise APIs is to follow the principles of information theory, which aims to reduce information entropy as much as possible. Information entropy refers to the amount of uncertainty or randomness in a system, and reducing it can help to simplify the design of the API and make it more intuitive for developers to use.**

## Reduce Information Entropy as much as Possible: Design Software like a Linguist

Some specific techniques I suggests that can be used to reduce information entropy in API design include:

* Using clear and consistent naming conventions for functions, variables, and other elements of the API.
* Minimizing the number of parameters and arguments required to use the API, as this can help to reduce complexity and increase readability.
* Providing clear and concise documentation for the API, including examples and explanations of how to use different features.
* Designing the API to be as modular and composable as possible, so that developers can easily combine different components to achieve their desired functionality.
* Developing explicit segregated type systems for different functional domains in the system, and limit the number of types as much as possible.

By following these principles and techniques, software engineers can create APIs that are easy to use, understand, and maintain, which can lead to more reliable and efficient software systems. 

Software engineers always talk about software architectural design as if building software systems refers to architectural engineering. But I prefer thinking about software design as designing a new language, a new language consisting of a collection of term definitions(type system), imperative sentence(subroutines or functions performing tasks) and concept clarification(documentation), a domain specific language to describe and solve a range of problems in the domain. Language is the most powerful tool for human to communicate, it should be accurate, concise and understandable, just like we expect from our APIs.

## What Can We Expect in the Future: Will AI programmers control the complexity?

When Google launched in 1998, it forever changed the way people search and read information. Today, OpenAI released ChatGPT in 2023, forever changed the way people create content. I could not have written this article without Internet, Google and ChatGPT, and I also believe we can use natural language to maintain legacy code, update, develop software and forget about coding techniques and languages in the "near" future. 

And if this day comes, will AI control the software complexity as we did? Will our hard work be in vein as computer with much much bigger memory(RAM and databases) and process resouces(CPU) to enable AI to gain insights of extreamly large code base which human programmer can't read them all in life time? And will AI write messy code only AI can "understand"?

My prediction is: I don't think artificial intelligence will write poorly designed code then. One reason is that AI always finds the best way to do things, with my knowledge of reinforcement learning techniques used in today's AI development. If the AI ​​is optimized to use the least amount of resources, it will inevitably(automatically)  writes good code as a side effect of reducing information entropy to save memory and hard drive space as much as possible, and maybe it will not write documentation if we not specify it, since the coding part no longer requires human participation. Another reason is that we humans can and will optimize AI to generate clean and understandable code, because humans of course want everything under control and prevent the Terminator T-800 comes out of nowhere :)





