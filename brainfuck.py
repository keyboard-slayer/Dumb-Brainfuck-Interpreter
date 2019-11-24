#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_loop_end(code: str) -> int:
    index = 0

    while code[index] != ']':
        index += 1
    
    return index


def execute_brainfuck(code: str) -> str:
    output = ""
    memory_array = [0 for _ in range(16)]
    pointer_pos = 0
    op_pos = 0

    loop_begin = 0
    loop_end = 0

    while op_pos < len(code):

        if code[op_pos] == '>':
            if pointer_pos >= 16 :
                raise Exception(f"Pointer position overflow at char n°{op_pos}")

            pointer_pos += 1
        
        if code[op_pos] == '<':
            if pointer_pos <= 0:
                raise Exception(f"Pointer position overflow at char n°{op_pos}")
            
            pointer_pos -= 1
        
        if code[op_pos] == '-':
            if memory_array[pointer_pos] == 0:
                memory_array[pointer_pos] = 256
            
            memory_array[pointer_pos] -= 1

        if code[op_pos] == '+':
            if memory_array[pointer_pos] == 255:
                memory_array[pointer_pos] = -1
            
            memory_array[pointer_pos] += 1
        
        if code[op_pos] == '.':
            output += chr(memory_array[pointer_pos])
        
        if code[op_pos] == ']':
            op_pos = loop_begin

        if code[op_pos] == '[':
            if not loop_begin and not loop_end:
                loop_end = find_loop_end(code[op_pos:]) + op_pos
                loop_begin = op_pos 
            
            if memory_array[pointer_pos] == 0:
                op_pos = loop_end 
                loop_end = 0
                loop_begin = 0

        op_pos += 1

    return output

if __name__ == "__main__":
    import sys 

    if len(sys.argv) != 2:
        print(f"{sys.argv[0]} *.bf")

    else:
        with open(sys.argv[1], 'r') as brainfuck_code:
            print(execute_brainfuck(''.join(brainfuck_code.readlines())))
