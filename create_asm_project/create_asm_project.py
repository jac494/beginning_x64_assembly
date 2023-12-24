#!/usr/bin/env python3

import os

import click

MAKEFILE_TEMPLATE = """#makefile for {progname}.asm
{progname}: {progname}.o
	gcc -o ../bin/{progname} {progname}.o -no-pie
{progname}.o: {progname}.asm
	nasm -f elf64 -g -F dwarf {progname}.asm -l {progname}.lst
"""
BASIC_ASM_TEMPLATE = """; {progname}.asm
section .data
section .bss
section .text
    global main
main:
    push rbp       ; prologue
    mov rbp,rsp
    ; program here
    mov rax,0     ; success exit code
    mov rsp, rbp   ; epilogue
    pop rbp
    ret
"""
DEFAULT_BASE_DIRECTORY = "/home/jac494/Projects/beginning_x64_assembly/"

@click.command()
@click.argument("progname")
def main(progname):
    prog_path = os.path.join(DEFAULT_BASE_DIRECTORY, progname)
    os.mkdir(prog_path)
    fname = f"{progname}.asm"
    fpath = os.path.join(prog_path, fname)
    with open(fpath, "w") as asm_fp:
        _ = asm_fp.write(BASIC_ASM_TEMPLATE.format(progname=progname))
    makefile_path = os.path.join(prog_path, "makefile")
    with open(makefile_path, "w") as makefile_fp:
        _ = makefile_fp.write(MAKEFILE_TEMPLATE.format(progname=progname))


if __name__ == "__main__":
    main()