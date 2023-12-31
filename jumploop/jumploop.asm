; jumploop.asm
extern printf
section .data
    number  dq  5
    fmt     db  "The sum from 0 to %ld is %ld",0
section .bss
section .text
    global main
main:
    push rbp     ; prologue
    mov rbp,rsp
    mov rbx,0    ; counter
    mov rax,0    ; sum will be in rax
jloop:
    add rax,rbx
    inc rbx
    cmp rbx,[number]  ; number already reached?
    jle jloop         ; number not reached yet, loop
    ; number reached, continue
    mov rdi,fmt       ; prepare for calling printf
    mov rsi,[number]
    mov rdx,rax
    mov rax,0
    call printf

    mov rax,0  ; result of program execution
    mov rsp, rbp ; epilogue
    pop rbp
    ret