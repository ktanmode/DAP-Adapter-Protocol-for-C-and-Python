# Command required to run gdb dap server

gdb -ex "source DapGdbClient.py"

### To compile a file with debugging capability using gcc (GNU Compiler Collection) for the C/C++ language, you can use the -g flag. The -g flag tells gcc to generate debug information to be used with debugging tools like GDB (GNU Debugger).

This is required for files to be able to be debugged with maximum compatibility

gcc -g example.c -o example
