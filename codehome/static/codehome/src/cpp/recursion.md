# Introduction to Recursion

## Table of Contents
- [Introduction to Recursion][1]
	- [Towers of Hanoi][2]
	- [What is Recursion][3]
	- [Why Recursion][4]
	- [Recursion in Programming][5]
- [Recursion World][6]
	- [Recursion in Real Life][7]
	- [Counting a column of people][8]
	- [Recursive Structure][9]
	- [Recursive Functions][10]
	- [The Three "Musts" of Recursion][11]
		- [The "Recursive Leap of Faith"][12]
- [Recursion Practices][13]
	- [The power(x, n) function][14]
	- [Big O of power(x, n)?][15]
	- [Faster power function!][16]
	- [Mystery Recursion: Trace this function][17]
	- [isPalindrome(string s)][18]
	- [Back to the Towers of Hanoi][19]
- [Recursion Recap][20]


## Introduction to Recursion

![recursion-recursion](codehome/src/img/cpp/recursion-recursion.png)

Recursion is everywhere in our world.

### Towers of Hanoi

Here is the way the game is played,

![Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi](codehome/src/img/cpp/Iterative_algorithm_solving_a_6_disks_Tower_of_Hanoi.gif)

### What is Recursion

Recursion is: A problem solving technique in which problems are solved by reducing them to smaller problems of the same form.

### Why Recursion

- Great style
- Powerful tool
- Master of control flow

### Recursion in Programming

In programming, recursion simply means that a function will call itself:

```cpp
int main() {
 main();
 return 0;
}
```

`main()` isn't supposed to call itself, but if we do write this program, what happens?

We'll get back to programming in a moment!

## Recursion World

### Recursion in Real Life

![hard-jigsaw-puzzle](codehome/src/img/cpp/hard-jigsaw-puzzle.png)

How to solve a jigsaw puzzle recursively ("solve the puzzle")

- Is the puzzle finished? If so, stop.
- Find a correct puzzle piece and place it.
- Solve the puzzle

### Counting a column of people

Let's pretend we have a column of people, one behind the other. Let's try counting the people by only allowing them to ask questions of the people directly behind them and respond to questions to the people directly in front of them. In other words, we have the following rules:

1. A person can see only the people directly in front and behind them. So, they can't just look back and count.
2. A person is allowed to ask questions of the person behind them, and respond to the person in front of them.

How can we solve this problem recursively?

Answer:

1. The first person looks behind them, and sees if there is a person there. If there is, they ask them how many people are in line, including them, and wait for a response. If there isn't anyone, the person responds "1", and we are done counting.

2. If there is a person, that person repeats step 1, and waits for a response.

3. Once a person receives a response (a number), they add 1 for themselves, and they respond to the person that asked them.

##### Counting a column of people recursively in C++

```cpp
int numPeopleInLine(Person curr) {
    if (noOneBehind(curr)) {
        return 1;
    } else {
        Person personBehind = curr.getBehind();
        return numPeopleInLine(personBehind) + 1; // recursive call!
    }
}
```

Notice that eventually, a person will look behind them and see that there isn't anyone there. That person responds "1", which gets returned to the second-to-last person, who adds 1 to 1, and responds "2". This gets returned to the third-to-last person, who adds 1 to 2, and responds "3". This keeps happening all the way to the first person, who adds "1" and now has a complete count of the number of people in line.

### Recursive Structure

The structure of a recursive function is typically like the following:

```cpp
returnValue recursiveFunction(parameter) {
  if (test for simple case) {
     Compute the solution without recursion
  } else {
     Break the problem into a subproblem of the same form, where "parameter" becomes "newParameter"
     Call recursiveFunction(newParameter)
     Get the result of the subproblem, update and return
  }
}
```

### Recursive Functions

Every recursive algorithm involves at least two cases:

- base case: The simple case; an occurrence that can be answered directly; the case that recursive calls reduce to.
- recursive case: a more complex occurrence of the problem that cannot be directly answered, but can be described in terms of smaller occurrences of the same problem.

```cpp
int numPeopleInLine(Person curr) {
    // base case
    if (noOneBehind(curr)) {
        return 1;
    } else {
        // recursive case
        Person personBehind = curr.getBehind();
        return numPeopleInLine(personBehind) + 1; // recursive call!
    }
}
```

