#include "./lexer.h"

std::string IdentifierStr;
double NumVal;

int gettok()
{
    static int LastChar = ' ';

    while (isspace(LastChar)) // 공백, 탭, 개행 제거
        LastChar = getchar();

    if (isalpha(LastChar)) // 알파벳인 경우
    {
        IdentifierStr = LastChar; // 문자열 조립
        while (isalnum((LastChar = getchar())))
            IdentifierStr += LastChar;

        if (IdentifierStr == "def") // def 키워드인 경우
            return tok_def;
        if (IdentifierStr == "extern") // extern 키워드인 경우
            return tok_extern;
        return tok_identifier;
    }

    if (isdigit(LastChar) || LastChar == '.') // 숫자 혹은 .인 경우
    {
        std::string NumStr;
        do
        {
            NumStr += LastChar;
            LastChar = getchar();
        } while (isdigit(LastChar) || LastChar == '.'); // 가령 12.34.56의 경우 12.34로 처리됨에 유의하라.

        NumVal = strtod(NumStr.c_str(), 0); // 숫자를 저장
        return tok_number;
    }

    if (LastChar == '#') // 주석인 경우
    {
        do
            LastChar = getchar();
        while (LastChar != EOF && LastChar != '\n' && LastChar != '\r');

        if (LastChar != EOF) // EOF가 아니면 토큰을 반환
            return gettok();
    }

    if (LastChar == EOF) // EOF인 경우
        return tok_eof;

    // 위 모든 경우에 해당되지 않는, +와 같은 연산자인 경우
    int ThisChar = LastChar;
    LastChar = getchar();
    return ThisChar;

};