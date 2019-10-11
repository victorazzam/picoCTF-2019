; http://www.keil.com/support/man/docs/armclang_intro/armclang_intro_lmi1470147220260.htm

     .globl   asm4
     .p2align 2
     .type    asm4,%function

myadd:                     // Function "myadd" entry point.
     .fnstart
     add      r0, r0, r1   // Function arguments are in R0 and R1. Add together and put the result in R0.
     bx       lr           // Return by branching to the address in the link register.
     .fnend
