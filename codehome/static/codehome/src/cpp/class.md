# C++ Standard Class

## Table of Contents

## Review

### Quiz

In the last tutorial, we introduced the idea of a C++ reference. What is the output of this code?

```cpp
void mystery(int& b, int c, int& a) { 
    a++;
    b--;
    c += a; 
}

int main() { 
    int a = 5; 
    int b = 2;
    int c = 8;
    mystery(c, a, b);
    cout << a << " " << b << " " << c << endl;
    return 0;
}
```

Poll:

```cpp
A. 5 2 8
B. 5 3 7
C. 6 1 8 
D. 61 13 
E. other
```

Poll answer:

```cpp
B. 5 3 7
```

### Solving the Quadratic Equation

Let's write a function for solving the quadratic equation.

A quadratic equation for variable x is one of the form:

ax^2 + bx + c = 0

- The two roots of a quadratic equation can be found using the quadratic formula as follows, ![quadratic-formula]({% static 'codehome/src/img/cpp/quadratic-formula.png' %})
- Example: The roots of **x^2 - 3x - 4 = 0** are **x=4** and **x=-1**
- How would we write a function named quadratic to solve quadratic equations?
    - What parameters should it accept?
    - Which parameters should be passed by value, and which by reference?
    - What, if anything, should it return?

```cpp
/*
 * Solves a quadratic equation ax^2 + bx + c = 0,
 * storing the results in output parameters root1 and root2. 
 * Assumes that the given equation has two real roots.
 */
void quadratic(double a, double b, double c,
               double& root1, double& root2) {
    double d = sqrt(b * b - 4 * a * c);
    root1 = (-b + d) / (2 * a);
    root2 = (-b - d) / (2 * a);
}
```

However, what other choices could we have made?

## Vector

### Intuition on Vector

What is a **Vector**?

- It is like a **list** in Python, or an **ArrayList** in Java.
- It is a list of elements that can grow and shrink.
- Each element has a place (or index) in the list.

Important Details

- The constructor creates an empty list (more on constructors soon)
- The Stanford **Vector** class performs bounds checks, meaning that if you try to access an element that is outside the bounds of a **Vector**, the program crashes.
- A **Vector** Knows its size.
- To use **Vectors**, you `#include "vector.h"`.

Under the hood, a vector is an array, which means that in the computer's memory, one value follows the next.

### Creating a Vector

You must specify the type of your vector (e.g., **int**, **string**, etc.)

When a vector is created it is initially empty.

To create a vector called **vec** that can hold integers (**ints**), we write the following:

```cpp
Vector<int> vec; 
```

This calls the default constructor, which just means that it initializes and creates (constructs) an empty vector for us.

### Adding Elements to A Vector

Here is an example where we create a vector called **magic** and add the numbers **4**, **8**, **15**, and **16** to the vector, and then print out the element at index **2**:

```cpp
Vector<int> magic;
magic.add(4);
magic.add(8);
magic.add(15);
magic.add(16);
cout << magic[2] << endl;
```

Output:

```cpp
15
```

Notice that the index ordering starts from **zero**!

In the computer's memory, our vector is represented by one number after another, as follows:

```cpp
magic:
index:	0 	1 	2 	3 
value:	4	8	15	16
```

Vectors have useful functions, like `size()`

The following loops through the values in the vector and prints them:

```cpp
for(int i = 0; i < magic.size(); i++) {
 cout << magic[i] << endl;
}
```

Output:

```cpp
4
8
15
16
```

### Another for Loop: the for each Loop

The following is a loop that automatically gets the next value in a collection,

```cpp
for(int value : magic) {
 cout << value << endl;
}
```

Output:

```cpp
4
8
15
16
```

### Vector Functions

The following functions are part of the vector collection, and can be useful:

- `vec.size()`: Returns the number of elements in the vector.
- `isEmpty()`: Returns true if the vector is empty, false otherwise.
- `vec[i]`: Selects the ith element of the vector.
- `vec.add(value)`: Adds a new element to the end of the vector.
- `vec.insert(index, value)`: Inserts the value before the specified index, and moves the values after it up by one index.
- `vec.remove(index)`: Removes the element at the specified index, and moves the rest of the elements down by one index.
- `vec.clear()`: Removes all elements from the vector.

