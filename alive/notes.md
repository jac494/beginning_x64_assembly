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
