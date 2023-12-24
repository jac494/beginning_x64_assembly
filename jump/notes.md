# Notes

Found [this SO post](https://stackoverflow.com/questions/63188810/debugging-nasm-in-vs-code) when I was struggling to use nasm on a remote machine. Ultimately it led me to using:

```sh
gdb ./jump --tui`
(gdb) layout regs
(gdb) b main
(gdb) run
```

A few 'nexts' later...

```txt
│ Register group: general                                                                                                                                           │
│rax            0x2a                42                 rbx            0x29                41                 rcx            0x403e18            4210200             │
│rdx            0x7fffffffe188      140737488347528    rsi            0x7fffffffe178      140737488347512    rdi            0x1                 1                   │
│rbp            0x7fffffffe060      0x7fffffffe060     rsp            0x7fffffffe060      0x7fffffffe060     r8             0x0                 0                   │
│r9             0x7ffff7fcc910      140737353926928    r10            0x7fffffffdd90      140737488346512    r11            0x202               514                 │
│r12            0x0                 0                  r13            0x7fffffffe188      140737488347528    r14            0x403e18            4210200             │
│r15            0x7ffff7ffd000      140737354125312    rip            0x401147            0x401147 <main+23> eflags         0x202               [ IF ]              │
│cs             0x33                51                 ss             0x2b                43                 ds             0x0                 0                   │
│es             0x0                 0                  fs             0x0                 0                  gs             0x0                 0                   │
│                                                                                                                                                                   │
│                                                                                                                                                                   │
│                                                                                                                                                                   │
┌─jump.asm──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│B      13      push    rbp                                                                                                                                         │
│       14      mov     rbp,rsp                                                                                                                                     │
│       15      mov     rax, [number1]      ; move the numbers into registers                                                                                       │
│       16      mov     rbx, [number2]                                                                                                                              │
│       17      cmp     rax,rbx             ; compare rax and rbx                                                                                                   │
│  >    18      jge     greater             ; rax greater or equal go to greater:                                                                                   │
│       19  mov rax,0                       ; no xmm involved                                                                                                       │
│       20      call    printf              ; display fmt2                                                                                                          │
│       21      jmp     exit                ; jump to label exit:                                                                                                   │
│       22  greater:                                                                                                                                                │
│       23      mov     rdi,fmt1            ; rax is greater                                                                                                        │
│       24      mov     rax,0               ; no xmm involved                                                                                                       │
│       25      call    printf                                                                                                                                      │
│       26  exit:                                                                                                                                                   │
│       27      mov     rsp,rbp                                                                                                                                     │
│       28      pop     rbp                                                                                                                                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
Breakpoint 1 at 0x401130: file jump.asm, line 12.
(gdb) run
Starting program: /home/jac494/Projects/beginning_x64_assembly/jump/jump

Breakpoint 1, main () at jump.asm:12
(gdb) layout regs
(gdb) n
(gdb) n
```

Some info on the different flags in eflags (at one point in `jump` they were `[ ZF PF IF ]` ) - [c-jump.com eflags bits](http://www.c-jump.com/CIS77/ASM/Instructions/I77_0070_eflags_bits.htm)

This is another pretty neat thing I found there, this site is kinda cool: [C++ STL Tutorial](http://www.c-jump.com/pagedownload07cppstl.html)