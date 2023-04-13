Title: Debug Adapter Protocol - My First Impression 
Date: 2023-04-13 21:20
Category: IDE
Tags: IDE, VSCode, DAP

For the past 4 weeks I've been working on the mechanics of DAP for my IDE project. And there are so much things we can learn from project unittests. 

The debug adapter protocol is too large for me to simply read the protocol specification and understand the details of the interaction behavior or the correct order of how to call it. The reason why it is called state explosion is that the order of events (messages) between the debugging client and the debugging server can be arbitrary, and you will only know how to use it correctly until you try it yourself. Then I searched online for examples on how to use DAP as a starting point for learning how to use DAP.

Luckily I got this repo https://github.com/abhilashgupta/DAP-client as starting point.

In the DAP-client repo, I got a working example of DAP-client using `attaching` method to debug debuggee.

After finishing the "attaching" example, I moved on to the "launching" example, which exists only in the unit tests of the "debugpy" library, which is now maintained by the Microsoft VSCode team and is officially used to support the VSCode Python extension.

The unittests for "debugpy" are somewhat complex and require effort to understand how it works properly. The difficulty comes from following the fundamental difference between debugging a python debugger and debugging a normal python program.

1. The debugger cannot be debugged directly, so the development team of the DAP project invented a clever testing method called "timeline" to solve the problem of timing relationship verification in the message communication timeline.

2. If the debug adapter spawned a debuggee, and we're debugging this debug adapter, it was also spawned by the IDE's debug adapter, and is itself a debuggee. When a breakpoint is triggered, which debug clinet should be used? The debug adapter we spawned or IDE's debug adapter? Soon it will become a matryoshka problem. And can't be dealt with correctly.

3. The debugging process itself is very complicated. Taking "launching" as an example, the debugging client generates a debugging adapter server, and the debugging adapter server will generate a debugger. The debugged object is also a server. You can think of it as a virtual machine that runs a program python program in its controlled environment. The problem becomes even tricker.

In summary, the Debug Adapter Protocol (DAP) process consists of the following stages:

1. **Initialize**: The client sends an `initialize` request to the debug adapter to start the communication process. The debug adapter responds with an `initialize` response that includes information about the adapter and its capabilities.

2. **Launch**: The client sends a `launch` request to the debug adapter to start the debug session. The debug adapter will not respond with a `launch` response immediately, but responds an `initialized` event to notify client to do the breakpoints configurations. I call this: "Configuration Subroutine". The "Configuration Subroutine" starts with `initialized` event sent by debug adapter and ends with `configurationDone` response received by client which is sent by debug adapter to reponds to `configurationDone` request after all breakpoints are set.

3. **Configuration**: The client and debug adapter exchange information about the debug configuration, such as the program to be debugged, command line arguments, environment variables, and other options.

4. **Breakpoints**: The client sends requests to set or remove breakpoints in the code. The debug adapter responds with information about the breakpoints, such as their IDs and whether they are currently enabled or disabled.

5. **Stepping and control flow**: The client sends requests to step through the code, continue execution, pause execution, or terminate the debug session. The debug adapter responds with information about the current state of the program, such as the call stack and variables.

6. **Data inspection**: The client sends requests to inspect the values of variables or expressions in the code. The debug adapter responds with information about the values, such as their types and current values.

7. **Events**: The debug adapter sends events to the client to indicate changes in the state of the debug session, such as the program starting or stopping, breakpoints being hit, or errors occurring.

8. **Teardown**: The client sends a disconnect request to terminate the debug session. The debug adapter responds with a disconnect response and performs any necessary cleanup.

These stages are typically performed in a specific order, but some stages can be performed in parallel or out of order, depending on the needs of the debugging scenario. The DAP process is designed to be flexible and extensible, allowing developers to customize it to suit their needs.

After I have a preliminary understanding of DAP and how it works(the interaction behavior), I turned to the source code of the VSCode `mock-debug-example` and `contrib.debug` modules to learn more about VSCode's debugging capabilities, its design and implementation.

Now I can finally try to implement debugging functionality in our own python IDE.

