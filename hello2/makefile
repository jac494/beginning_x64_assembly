#makefile for hello.asm
hello2: hello2.o
		gcc -o ../bin/hello2 hello2.o -no-pie
hello2.o: hello2.asm
		nasm -f elf64 -g -F dwarf hello2.asm -l hello2.lst