### The Three "Musts" of Recursion

- Your code must have a case for all valid inputs.
- You must have a base case that makes not recursive calls.
- When you make a recursive call it should be to a simpler instance of the same problem, and make forward progress towards the base case.

#### The "Recursive Leap of Faith"

![leap-of-faith](codehome/src/img/cpp/leap-of-faith.png)

You must trust that your recursion will proceed as you have designed it – this is hard to do when you first start coding recursively!

## Recursion Practices

The first real recursion problem we will tackle is a function to raise a number to a power. Specifically, we are going to write a recursive function that takes in a number, **x** and an exponent, **n**, and returns the result of `x^n`.

- When computing a power, we have the simplest case of `x^0` = 1.
- We also have a way to define a number raised to a power as a simpler form of itself: `x^n = x * x^(n - 1)`
- By repeatedly performing the simpler calculation, we will eventually get to a power of 0 (assuming that we have a positive power to begin with), and then we can return our `x^0` case of 1.

### The power(x, n) function

```cpp
int power(int x, int n) {
    if (n == 0) {
        return 1;
    } else {
        return x * power(x, n - 1);
    }
}
```

Each previous call waits for the next call to finish (just like any function):

```cpp
int result = power(5, 3);
```

- The first call is to **power(5, 3)**
    - The second call is to **power(5, 2)**
        - The third call is to **power(5, 1)**
            - The fourth call is to **power(5, 0)**, which returns 1.
        - The third call gets the return value of 1, and returns **5 * 1**
    - The second call gets the return value of 5, and returns **5 * 5 (25)**
- The first call gets the return value of 25, and returns **5 * 25 (125)**

**result** now holds 125, and this is how recursion works!

You might argue, wait, I could have done that with a loop just as easily, and you would be right. Recursion isn't always the best way to solve a problem, but we will soon see problems that would be very, very hard to do without recursion (we're looking at simple examples now).

### Big O of power(x, n)?

Guess what? We can apply all of that Big O stuff we just learned to recursive functions, too!

Let's try and think about how **power(x, n)** grows as n grows.

Each time we call the function recursively, we are reducing n by 1. Because we need to go from **n** all the way to 0, we must call the recursive function **n** times. Therefore, we have `O(n)` for our complexity. Neat!

### Faster power function!

An interesting fact about taking a power is that, for even powers, `x^n = x^(n/2) * x^(n/2)`

Therefore, if we have an even power, we can calculate `x^(n/2)` and then just square that when we return…

We have a special case when **n** is odd, but this isn't hard to manage.

Take a look at the following code:

```cpp
int power(int x, int n) {
  if(n == 0) {
      // base case
      return 1;
  } else {
      if (n % 2 == 1) {
          // if n is odd
          return x * power(x, n - 1);
      } else {
          // else, if exp is even
          int y = power(x, n / 2);
          return y * y;
      }
  }
}
```

We have still made the problem smaller at each recursive call, but we have made it much smaller, by halving it each time.

What is our complexity? `O(log n)` – wow!

### Mystery Recursion: Trace this function

```cpp
int mystery(int n) {
    if (n < 10) {
        return n;
    } else {
        int a = n / 10;
        int b = n % 10;
        return mystery(a + b);
    }
}
```

What is the result of `mystery(648)`?

First call, `mystery(648)`:

```cpp
int mystery(int n) { // 648
  if (n < 10) {
      return n;
  } else {
      int a = n / 10; // a = 64
      int b = n % 10; // b = 8
      return mystery(a + b); // mystery(72)
  }
}
```

Second call,

```cpp
int mystery(int n) { // 72
  if (n < 10) {
      return n;
  } else {
      int a = n / 10; // a = 7
      int b = n % 10; // b = 2
      return mystery(a + b); // mystery(9)
  }
}
```

Third call,

```cpp
int mystery(int n) { // 9
  if (n < 10) {
      return n; // return 9
  } else {
      int a = n / 10;
      int b = n % 10;
      return mystery(a + b);
  }
}
```

Second and first calls both return the result of the third call (nothing else gets added to the return value), so **9** gets returned all the way to the original calling function.

### isPalindrome(string s)

