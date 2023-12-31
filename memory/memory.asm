; memory.asm
section .data
    bNum    db      123
    wNum    dw      12345
    warray  times   5 dw 0      ; array of 5 words containing 0
    dNum    dd      12345
    qNum1   dq      12345
    text1   db      "abc",0
    qNum2   dq      3.141592654
    text2   db      "cde",0
section .bss
    bvar    resb    1
    dvar    resd    1
    wvar    resw    10
    qvar    resq    3
section .text
    global main
main:
    push rbp       ; prologue
    mov rbp,rsp
    
    lea rax,[bNum]    ; load  in rax   address of bNum
    mov rax,bNum      ; load  in rax   address of bNum
    mov rax,[bNum]    ; load  in rax   value at bNum
    mov [bvar],rax    ; load  at address of bvar  from rax
    lea rax,[bvar]    ; load  in rax   address of bvar
    lea rax,[wNum]    ; load  in rax   address of wNum
    mov rax,[wNum]    ; load  in rax   content of wNum
    lea rax,[text1]   ; load  in rax   address of text1
    mov rax,text1     ; load  in rax   address of text1
    mov rax,text1+1   ; load  in rax   second character of text1
    lea rax,[text1+1] ; load  in rax   second character of text1
    mov rax,[text1]   ; load  in rax   starting at text1
    mov rax,[text1+1] ; load  in rax   starting at text1+1

    xor rax,rax      ; clear rax - (rax 0x0 == success return code)

    mov rsp, rbp   ; epilogue
    pop rbp
    ret
