# 12CP_THESIS_INFO4001


Creating a DAP-Compatible Debug Adapter between Binaries and Debuggers. 

Software development in its various stages, involves the rigorous process and cycle
of writing code, testing, and debugging. As the development cycle evolves, the
need for these debugging tools to communicate seamlessly with the programs or
binaries becomes paramount as the software become more diverse and complex, the
extensibility of debuggers may either not exist or be sufficient enough to keep up
with new development ecosystems. To remedy this, this thesis delves into the Debug
Adapter Protocol (DAP), an approach designed to unify the communication between
development tools, IDE and various debuggers, which can help programmers to have
a consistent debugging experience across these diverse environments without having
to learn the intricacies of each debugger.
Our primary focus is the crucial role of the Debug Adapter, an intermediary
component that bridges the gap between existing debugger and the various binaries
or development tools through the DAP. This is essential as expecting a complete
adoption of DAP by existing debuggers is still very much unlikely as they require
significant modification to the individual debugger. Through this protocol, the
thesis examines how the introduction of such an intermediary reduces the effort to
integrate a new debugger, thereby offering a significant universal entry point to tools
such as different IDEs to interact with debuggers while maintaining its extensibility.
By adopting a wire-protocol through a JSON-RPC communication protocol, the
DAP offers flexibility in the language choice for the debug adapter implementation,
catering to the nuances of specific debuggers. Despite its high-level design, which
abstracts many of the underlying debugger intricacies, the DAP ensures that users
are able to send requests and receive comprehensive responses from the debugger,
thanks to the string-based data structures that can be mapped neatly onto a de-
bugger UI.
This project aims to build upon this concept, specifically targeting binaries pro-
duced by languages like C. It addresses the challenges and intricacies of creating a
debug adapter capable of translating between programs and binary executables and
the corresponding debugger, such as GDB, using the DAP as our guiding framework.
Through this endeavor, this project proposes to develop a greater interoperability
and streamlining of the debugging process, further solidifying the Debug Adapter
Protocol’s place as a means to facilitate efficient debugging in software development
tooling.

2023 INFO 4001 12CP Research Thesis Project
