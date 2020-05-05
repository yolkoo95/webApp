# Strings

## Table of Contents

- [Strings in Cpp][1]
- [Strings and Characters][2]
    - [ASCII][3]
- [A Standard Library][4]
- [String Operators][5]
- [Cpp vs C Strings][6]
- [C string issues][7]


## Strings in Cpp

```cpp
#include <string>

string s = "hello";
```

A string is a sequence of characters, and can be the empty string: " "

In C++, a string has "double quotes", not single quotes:

- **"this is a string"**
- **'this is not a string'**

Strings are similar to Python and Java strings, although the functions have different names and in some cases different behavior.

The biggest difference between a Python or Java string and a C++ string is that C++ strings are mutable (changeable).

The second biggest difference is that in C++, we actually have two types of strings (more on that in a bit)

## Strings and Characters

Strings are made up of characters of type **char**, and the characters of a string can be accessed by the index in the string (this should be familiar):

```cpp
string stanfordTree = "Fear the Tree";
```

```
    index:	 0	 1	 2	 3	 4	 5	 6	 7	 8	 9	 10	 11	 12
character:	'F'	'e'	'a'	'r'	' '	't'	'h'	'e'	' '	'T'	'r'	'e'	'e'
```

```cpp
char c1 = stanfordTree[3];    // 'r'
char c2 = stanfordTree.at(2); // 'a'
```

Notice that **char**s have single quotes and are limited to one ASCII character. A space char is ' ', not '' (in fact, '' is not a valid char at all. It is hard to see on the slide, but there is an actual space character between the single quotes in a valid space char, and there is no space in the not-valid example)

There are two ways to loop through the characters in a string:

```cpp
for (int i = 0; i < stanfordTree.length(); i++) {
    cout << i << " : '" << stanfordTree[i] << "'" << endl;
}
cout << endl;

for (char c : stanfordTree) {
    cout << "'" << c << "'" << endl;
}
cout << endl;
```

Output:

```cpp
0 : 'F'
1 : 'e'
2 : 'a'
3 : 'r'
4 : ' '
5 : 't'
6 : 'h'
7 : 'e'
8 : ' '
9 : 'T'
10 : 'r'
11 : 'e'
12 : 'e'

'F'
'e'
'a'
'r'
' '
't'
'h'
'e'
' '
'T'
'r'
'e'
'e'
```

### ASCII

![caesar](/Users/Quminzhi/Documents/python/webApp/codehome/static/codehome/src/img/cpp/julius-caesar.png)

![ascii](/Users/Quminzhi/Documents/python/webApp/codehome/static/codehome/src/img/cpp/ascii-table.png)

Characters have a numerical representation, as shown in the **ASCII** table above.

- `cout << (int) 'A' << endl; // 65`
- This means you can perform math on characters, but you need to be careful:

```cpp
string plainText = "ATTACK AT DAWN";
string cipherText = "";
int key = 5; // caesar shift by five
    
// only works for uppercase!
for (int i=0; i<(int)plainText.length(); i++) {
    char plainChar = plainText[i];
    char cipherChar;
    if (plainChar >= 'A' && plainChar <= 'Z') {
        cipherChar = plainText[i] + key;
        if (cipherChar > 'Z') {
            cipherChar -= 26; // wrap back around
        }
    } else {
        cipherChar = plainChar;
    }
    cipherText += cipherChar;
}
cout << "Plain text:  " << plainText << endl;
cout << "Cipher text: " << cipherText << endl;
```

Output:

```cpp
Plain text:  ATTACK AT DAWN
Cipher text: FYYFHP FY IFBS
```

## A Standard Library

`#include <cctype>`

This library provides functions that check a single **char** for a property (e.g., if it is a digit), or return a char converted in some way (e.g., to uppercase)

- `isalnum`: checks if a character is alphanumeric
- `isalpha`: checks if a character is alphabetic
- `islower`: checks if a character is lowercase
- `isupper`: checks if a character is an uppercase character
- `isdigit`: checks if a character is a digit
- `isxdigit`: checks if a character is a hexadecimal character
- `iscntrl`: checks if a character is a control character
- `isgraph`: checks if a character is a graphical character
- `isspace`: checks if a character is a space character
- `isblank`: checks if a character is a blank character
- `isprint`: checks if a character is a printing character
- `ispunct`: checks if a character is a punctuation character
- `tolower`: converts a character to lowercase
- `toupper`: converts a character to uppercase

