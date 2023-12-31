#!/usr/bin/env python3

import logging
import os

import click

# it might be worth noting that I moved the output executable file to
# ../bin directory so that I could more easily define an exclusion in
# the project root gitignore
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
    push rbp         ; prologue
    mov rbp,rsp
    ; program here
    xor rax,rax      ; clear rax - (rax 0x0 == success return code)
    mov rsp,rbp      ; epilogue
    pop rbp
    ret
"""
DEFAULT_BASE_DIRECTORY = "/home/jac494/Projects/beginning_x64_assembly/"


@click.command()
@click.argument("progname")
def main(progname):
    prog_dir_path = os.path.join(DEFAULT_BASE_DIRECTORY, progname)
    os.mkdir(prog_dir_path)
    prog_fname = f"{progname}.asm"
    prog_fpath = os.path.join(prog_dir_path, prog_fname)
    with open(prog_fpath, "w") as asm_fp:
        prog_file_bytes_written = asm_fp.write(
            BASIC_ASM_TEMPLATE.format(progname=progname)
        )
        logging.debug(f"{prog_file_bytes_written=}")
    makefile_path = os.path.join(prog_dir_path, "makefile")
    with open(makefile_path, "w") as makefile_fp:
        makefile_bytes_written = makefile_fp.write(
            MAKEFILE_TEMPLATE.format(progname=progname)
        )
        logging.debug(f"{makefile_bytes_written=}")


if __name__ == "__main__":
    main()
