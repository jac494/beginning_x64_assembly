;hello4.asm
extern      printf
section .data
      msg    db    "hello, world",0
      fmtstr db    "This is our string: %s",10,0 ; printformat
section .bss
section .text
    global  main
main:
    push    rbp
    mov     rbp,rsp
    mov     rdi,fmtstr   ; first arg for printf
    mov     rsi, msg     ; second arg for printf
    mov     rax, 0       ; no xmm registers involved
    call    printf       ; call the function
    mov     rsp,rbp
    pop     rbp
    mov     rax, 60      ; 60 = exit
    mov     rdi, 0       ; 0 = success
    syscall              ; quit
