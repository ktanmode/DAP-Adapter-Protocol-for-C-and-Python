# 2023 INFO 4001 12CP Research Thesis Project
## Creating a DAP-Compatible Debug Adapter between Binaries and Debuggers.

Software development, in its various stages, involves the rigorous process and cycle of writing code, testing, and debugging. As the development cycle evolves, the need for debugging tools to communicate seamlessly with the programs or binaries becomes paramount. The software becomes more diverse and complex, and the extensibility of debuggers may either not exist or not be sufficient enough to keep up with new development ecosystems.

> **Abstract:**  
> This thesis delves into the Debug Adapter Protocol (DAP), an approach designed to unify the communication between development tools, IDE, and various debuggers. It aims to help programmers have a consistent debugging experience across these diverse environments without having to learn the intricacies of each debugger.

### **Primary Focus:**
Our primary focus is the crucial role of the Debug Adapter, an intermediary component that bridges the gap between existing debuggers and various binaries or development tools through the DAP. Expecting a complete adoption of DAP by existing debuggers is still very unlikely, as they require significant modification to the individual debugger. 

Through this protocol, the thesis examines how the introduction of such an intermediary reduces the effort to integrate a new debugger, offering a significant universal entry point for tools such as different IDEs to interact with debuggers while maintaining its extensibility.

### **Wire-Protocol & Language Flexibility:**
By adopting a wire-protocol through a JSON-RPC communication protocol, the DAP offers flexibility in the language choice for the debug adapter implementation, catering to the nuances of specific debuggers. Despite its high-level design, which abstracts many of the underlying debugger intricacies, the DAP ensures that users can send requests and receive comprehensive responses from the debugger.

### **Project Aim:**
This project aims to build upon the DAP concept, specifically targeting binaries produced by languages like C. It addresses the challenges and intricacies of creating a debug adapter capable of translating between programs and binary executables and the corresponding debugger, such as GDB. The DAP serves as our guiding framework in this endeavor.

### **Objectives:**
- Develop greater interoperability and streamline the debugging process.
- Solidify the Debug Adapter Protocol’s place as a means to facilitate efficient debugging in software development tooling.

### **Concluding Remarks:**
The approach proposed in this project fosters a harmonious interaction between different development tools, debuggers, and IDEs, promoting a unified, streamlined, and more efficient software development process, enriched by the benefits of the Debug Adapter Protocol.

---

_**2023 INFO 4001 12CP Research Thesis Project**_
