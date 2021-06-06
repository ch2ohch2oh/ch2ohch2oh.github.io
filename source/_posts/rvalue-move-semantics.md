---
title: Rvalues and move semantics
date: 2021-06-06 18:11:07
tags: cpp, move, rvalue
---

## Lvalues and rvalues

A lvalue refers to a memory location which can be referenced by
a pointer.

```cpp
int x = 233;    // x is a lvalue
int * y = &x;
```

A rvalue on the other hand cannot be referenced by a pointer.

```cpp
int * y = &233;
```

A lvalue can appear on the left hand side of the assignment operator,
while a rvalue cannot.

```cpp
int funcl()
{
    return 233;
}

funcl() = 666;  // error: cannot assign to a rvalue
```

An ordinary reference must point to a memory location.

```cpp
void func(int & x) {}

func(233);  // error: 233 is a constant and does not have a mem location
```

## Const lvalue references

We can bind a const reference to a rvalue. The compiler is creating
a temporary variable behind the scene.

```cpp
const int & ref = 233;
```

## Rvalue references

```cpp
std::string s1 = "aaaa";
std::string s2 = "bbbb";
std::string && ref = s1 + s2;
```

## Move semantics

Avoid returning heavy-weight objects by value, since it
involves allocating and deallocating resources.
The `std::move` will convert a lvalue to a rvalue.
The moved object will be set to an invalid state.
The `std::move` does not do anything except merely
tells the compiler that the moved object can be
cannibalized.

## `std::unique_ptr`

`std::unique_ptr` cannot be copied and must be moved.

## References

1. https://www.internalpointers.com/post/understanding-meaning-lvalues-and-rvalues-c
2. https://www.internalpointers.com/post/c-rvalue-references-and-move-semantics-beginners
3. https://stackoverflow.com/questions/3413470/what-is-stdmove-and-when-should-it-be-used
