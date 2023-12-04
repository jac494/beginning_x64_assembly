# Hello.asm Notes

Running into a problem with gdb when trying to run `disassemble main`

```sh
$ ls
hello  hello.asm  hello.lst  hello.o  makefile

[  1:17PM ]  [ jac494@fedora:~/Projects/beginning_x64_assembly/hello ]
 $ cat makefile
 #makefile for hello.asm
 hello: hello.o
                 gcc -o hello hello.o -no-pie
hello.o: hello.asm
                nasm -f elf64 -g -F dwarf hello.asm -l hello.lst
[  1:17PM ]  [ jac494@fedora:~/Projects/beginning_x64_assembly/hello ]
$ nasm --version
NASM version 2.15.05 compiled on Jul 22 2022

[  1:17PM ]  [ jac494@fedora:~/Projects/beginning_x64_assembly/hello ]
$ gdb --version
GNU gdb (GDB) Fedora Linux 13.1-3.fc37
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

[  1:17PM ]  [ jac494@fedora:~/Projects/beginning_x64_assembly/hello ]
$
```

```txt
$ gdb hello
GNU gdb (GDB) Fedora Linux 13.1-3.fc37
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from hello...
(gdb) disassemble main
warning: (Error: pc 0x401110 in address map, but not in symtab.)
warning: (Internal error: pc 0x401110 in read in CU, but not in symtab.)
warning: (Error: pc 0x401110 in address map, but not in symtab.)
Dump of assembler code for function main:
warning: (Internal error: pc 0x401110 in read in CU, but not in symtab.)
warning: (Error: pc 0x401110 in address map, but not in symtab.)
   0x0000000000401110warning: (Internal error: pc 0x401110 in read in CU, but not in symtab.)
warning: (Error: pc 0x401110 in address map, but not in symtab.)
 <+0>:  mov    $0x1,%eax
   0x0000000000401115warning: (Internal error: pc 0x401115 in read in CU, but not in symtab.)
warning: (Error: pc 0x401115 in address map, but not in symtab.)
 <+5>:  mov    $0x1,%edi
   0x000000000040111awarning: (Internal error: pc 0x40111a in read in CU, but not in symtab.)
warning: (Error: pc 0x40111a in address map, but not in symtab.)
 <+10>: movabs $0x40401c,%rsi
   0x0000000000401124warning: (Internal error: pc 0x401124 in read in CU, but not in symtab.)
warning: (Error: pc 0x401124 in address map, but not in symtab.)
 <+20>: mov    $0xc,%edx
   0x0000000000401129warning: (Internal error: pc 0x401129 in read in CU, but not in symtab.)
warning: (Error: pc 0x401129 in address map, but not in symtab.)
 <+25>: syscall
   0x000000000040112bwarning: (Internal error: pc 0x40112b in read in CU, but not in symtab.)
warning: (Error: pc 0x40112b in address map, but not in symtab.)
 <+27>: mov    $0x3c,%eax
   0x0000000000401130warning: (Internal error: pc 0x401130 in read in CU, but not in symtab.)
warning: (Error: pc 0x401130 in address map, but not in symtab.)
 <+32>: mov    $0x0,%edi
   0x0000000000401135warning: (Internal error: pc 0x401135 in read in CU, but not in symtab.)
warning: (Error: pc 0x401135 in address map, but not in symtab.)
 <+37>: syscall
End of assembler dump.
(gdb) quit

[  1:34PM ]  [ jac494@fedora:~/Projects/beginning_x64_assembly/hello ]
$
```

Found [this SO post](https://stackoverflow.com/questions/75713295/arch-linux-gdb-error-pc-0x401000-in-address-map-but-not-in-symtab-occured) then uninstalled `nasm 2.15` and found the [rpm for nasm 2.16](https://www.nasm.us/pub/nasm/releasebuilds/2.16.01/linux/nasm-2.16.01-0.fc36.x86_64.rpm) and installed with dnf; now it works!!

```asm
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     mov    eax,0x1
   0x0000000000401115 <+5>:     mov    edi,0x1
   0x000000000040111a <+10>:    movabs rsi,0x40401c
   0x0000000000401124 <+20>:    mov    edx,0xc
   0x0000000000401129 <+25>:    syscall
   0x000000000040112b <+27>:    mov    eax,0x3c
   0x0000000000401130 <+32>:    mov    edi,0x0
   0x0000000000401135 <+37>:    syscall
End of assembler dump.
(gdb)
```

Taking a quick look again **20231120**

When I run this again, the output is identical (exact same memory addresses, interesting, I would have thought they would have changed.)

```txt
[  9:35PM ]  [ jac494@hp-laptop:~/Projects/beginning_x64_assembly/hello ]
 $ gdb hello
GNU gdb (GDB) Fedora Linux 13.2-3.fc37
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from hello...
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     mov    eax,0x1
   0x0000000000401115 <+5>:     mov    edi,0x1
   0x000000000040111a <+10>:    movabs rsi,0x40401c
   0x0000000000401124 <+20>:    mov    edx,0xc
   0x0000000000401129 <+25>:    syscall
   0x000000000040112b <+27>:    mov    eax,0x3c
   0x0000000000401130 <+32>:    mov    edi,0x0
   0x0000000000401135 <+37>:    syscall
End of assembler dump.
(gdb) x/s 0x40401c
0x40401c <msg>: "hello, world"
(gdb)
```

`x/s 0x40401c`: x = examine, s = string; x/c = examine character

```txt
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     mov    eax,0x1
   0x0000000000401115 <+5>:     mov    edi,0x1
   0x000000000040111a <+10>:    movabs rsi,0x40401c
<...snip...>

(gdb) x/c 0x40401c
0x40401c <msg>: 104 'h'
(gdb) x/c 0x40401d
0x40401d:       101 'e'
(gdb)
```

Various ways to examine multiple characters together (ascii, decimal, hex)

```txt
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     mov    eax,0x1
   0x0000000000401115 <+5>:     mov    edi,0x1
   0x000000000040111a <+10>:    movabs rsi,0x40401c
<...snip...>

(gdb) x/13c 0x40401c
0x40401c <msg>: 104 'h' 101 'e' 108 'l' 108 'l' 111 'o' 44 ','  32 ' '  119 'w'
0x404024:       111 'o' 114 'r' 108 'l' 100 'd' 0 '\000'
(gdb) x/13d 0x40401c
0x40401c <msg>: 104     101     108     108     111     44      32      119
0x404024:       111     114     108     100     0
(gdb) x/13x 0x40401c
0x40401c <msg>: 0x68    0x65    0x6c    0x6c    0x6f    0x2c    0x20    0x77
0x404024:       0x6f    0x72    0x6c    0x64    0x00
(gdb)
```

```txt
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401110 <+0>:     mov    eax,0x1
   0x0000000000401115 <+5>:     mov    edi,0x1
   0x000000000040111a <+10>:    movabs rsi,0x40401c
<...snip...>

(gdb) x/s &msg
0x40401c <msg>: "hello, world"
(gdb) x/2x 0x401110
0x401110 <main>:        0xb8    0x01
(gdb)
```

For the above, note the following output in the `hello.lst` file for the machine codes of the first instruction:

```txt
     7                                  main:
     8 00000000 B801000000                  mov     rax, 1      ; 1 = write
     9 00000005 BF01000000                  mov     rdi, 1      ; 1 = to stdout
```

The main thing here being both `0x401110 <main>:        0xb8    0x01` and `8 00000000 B801000000` as the first instruction in main and reference to main.

