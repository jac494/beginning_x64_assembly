#makefile for jumploop.asm
jumploop: jumploop.o
	gcc -o ../bin/jumploop jumploop.o -no-pie
jumploop.o: jumploop.asm
	nasm -f elf64 -g -F dwarf jumploop.asm -l jumploop.lst
