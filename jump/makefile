#makefile for jump.asm
jump: jump.o
	gcc -o ../bin/jump jump.o -no-pie
jump.o: jump.asm
	nasm -f elf64 -g -F dwarf jump.asm -l jump.lst