For the exhaustive list, check out the [Stanford Vector class](https://web.stanford.edu/dept/cs_edu/cppdoc/Vector-class.html)

## The Grid Container

![matrix]({% static 'codehome/src/img/cpp/matrix.png' %})

The **Grid** is a Stanford library class for 2-dimensional arrays, like a matrix in math:

```cpp
a0	b0	c0
a1	b1	c1
a2	b2	c2
```

### Intuition on Grid

What is it?

- Advanced 2D array.
- Think spread sheets, game boards

Important Details

- Default constructor makes a grid of size 0
- Doesn’t support “ragged right”.
- Bounds checks
- Knows its size.

We could use a combination of Vectors to simulate a 2D matrix, but a Grid is easier!

### Grid Example Code

```cpp
Grid<int> matrix(2,2); 
matrix[0][0] = 42;
matrix[0][1] = 6;
matrix[1][0] = matrix[0][1];
cout << matrix.numRows() << endl;
cout << matrix[0][1] << endl;
cout << matrix[1][1] << endl;
cout << matrix[2][3] << endl;
```

Let's draw what happens on each line.

```cpp
Grid<int> matrix(2,2); // Create a 2x2 grid, with 0 as the default entries

	0	1
0	0	0
1	0	0
```

```cpp
matrix[0][0] = 42; // put 42 at row 0, column 0

    0	1
0	42	0
1	0	0
```

```cpp
matrix[0][1] = 6; // put 6 at row 0, column 1

    0	1
0	42	6
1	0	0
```

```cpp
matrix[1][0] = matrix[0][1]; // put the value from r0,c1 at r1,c0

	0	1
0	42	6
1	6	0
```

```cpp
cout << matrix.numRows() << endl;
cout << matrix[0][1] << endl;
cout << matrix[1][1] << endl;
```

Prints the number of rows, then the value at r0,c1, then the value at r1,c1:

```cpp
2
6
0
```

```cpp
cout << matrix[2][3] << endl; // attempts to print out the value at r2,c3

***
*** STANFORD C++ LIBRARY 
*** An ErrorException occurred during program execution: 
*** Grid::operator [][]: (2, 3) is outside of valid range [(0, 0)..(1, 1)]
***
libc++abi.dylib: terminate_handler unexpectedly threw an exception
15:25:55: The program has unexpectedly finished.
15:25:55: The process was ended forcefully.
```

Grids do bounds checking! If you want to bounds check without crashing, you should call the `grid.inBounds(row, col)` function, which returns true if the row and column are in bounds for the grid.

### Grid Functions

The following functions are part of the grid collection, and can be useful:

- `grid.numRows()`: Returns the number of rows in the grid.
- `grid.numCols()`: Returns the number of columns in the grid.
- `grid[i][j]`: selects the element in the ith row and jth column.
- `grid.resize(rows, cols)`: Changes the dimensions of the grid and re-initializes all entries to their default values.
- `grid.inBounds(row, col)`: Returns true if the specified row, column position is in the grid, false otherwise.

For the exhaustive list, check out the [Stanford Grid class](https://web.stanford.edu/dept/cs_edu/cppdoc/Grid-class.html)

### Grid Example: Traversing a Grid

```cpp
void printGrid(Grid<char> &grid) {
    for(int r = 0; r < grid.numRows(); r++) {
        for(int c = 0; c < grid.numCols(); c++) {
            cout << grid[r][c];
        }
        cout << endl;
    }
}
```

If we pass in the following grid, what will print?

```cpp
    0	1
0	a	b
1	c	d
2	e	f
```

Output:

```cpp
ab
cd
ef
```
### Common Pitfalls When Working with Collections in C++

- `Vector numbers;`
    - Needs a type! Should be: `Vector<int> numbers;`
- `void myFunction(Grid<bool> gridParam);`
    - Two issues:
        - If you want the original `gridParam` to be changed in the calling function, you're out of luck.
        - Inefficient because you have to make a copy of `gridParam`.

## Stacks

We are about to discuss two new containers in which to store our data: the **stack** and **queue** containers. These are also known as *abstract data types*, meaning that we are defining the interface for a container, and how it is actually implemented under the hood is not of our concern (at this point!)

An *abstract data type* is defined by its behavior from the point of view of the user of the data, and by the operations it can accomplish with the data.

The stack and queue containers have similar interfaces, but they are used for very different problems, as we shall see.

### Intuition on Stack

A stack is an abstract data type with the following behaviors / functions:

- `push(value)` (or `add(value)`) - place an entity onto the top of the stack
- `pop()` (or `remove()`) - remove an entity from the top of the stack and return it
- `top()` (or `peek()`) - look at the entity at the top of the stack, but don’t remove it
- `isEmpty()` - a boolean value, true if the stack is empty, false if it has at least one element. (note: a runtime error occurs if a pop() or top() operation is attempted on an empty stack.)

Why do we call it a stack? Because we model it using a stack of things:

![stack]({% static 'codehome/src/img/cpp/stack.png' %})

The **push**, **pop**, and **top** operations are the only operations allowed by the stack ADT, and as such, only the top element is accessible. Therefore, a stack is a Last-In-First-Out (LIFO) structure: the last item in is the first one out of a stack.

Despite the stack’s limitations (and indeed, because of them), the stack is a very frequently used ADT. In fact, most computer architectures implement a stack at the very core of their instruction sets – both push and pop are assembly code instructions.

Stack operations are so useful that there is a stack built in to every program running on your PC — the stack is a memory block that gets used to store the state of memory when a function is called, and to restore it when a function returns.

Why are stacks used when functions are called?

- Let's say we had a program like this: ![function-calls]({% static 'codehome/src/img/cpp/function-calls.png' %})
- `main` calls `function1`, which calls `function2`, which calls `function3`.
- First, `function3` returns, then `function2` returns, then `function1` returns, then `main` returns.
- This is a LIFO pattern! ![function-stack]({% static 'codehome/src/img/cpp/function-stack.png' %})

### Stacks: Tradeoffs

What are some downsides to using a stack?

- No random access. You get the top, or nothing.
- No walking through the stack at all — you can only reach an - element by popping all the elements higher up off first
- No searching through a stack.

What are some benefits to using a stack?

- Useful for lots of problems – many real-world problems can be solved with a Last-In-First-Out model (we'll see one in a minute)
- Very easy to build one from an array such that access is guaranteed to be fast.
- Where would you have the top of the stack if you built one using a Vector? Why would that be fast?

### Reversing the words in a sentence

Let's build a program from scratch that reverses the words in a sentence.

Goal: reverse the words in a sentence that has no punctuation other than letters and spaces.

1. Use a stack
2. Read characters in a string and place them in a new word.
3. When we get to a space, push that word onto the stack, and reset the word to be empty.
4. Repeat until we have put all the words into the stack.
5. Pop the words from the stack one at a time and print them out.

```cpp
#include <iostream>
#include "console.h"
#include "stack.h"

using namespace std;
const char SPACE = ' ';

int main() {
    string sentence = "hope is what defines humanity";
    string word;
    Stack<string> wordStack;

    cout << "Original sentence: " << sentence << endl;

    for (char c : sentence) {
       if (c == SPACE) {
           wordStack.push(word);
           word = ""; // reset
       } else {
           word += c;
       }
    }
    if (word != "") {
        wordStack.push(word);
    }

    cout << "     New sentence: ";
    while (!wordStack.isEmpty()) {
        word = wordStack.pop();
        cout << word << SPACE;
    }
    cout << endl;

    return 0;
}
```

Output:

```cpp
Original sentence: hope is what defines humanity
     New sentence: humanity defines what is hope
```

## Queues

### Intuition on Queue

The next ADT we are going to talk about is a queue. A queue is similar to a stack, except that (much like a real queue/line), it follows a "First-In-First-Out" (FIFO) model:

![queue]({% static 'codehome/src/img/cpp/function-stack.png' %})

- The first person in line is the first person served.
- The last person in line is the last person served.
- Insertion into a queue `enqueue()` is done at the back of the queue, and removal from a queue `dequeue()` is done at the front of the queue.

### Member Functions

Like the stack, the queue Abstract Data Type can be implemented in many ways (we will talk about some later!). A queue must implement at least the following functions:

- `enqueue(value)` (or `add(value)`) - place an entity onto the back of the queue
- `dequeue()` (or `remove()`) - remove an entity from the front of the queue and return it
- `front()` (or `peek()`) - look at the entity at the front of the queue, but don’t remove it
- `isEmpty()` - a boolean value, **true** if the queue is empty, **false** if it has at least one element. (note: a runtime error occurs if a `dequeue()` or `front()` operation is attempted on an empty queue).

Please look at the Stanford Library Queue reference for other functions (e.g., there is a `back()` function that is analogous to `front()` for the back of the queue – but no removing the value!)

Examples:

```cpp
Queue<int> q;                // {}, empty queue
q.enqueue(42);               // {42}
q.enqueue(-3);               // {42, -3}
q.enqueue(17);               // {42, -3, 17}
cout << q.dequeue() << endl; // 42 (q is {-3, 17})
cout << q.front() << endl;   // -3 (q is {-3, 17})
cout << q.dequeue() << endl; // -3 (q is {17})
```

### Queue Examples

Both the Stanford Stack and Queue classes have a size() function that returns the number of elements in the object.

What is the output of the following code?

```cpp
 Queue<int> queue;
 // produce: {1, 2, 3, 4, 5, 6}
 for (int i = 1; i <= 6; i++) {
     queue.enqueue(i);
 }
 for (int i = 0; i < queue.size(); i++) {
     cout << queue.dequeue() << " ";
 }
 cout << queue.toString() << "  size " << queue.size() << endl;
```

Answer:

```cpp
1 2 3 {4,5,6} size 3
```

Reason: watch out! `queue.size()` changes while the loop runs! You have to be careful when looping and also checking the size of your container.

### Queue Idiom

If you are going to empty a stack or queue, a very good programming idiom is the following:

```cpp
Queue<int> queueIdiom1;
// produce: {1, 2, 3, 4, 5, 6}
for (int i = 1; i <= 6; i++) {
  queueIdiom1.enqueue(i);
}
while (!queueIdiom1.isEmpty()) {
  cout << queueIdiom1.dequeue() << " ";
}
cout << queueIdiom1.toString()
   << "  size " << queueIdiom1.size() << endl;
```

Output:

```cpp
1 2 3 4 5 6 { } size 0
```

If you are going to go through a stack or queue once for the original values, a very good programming idiom is the following, which calculates the size of the queue only once:

```cpp
Queue<int> queueIdiom2;
  for (int i = 0; i < 6; i++) {
      queueIdiom2.enqueue(i + 1);
  }
   
  //  do NOT put queue.size() in for loop, to avoid calling repeatedly 
  int origQSize = queueIdiom2.size();
  for (int i=0; i < origQSize; i++) {
     int value = queueIdiom2.dequeue();
     cout << value << " ";
     // re-enqueue even values
     if (value % 2 == 0) {
        queueIdiom2.enqueue(value);
     }
  }
  cout << endl;
  cout << queueIdiom2 << endl;
```

Output:

```cpp
1 2 3 4 5 6
{2, 4, 6}
```

There will still be three values left in the queue `(2, 4, 6)`, but we only looped through the queue for the original values.

### More Advanced Stack Example: Postfix

When you were first learning algebraic expressions, your teacher probably gave you a problem like this, and said, "What is the result?"

`5 * 4 - 8 / 2 + 9`

The class got all sorts of different answers, because no one knew the order of operations yet (the correct answer is 25, by the way). Parenthesis become necessary as well (e.g., `10 / (8-3)`).

This is a somewhat annoying problem — it would be nice if there were a better way to do arithmetic so we didn't have to worry about order of operations and parenthesis.

As it turns out, there is a "better" way! We can use a system of arithmetic called "postfix" notation — the expression above would become the following:

`5 4 * 8 2 / - 9 +`  Wat?

Postfix notation* works like this: Operands (the numbers) come first, followed by an operator (`+`, `-`, `*`, `/`, etc.). When an operator is read in, it uses the previous operands to perform the calculation, depending on how many are needed (most of the time it is two).

So, to multiply 5 and 4 in postfix, the postfix is `5 4 *` To divide 8 by 2, it is `8 2 /`

There is a simple and clever method using a stack to perform arithmetic on a postfix expression:

1. Read the input and push numbers onto a stack until you reach an operator.
2. When you see an operator, apply the operator to the two numbers that are popped from the stack.
3. Push the resulting value back onto the stack.
4. When the input is complete, the value left on the stack is the result.

> *Postfix notation is also called "Reverse Polish Notation" (RPN) because in the 1920s a Polish logician named Jan Łukasiewicz invented "prefix" notation, and postfix is the opposite of postfix, and therefore so-called "Reverse Polish Notation"

```cpp
// Postfix arithmetic, implementing +, -, *, /

#include <iostream>
#include "console.h"
#include "simpio.h"
#include "stack.h"

using namespace std;

const string OPERATORS = "+-*x/";
const string SEPARATOR = " ";

// function prototypes
double parsePostfix(string expression);
string getNextToken(string &expression);
void performCalculation(Stack<double> &s, char op);

// Postfix arithmetic, implementing +, -, *, /

#include <iostream>
#include "console.h"
#include "simpio.h"
#include "stack.h"

using namespace std;

const string OPERATORS = "+-*x/";
const string SEPARATOR = " ";

// function prototypes
double parsePostfix(string expression);
string getNextToken(string &expression);
void performCalculation(Stack<double> &s, char op);

int main() {
    string expression;
    double answer;
    do {
        expression = getLine("Please enter a postfix expression (blank to quit): ");
        answer = parsePostfix(expression);
        cout << "The answer is: " << answer << endl << endl;
    } while (expression != "");
    return 0;
}

int main() {
    string expression;
    double answer;
    do {
        expression = getLine("Please enter a postfix expression (blank to quit): ");
        if (expression == "") {
            break;
        }
        answer = parsePostfix(expression);
        cout << "The answer is: " << answer << endl << endl;
    } while (true);
    return 0;
}

string getNextToken(string &expression) {
    // pull out the substring up to the first space
    // and return the token, removing it from the expression

    string token;
    int sepLoc = expression.find(SEPARATOR);
    if (sepLoc != (int) string::npos) {
        token = expression.substr(0,sepLoc);
        expression = expression.substr(sepLoc+1,expression.size()-sepLoc);
        return token;
    }
    else {
        token = expression;
        expression = "";
        return token;
    }
}

double parsePostfix(string expression) {
    Stack<double> s;
    string nextToken;
    
    while (expression != "") {
        // gets the next token and removes it from expression
        nextToken = getNextToken(expression);
        if (OPERATORS.find(nextToken) == string::npos) {
            // we have a number
            double operand = stringToDouble(nextToken);
            s.push(operand);
        }
        else {
            // we have an operator
            char op = stringToChar(nextToken);
            performCalculation(s,op);
        }
    }
    return s.pop();
}

void performCalculation(Stack<double> &s, char op) {
    double result;
    double operand2 = s.pop(); // LIFO!
    double operand1 = s.pop();
    switch(op) {
        case '+': result = operand1 + operand2;
            break;
        case '-': result = operand1 - operand2;
            break;
            // allow "*" or "x" for times
        case '*':
        case 'x': result = operand1 * operand2;
            break;
        case '/': result = operand1 / operand2;
            break;
    }
    s.push(result);
}
```

Example run:

```cpp
Please enter a postfix expression (blank to quit): 5 4 * 8 2 / - 9 +
The answer is: 25

Please enter a postfix expression (blank to quit): 1 2 3 4 + + +
The answer is: 10
 
Please enter a postfix expression (blank to quit): 1 2 3 4 - - -
The answer is: -2
 
Please enter a postfix expression (blank to quit): 1 2 + 3 * 6 + 2 3 + /
The answer is: 3 

Please enter a postfix expression (blank to quit): 2 3 4 + * 6 - 
The answer is: 8 
```

**World's First Programmable Desktop Computer**

The HP 9100A Desktop Calculator: the world’s first programmable scientific desktop computer — really, the first desktop computer. (Wired, Dec. 2000)

![hp-9100A]({% static 'codehome/src/img/cpp/hp-9100A.png')

- RPN (postfix)
- Special algorithm for trigonometric and logarithmic functions
- Cost $5000 in 1968 ($37,000 today)
