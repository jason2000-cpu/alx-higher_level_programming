## 0x05-Python-Exceptions

Exceptions are errors detected during execution and are not unconditionally fatal:
#### Examples include;
- ZeroDivisionalError (dividing by zero)
- TypeError (inappropriate data type)
- IndexError (index out of range)
- NameError (occurs when you try to use a variable, function, or module that doesn't exist or wasn't used in a valid way)
- ValueError ( occurs when a function receives an argument of the correct data type but an inappropriate value)
- RuntimeError (happens when Python understands what you are saying, but runs into trouble when following your instructions)

### Syntax
       try:
          //code to execute  when no errror
        except  <typeoferror>:
           //code to excecute  in the occurence of the error