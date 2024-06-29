#include "./parser/parser.h"


#include <cstdio>
#include <cstdlib>

int main()
{
    BinopPrecedence['<'] = 10;
    BinopPrecedence['+'] = 20;
    BinopPrecedence['-'] = 20;
    BinopPrecedence['*'] = 40;

    fprintf(stderr, "ready> ");
    getNextToken();

    MainLoop();

    return 0;
}