Write a recursive function isPalindrome accepts a string and returns true if it reads the same forwards as backwards.

```cpp
isPalindrome("madam");          // true 
isPalindrome("racecar");        // true 
isPalindrome("step on no pets") // true 
isPalindrome("python")          // false 
isPalindrome("byebye")          // false
```

Remember: The Three "Musts" of Recursion

- Your code must have a case for all valid inputs.
- You must have a base case that makes not recursive calls.
- When you make a recursive call it should be to a simpler instance of the same problem, and make forward progress towards the base case.

Answer:

```cpp
// Returns true if the given string reads the same
// forwards as backwards.
// Trivially true for empty or 1-letter strings.
bool isPalindrome(const string& s) {
    if (s.length() < 2) { // base case
        return true;
    } else { // recursive case
        if (s[0] != s[s.length() - 1]) {
            return false;
        }
        string middle = s.substr(1, s.length() - 2);
        return isPalindrome(middle);
    }
}
```

### Back to the Towers of Hanoi

We need to find a very simple case that we can solve directly in order for the recursion to work.
If the tower has size one, we can just move that single disk from the source to the destination.
If the tower has more than one, we have to use the auxiliary spindle.
We can break the entire process down into very simple steps – not necessarily easy to think of steps, but simple ones!

But how to find self-similar problem in Tower of Hanoi?

Here is an idea,

Let's start with original state,

![hanoi-init](codehome/src/img/cpp/hanoi-init.png)

We assume that there are 3 disks, our aim is to put 3 disks from A(origin) spindle to C(destination) spindle.

![hanoi-first](codehome/src/img/cpp/hanoi-first.png)

the first step is to place 2 disks on the top of brown disk into B(auxiliary) spindle. (Here you may have a question, how to accomplish the operation? We will explain it in a moment)

![hanoi-second](codehome/src/img/cpp/hanoi-second.png)

the second step is easy, where we put brown disk from A to C. Notice that this is our **base state** - the only one disk on original spindle.

![hanoi-third](codehome/src/img/cpp/hanoi-third.png)

the only thing left is to place two disks from B to C. But how to do it? Here is a trick, we can see it from a different perspective, where B is new origin spindle, and A becomes new auxiliary spindle. Then it has been downgrade into a subproblem - place 2 disks from A(origin) spindle to C(destination) spindle, noting that Brown disk on C has no influence on the subproblem.

![hanoi-downto](codehome/src/img/cpp/hanoi-downto.png)

Okay, let's make a summary of what we have done by now,

1. Place the disks above the disk at the bottom of the spindle from original spindle to auxiliary spindle. (We haven't solved!)
2. Place the bottom disk from original spindle to destination spindle. (Base Condition)
3. Place the disks on auxiliary spindle to destination spindle. (Downgraded Subproblem)

Look back to **the first step** what we have not solved now. We will find it easily that it is also a downgraded subproblem which is much similar to **the third step**. We place the disks above the bottom disk from A to B with the help of C, where C could be viewed as auxiliary spindle and B could be treated as destination spindle.

That's magic!

## Recursion Recap

Features of Recursion:

- Break a problem into smaller subproblems of the same form, and call the same function again on that smaller form.
- Super powerful programming tool Not always the perfect choice, but often a good one
- Some beautiful problems are solved recursively

Three Musts for Recursion:

- Your code must have a case for all valid inputs
- You must have a base case that makes no recursive calls
- When you make a recursive call it should be to a simpler instance and make forward progress towards the base case.

<EndMarkdown>
[1]: #introduction-to-recursion
[2]: #towers-of-hanoi
[3]: #what-is-recursion
[4]: #why-recursion
[5]: #recursion-in-programming
[6]: #recursion-world
[7]: #recursion-in-real-life
[8]: #counting-a-column-of-people
[9]: #recursive-structure
[10]: #recursive-functions
[11]: #the-three-"musts"-of-recursion
[12]: #the-"recursive-leap-of-faith"
[13]: #recursion-practices
[14]: #the-power(x,-n)-function
[15]: #big-o-of-power(x,-n)?
[16]: #faster-power-function!
[17]: #mystery-recursion:-trace-this-function
[18]: #ispalindrome(string-s)
[19]: #back-to-the-towers-of-hanoi
[20]: #recursion-recap
