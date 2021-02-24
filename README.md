<div align="center">
  <img src="assets/images/Caesium logo.png" >
  <br>
  <br>
  <br>
</div>

A: "Finally Python is more functional!"
<br>
<br>
B: "No it's not."
<br>
<br>
A: "Oh, wait..." 
<br>
<br>
B: "Look at the name."
<br>
<br>
A & B: "This isn't Python; it's..."

# Caesium (C##/Cx/C++++++)
Caesium (pronounced see-zi-um)

NOUN

1. The chemical element of atomic number 55, a soft, silvery, extremely reactive metal. It belongs to the alkali metal group and occurs as a trace element in some rocks and minerals.

2. The programming language that mixes Python's readability with C's functionality. The language that made Python functional with Python.
------

Caesium is 2 things:

1. My favourite element of the periodic table because it is highly flammable and explosive

2. My first independent programming language 😀

Ok, so it's not that much of a big deal as I am designing Caesium with one main goal in mind: I am going to use it to make other languages.

-----

## To-Do
### Lexer
- [ ] Add a load of other characters (@, £, $, %, ~, #...)
- [ ] Regex expression Lexing

### Parser
- [x] Fix exprlevel4() to accept negative numbers
- [ ] Add strings and other datatypes

### Compiler, Interpreter and Builtins
- [x] Start Interpreter
- [x] Start Builtins
- [x] Change Interpreter to support Builtins

### Rules
- [ ] Change DEFAULT_PROGRAM_TOKENS to tokens instead of dictionaries and functional instead of object-oriented and actually use them somewhere

If you will like to help me with any of this, for the repo and submit a pull request! I can always use some help. 😏


## Syntax

### Core syntax

Caesium has many core features of most programming languages and they are mentioned here:

- Print, Input and Error:

  Caesium has features to deal with stdout, stdin and stderr:

      void func main() {
              console.stdout("Hi");
              str a = console.stdin("How are you? ");
              console.stderr(CaeError, "This is an error.");
      }

- Variable definition:

  Caesium, like most programming languages has statements to add things to memory:

      void func main() {
              str a = "Hi";
              int s = 5;
              float:
                      x = 2.3
                      d = 1.4
                      pi = 3.14
              list w = [5, 2, 3, 4], q = [];
      }

### Quirks and extra features

Caesium has a few quirks in its syntax that should be learned even before the first release is out:

- Unary ops -- In Caesium, Unary operators are written in threes:

    In Python
    
        print(+2, -2)
    
    Caesium equivalent

        void func main(){
              console.stdout(+++2, ---2);
        }
              
    <p style="color:red"> Both will print positive 2 and negative 2 to the console. <p>

- Object definition -- In Caesium, custom object definitions are simply put as follows:

  In Python

      class Example:
              def __init__(self):
                      print("Example")
      a: Example = Example()

  Caesium Equivalent

      type Example {
              void method init(self) {
                      console.stdout("Example");
              }
      }
      void func main() {
              object a = new Example();
      }

    <p style="color:red"> Both will print "Example" to the console<p>

- Actions -- Now, I wouldn't really consider this a quirk but it's worth mentioning:

  In Python

      def a(b: int, c: int):
              print(b+c)
      def example():
              a(2, 3)
      example()

  Caesium Equivalent

      void func a(int b, str c) {
              console.stdout(b+c);
      }

      void func main() {
              action example = new Action(a(b=2, c=3));
              example();
      }
    
    <p style="color:red"> Both will print positive 5 to the console<p>
                      

-----

## Credits
<br>
There are a few repositories that I got the structure from and they are listed here.
<br>
<br>

- [davidcallanan/py-myopl-code](https://github.com/davidcallanan/py-myopl-code) -- Interpreter and builtins
- [nguyenphuminh/Jellyscript](https://github.com/nguyenphuminh/Jellyscript) -- Caesium logo display on readme
