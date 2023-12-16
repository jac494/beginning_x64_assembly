# Notes for Alive and Kicking

gdb output of `disassemble main`:

```txt
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     push   rbp
   0x0000000000401111 <+1>:     mov    rbp,rsp
   0x0000000000401114 <+4>:     mov    eax,0x1
   0x0000000000401119 <+9>:     mov    edi,0x1
   0x000000000040111e <+14>:    movabs rsi,0x40401c
   0x0000000000401128 <+24>:    mov    edx,0xe
   0x000000000040112d <+29>:    syscall
   0x000000000040112f <+31>:    mov    eax,0x1
   0x0000000000401134 <+36>:    mov    edi,0x1
   0x0000000000401139 <+41>:    movabs rsi,0x40402b
   0x0000000000401143 <+51>:    mov    edx,0x13
   0x0000000000401148 <+56>:    syscall
   0x000000000040114a <+58>:    mov    rsp,rbp
   0x000000000040114d <+61>:    pop    rbp
   0x000000000040114e <+62>:    mov    eax,0x3c
   0x0000000000401153 <+67>:    mov    edi,0x0
   0x0000000000401158 <+72>:    syscall
End of assembler dump.
(gdb)
```

Examine string at `0x40401c` (from output above, this should be "Hello, world!\n")

```txt
(gdb) disassemble main
Dump of assembler code for function main:
=> 0x0000000000401110 <+0>:     push   rbp
<snip>
   0x000000000040111e <+14>:    movabs rsi,0x40401c
<snip>
End of assembler dump.
(gdb) x/s 0x40401c
0x40401c <msg1>:        "Hello, world!\n"
```

...or via reference to the `msg1` variable:

```txt
(gdb) disassemble main
Dump of assembler code for function main:
=> 0x0000000000401110 <+0>:     push   rbp
<snip>
   0x000000000040111e <+14>:    movabs rsi,0x40401c
<snip>
End of assembler dump.
(gdb) x/s 0x40401c
0x40401c <msg1>:        "Hello, world!\n"
(gdb) x/s &msg1
0x40401c <msg1>:        "Hello, world!\n"
```

* `x/s`: e**x**amine **s**tring?
* `x/dw`: e**x**amine **d**ecimal **w**ord?
* `x/xw`: e**x**amine he**x** **w**ord?

Trying to get additional characters/bytes out of examine:

```txt
(gdb) x/s 0x40401c
0x40401c <msg1>:        "Hello, world!\n"
(gdb) x/xw 0x40401c
0x40401c <msg1>:        0x6c6c6548
(gdb) x/x 0x40401c
0x40401c <msg1>:        0x6c6c6548
(gdb) x/xb 0x40401c
0x40401c <msg1>:        0x48
(gdb) x/xb 0x40401c + f                       # nope!
No symbol "f" in current context.
(gdb) x/xb 0x40402b
0x40402b <msg2>:        0x41
(gdb) x/s 0x40402b
0x40402b <msg2>:        "Alive and Kicking!\n"
(gdb) x/xb 0x40402b
0x40402b <msg2>:        0x41
(gdb) x/x2b 0x40402b                          # nope!
Invalid number "2b".
(gdb) x/xb2 0x40402b                          # nope!
A syntax error in expression, near `0x40402b'.
(gdb) x/2xb 0x40402b                          # SUCCESS!!
0x40402b <msg2>:        0x41    0x6c
(gdb)
```

From internal help menu in gdb (`help x`):

```txt
(gdb) help x
Examine memory: x/FMT ADDRESS.
ADDRESS is an expression for the memory address to examine.
FMT is a repeat count followed by a format letter and a size letter.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char), s(string)
  and z(hex, zero padded on the left).
Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).
The specified number of objects of the specified size are printed
according to the format.  If a negative number is specified, memory is
examined backward from the address.

Defaults for format and size letters are those previously used.
Default count is 1.  Default address is following last thing printed
with this command or "print".
(gdb)
```

* FMT is a repeat count followed by a format letter and a size letter.
* Format letters are:
  * o(octal)
  * x(hex)
  * d(decimal)
  * u(unsigned decimal)
  * t(binary)
  * f(float)
  * a(address)
  * i(instruction)
  * c(char)
  * s(string)
  * z(hex, zero padded on the left)
* Size letters are:
  * b(byte)
  * h(halfword)
  * w(word)
  * g(giant, 8 bytes)

Now for examining `radius` and `pi`

```txt
; from 'alive.asm'
section .data
    <snip>
    radius  dq  357     ; no string, not displayable?
    pi      dq  3.14    ; no string, not displayable?

(gdb) x/dw &radius
0x40403f <radius>:      357
(gdb) x/xw &radius
0x40403f <radius>:      0x00000165
(gdb) x/fg &pi
0x404047 <pi>:  3.1400000000000001
(gdb) x/fx &pi
0x404047 <pi>:  0x40091eb851eb851f
(gdb)
```

Seeing how these numbers are stored via a look at `alive.lst`:

```txt
7 00000023 6501000000000000    radius  dq  357    ; no string, not displayable?
8 0000002B 1F85EB51B81E0940    pi      dq  3.14   ; no string, not displayable?
```

we can see that they're stored in reverse order (little-endian)

| name   | defined value | hex value            | stored value (little-endian)   |
| ------ | ------------- | -------------------- | ------------------------------ |
| radius | 357 (decimal) | `0x0165`             | `6501000000000000`             |
| pi     | 3.14 (float)  | `0x40091eb851eb851f` | `1F85EB51B81E0940`             |