Examples:

```cpp
string mixed = "ab80c3d27";
cout << "The digits in " << mixed << ": " << endl;
for (int i = 0; i < mixed.length(); i++) {
  if (isdigit(mixed[i])) {
      cout << mixed[i] << endl;
  }
}
string s = "my string";
for (int i = 0; i < s.length(); i++) {
  s[i] = toupper(s[i]);
}
cout << "Now " << s << " is all UPPERCASE." << endl;
```

## String Operators

As in Python and Java, you can concatenate strings using `+` or `+=`

```cpp
string s1 = "Chris";
string s2 = s1 + "Gregg"; // s2 == ChrisGregg
```

Like in Python (but unlike) in Java, you can compare strings using relational operators:

```cpp
string s3 = "Zebra";
if ((s1 < s3) && (s3 != "Walrus")) {
    cout << s1 << " < " << s3 << endl;
    cout << "letters earlier in the alphabet are " << endl
         << "less than letters later in the alphabet."
         << endl;
}

cout << endl;

s1[0] = tolower(s1[0]); // s1 now == "chris"
if (s1 > s3) {
    cout << s1 << " > " << s3 << endl;
    cout << "UPPERCASE letters are less than LOWERCASE letters"
         << endl;
}
```

Output:

```cpp
Chris < Zebra
letters earlier in the alphabet are 
less than letters later in the alphabet.

chris > Zebra
UPPERCASE letters are less than LOWERCASE letters
```

Unlike in Python and Java, strings are mutable and can be changed (!):

```cpp
s3.append("Giraffe"); // s2 is now "ZebraGiraffe"
s3.erase(4,3); // s2 is now "Zebrraffe" (which would be a very cool animal)
s3[5] = 'i'; // s2 is now "Zebrriffe"
s3[9] = 'e'; // BAD!!!1! PROGRAM MAY CRASH! POSSIBLE BUFFER OVERFLOW! NO NO NO!
```

Unlike in Python and Java, C++ does not bounds check for you! The compiler doesn't check for you, and Qt Creator won't warn you about this. We have entered the scary territory of you must know what you are doing. Buffer overflows are a critical way for viruses and hackers to do their dirty work, and they can also cause hard to track down bugs.

The following functions are part of the string class, and can be useful:

- `s.append(str)`: add text to the end of a string
- `s.compare(str)`: return -1, 0, or 1 depending on relative ordering
- `s.erase(index, length)` : delete text from a string starting at given index
- `s.find(str)`
- `s.rfind(str)`: first or last index where the start of **str** appears in this string (returns `string::npos` if not found)
- `s.insert(index, str)`: add text into a string at a given index
- `s.length() or s.size()`: number of characters in this string
- `s.replace(index, len, str)`: replaces len chars at given index with new text
- `s.substr(start, length)` or `s.substr(start)`: the next length characters beginning at start (inclusive); if length omitted, grabs till end of string

## Cpp vs C Strings

C++ has (confusingly) two kinds of strings:

- C strings (char arrays), inherited from the C language.
- C++ strings (string objects), which is part of the standard C++ library.
- When possible, declare C++ strings for better usability.

Any string literal such as "hi there" is a C string.

C strings don't have member functions, and you must manipulate them through regular functions. You also must manage the memory properly – this is SUPER IMPORTANT and involves making sure you have allocated the correct memory.

- E.g., C strings do not have a `.length()` function (there are no member functions, as C strings are not part of a class.

You can convert between string types:

- `string("text");` converts C string literal into C++ string
- `string s = someCStr;` converts a C string into a C++ string
- `string.c_str()` returns a C string out of a C++ string

## C string issues

Does not compile! C strings can't be concatenated with `+`

```cpp
string hiThere = "hi" + "there";
```

These three all compile and work properly.

```cpp
string hiThere = string("hi") + "there";
string hello = "hi";
hello += "there";
```

Bug: sets `n` to the memory address of the C string "42" (ack!). Qt Creator will produce a warning.

```cpp
int n = (int) "42";
```
Works – this explicitly converts "42" to a C++ string, and convert it into an int.

[1]: #strings-in-cpp
[2]: #strings-and-characters
[3]: #ascii
[4]: #a-standard-library
[5]: #string-operators
[6]: #cpp-vs-c-strings
[7]: #c-string-issues