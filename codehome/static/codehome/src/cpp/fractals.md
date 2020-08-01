# Fractals

## Table of Contents
- [Review about Recursion][1]
- [More Example in Google][2]
	- [Anatomy of a mathematical expression][3]
- [Fractals][4]
	- [The Cantor Fractal][5]
	- [Snowflake Fractal][6]


## Review about Recursion

The **base case** represents the simplest possible instance of the problem you are solving.

- Example: How many people are behind you, including you? Answer? 1, it's just me!
- Example: What is x^n? Answer: x^0 = 1
- Solve the Towers of Hanoi Answer: 1 ring is easy!

The **recursive case** represents how you can break down the problem into smaller instances of the same problem.

- Example: How many people are behind you, including you? Answer? 1 + the number behind me.
- Example: What is x^n? Answer: x * x^(n-1).
- Solve the Towers of Hanoi Answer: N-1 disks to aux, 1 disk to target, N-1 disks to target.

## More Example in Google

![google-math2](codehome/src/img/cpp/google-math2.png)

Google can do arithmetic: `((1*17)+(2*(3+(4*9)))) = 95`

But, how? Implement a function which evaluates an expression string:

- `((1+3)*(2*(4+1)))`
- `(7+6)`
- `(((4*(1+2))+6)*7)`

note: only needs to implement + and *

### Anatomy of a mathematical expression

An expression is always one of these three things:

- a number
- (an expression + an expression)
- (an expression * an expression)

For example: `((1*3)+(4*2))`

- There is an expression on the left, `(1*3)`
    - This expression is made up of a number * a number (and a number is also an expression)
- There is a joining operator, `+`
- There is an expression on the right, `2*4`
    - This expression is made up of a number * a number (and a number is also an expression)

The two smaller expressions with the `+` joining operator make up an expression, as well.

How do we evaluate `((1*17)+(2*(3+(4*9))))`?

![full-calculation-tree](codehome/src/img/cpp/full-calculation-tree.png)

First, we break each expression up into its component parts, and when we get to an expression with just numbers, we calculate those results. We have the + separating the two main expressions, `(1*17)` and `(2*(3+(4*9)))`.

Next, we start looking at the sub-expressions. The `(1*17)` has two numbers, so can evaluate the product, to get 17. The `(2*(3+(4*9)))` has a number, 2 and another expression, `3+(4*9)`. So, we have to evaluate the non-number first.

- We look at `(3+(4*9))` and see that it has a number, `3` and an expression, `4*9`, so we have to look at the expression first.
    - `4*9` has just numbers, so we can calculate the product, to get 36. Now we can back up, because we have a number for the previous expression.
- We can calculate `(3+36)` to get 39, and we can move up.

We can calculate `(2*39)` to get 78, and we can move up.

Finally, we can calculate 17+78 to get 95.

Is it recursive? Yes!

Take a look at `((1*3)+(4+2))`

- The big instance of this problem is the whole problem, and the smaller instances are the numbers, `1`, `3`, `4`, and `2`.

So, we can write a recursive function:

- `int evaluate(string exp); // "((1*3)+(4+2)) returns 9`
- We can use the library functions:
    - `stringIsInteger(exp)`
    - `stringToInteger(exp)`
- And we can use a couple of helper functions:
    - `char op = getOperator(exp); // returns '+' or '*'`
    - `string left = getLeftExp(exp); // returns "(1*3)"`
    - `string right = getRightExp(exp); // returns "(4+2)"`

##### Solution in PseudoCode

int evaluate(expression):

- if expression is a number, return expression
- Otherwise, break up expression by its operator:
    - leftResult = evaluate(leftExpression)
    - rightResult = evaluate(rightExpression)
    - return leftResult operator rightResult

The solution:

