1) when compiling, no issues come up

2) when running, the following error comes up:  zsh: bus error ./example2

3)

          1) Output of the program with no breakpoints: 

Process 13899 launched: '/Users/mayageva/CSC411/example2' (arm64)
    Process 13899 stopped
    * thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=2, address=0x23380407f)
        frame #0: 0x0000000100003e48 example2`str_reverse(src="C for System Programming", tgt="gnimmargorP metsyS rof C", n=24) at example2.c:18:18
       15       u_int32_t end = n - 1;
       16  
       17       while(end >= 0) {
    -> 18           tgt[end] = src[start];
       19           end --;
       20           start ++;
       21       }
    Target 0: (example2) stopped.

           2)  The str_reverse is causing the problem

           3) const char *) src = 0x000000016fdfedd0 "C for System Programming"
           (char *) tgt = 0x0000000133804080 "gnimmargorP metsyS rof C"
           (uint32_t) n = 24
           (u_int32_t) start = 24
           (u_int32_t) end = 4294967295

           the 'end' variable reaches the limit of how big the uint32 variable, which means the program does not                                                  succeed in breaking out of the while(end>=0) while loop

           4) the exact cause of the crash is that the while loop conditions are no longer met once 'end' reaches 0,                but the code in the loop still runs due to the nature of while loops. this causes 'end', which is already 0, to be    decremented once more, and becomes the uint32_max value. this causes an out of bounds error in the str-   reverse function and the program crashes.

4) in order to solve this problem, we can change 'end--;' to 'if(end!=0){ end-- }'