```cpp
int evaluate(string exp) {
    // base case
    if (stringIsInteger(exp)) {
        return stringToInteger(exp);
    } else {
        char op = getOperator(exp);
        string left = getLeftExp(exp);
        string right = getRightExp(exp);

        // recursive case #1
        int leftResult = evaluate(left);

        // recursive case #2 (!)
        int rightResult = evaluate(right);

        if (op == '+') {
            return leftResult + rightResult;
        } else {
            return leftResult * rightResult;
        }
    }
}
```

Helper function:

```cpp
int getOppIndex(string exp){
    int parens = 0; 
    // ignore first left paren
    for (int i = 1; i < exp.length(); i++) {
        char c = exp[i];
        if (c == '(') {
            parens++;
        } else if (c == ')') {
            parens--;
        }
        if (parens == 0 && (c == '+' || c == '*')) {
            return i;
        }
    }
    return -1;
}
```

## Fractals

A *fractal* is a recurring graphical pattern. Smaller instances of the same shape or pattern occur within the pattern itself.

![fractal-examples](codehome/src/img/cpp/fractal-examples.png)

##### Fractal Examples in Nature

![fractal-examples-in-nature](codehome/src/img/cpp/fractal-examples-in-nature.png)

Many natural phenomena generate fractal patterns:

- earthquake fault lines
- animal color patterns
- clouds
- mountain ranges
- snowflakes
- crystals
- coastlines
- DNA

### The Cantor Fractal

We can create many fractals programmatically, and because fractals are self-similar, we can do so recursively!

The first fractal we will code is called the "Cantor" fractal, named after the late-19th century German mathematician Georg Cantor.

![arm-cantor](codehome/src/img/cpp/arm-cantor.png)

- The Cantor fractal is a set of lines (indeed, a "Cantor Set" of lines) where there is one main line, and below that there are two other lines, each 1/3rd of the width of the original line, one on the left, and one on the right (with a 1/3 separation of white space between them)
- Below each of the other lines is an identical situation: two 1/3rd lines.
- This repeats until the lines are no longer visible.

![cantor-fractal1](codehome/src/img/cpp/cantor-fractal1.png)

In text, a 4-level Cantor fractal would look like this:

```cpp
---------------------------
---------         ---------
---   ---         ---   ---
- -   - -         - -   - -
```

Parts of a cantor set image … are Cantor set images!

![cantor-fractal2](codehome/src/img/cpp/cantor-fractal2.png)

- The Cantor fractal above has six levels.
- Every individual line segment is its own 1-level Cantor fractal

##### How to draw a level n Cantor fractal

![level-n-cantor](codehome/src/img/cpp/level-n-cantor.png)

1. Draw a line from start to finish.
2. Underneath, on the left third, draw a Cantor of size **n - 1**.
3. Underneath, on the right third, draw a Cantor of size **n - 1**.

Then we can use auxiliary tools for drawing lines in the process of accomplishing cantor fractal with C++.

### Snowflake Fractal

![snowflake-fractal](codehome/src/img/cpp/snowflake-fractal.png)

Let's break this down to a smaller part,

![partial-snowflake-fractal](codehome/src/img/cpp/partial-snowflake-fractal.png)

Depth 1 Snowflake: A line,

![level-1-snowflake](codehome/src/img/cpp/level-1-snowflake.png)

Depth 2 Snowflake: The line has a triangle break,

![level-2-snowflake](codehome/src/img/cpp/level-2-snowflake.png)

Depth 3 Snowflake: In progress,

![level-3-snowflake1](codehome/src/img/cpp/level-3-snowflake1.png)

Depth 3 Snowflake: In progress,

![level-3-snowflake2](codehome/src/img/cpp/level-3-snowflake2.png)

Depth 3 Snowflake: Finished,

![level-3-snowflake3](codehome/src/img/cpp/level-3-snowflake3.png)

<EndMarkdown>
[1]: #review-about-recursion
[2]: #more-example-in-google
[3]: #anatomy-of-a-mathematical-expression
[4]: #fractals
[5]: #the-cantor-fractal
[6]: #snowflake-fractal
