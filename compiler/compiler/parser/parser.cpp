#include "./parser.h"

// 연산자 우선순위
std::map<char, int> BinopPrecedence;

// 현재 토큰
int CurTok;

// 다음 토큰 얻기
int getNextToken()
{
    return CurTok = gettok();
}

// 현재 토큰의 우선순위 얻기
int GetTokPrecedence() {
    if (!isascii(CurTok))
        return -1;

    int TokPrec = BinopPrecedence[CurTok];
    if (TokPrec <= 0) return -1;
    return TokPrec;
}

// 표현식 AST 에러 로그
std::unique_ptr<ExprAST> LogError(const char *Str)
{
    fprintf(stderr, "Error: %s\n", Str);
    return nullptr;
}

// 프로토타입 AST 에러 로그
std::unique_ptr<PrototypeAST> LogErrorP(const char *Str)
{
    LogError(Str);
    return nullptr;
}

// 숫자 표현식 파싱
std::unique_ptr<ExprAST> ParseNumberExpr()
{
    auto Result = std::make_unique<NumberExprAST>(NumVal);
    getNextToken(); // 숫자 소모
    return std::move(Result);
}

// 괄호 표현식 파싱
std::unique_ptr<ExprAST> ParseParenExpr()
{
    getNextToken(); // 여는 괄호 소모
    auto V = ParseExpression();
    if (!V)
        return nullptr;

    if (CurTok != ')')
        return LogError("expected ')'");
    getNextToken(); // 닫는 괄호 소모
    return V;
}

// 식별자 표현식 파싱
std::unique_ptr<ExprAST> ParseIdentifierExpr() 
{
    std::string IdName = IdentifierStr;

    getNextToken(); // 식별자 소모

    if (CurTok != '(') // 함수 호출식이 아닌지 확인
        return std::make_unique<VariableExprAST>(IdName);
    
    // 함수 호출식인 경우
    getNextToken(); // 여는 괄호 소모
    std::vector<std::unique_ptr<ExprAST>> Args;
    if (CurTok != ')') {
        while (true) {
            if (auto Arg = ParseExpression()) // 표현식 파싱하여 argument에 저장
                Args.push_back(std::move(Arg));
            else
                return nullptr;

            if (CurTok == ')')
                break;
            
            if (CurTok != ',')
                return LogError("Expected ')' or ',' in argument list");
            
            getNextToken(); // 쉼표 소모
        }
    }

    getNextToken(); // 닫는 괄호 소모

    return std::make_unique<CallExprAST>(IdName, std::move(Args));
}

// 기본 표현식 파싱
std::unique_ptr<ExprAST> ParsePrimary() 
{
    switch (CurTok)
    {
    case tok_identifier:
        return ParseIdentifierExpr();
    case tok_number:
        return ParseNumberExpr();
    case '(':
        return ParseParenExpr();
    default:
        return LogError("unknown token when expecting an expression");
    }
}

// 이항 연산자와 RHS 파싱
std::unique_ptr<ExprAST> ParseBinOpRHS(int ExprPrec, std::unique_ptr<ExprAST> LHS) 
{
    while (true)
    {
        int TokPrec = GetTokPrecedence(); // 현재 토큰의 우선순위 얻기

        if (TokPrec < ExprPrec) // 표현식의 우선순위보다 낮으면, LHS 그대로 반환하고 종료
            return LHS;

        int BinOp = CurTok; // 연산자 저장
        getNextToken(); // 연산자 소모

        auto RHS = ParsePrimary(); // RHS 파싱
        if (!RHS)
            return nullptr;

        int NextPrec = GetTokPrecedence(); // 다음 연산자(CurTok)의 우선순위 얻기
        if (TokPrec < NextPrec) // 다음 연산자의 우선순위가 높은 경우
        {
            RHS = ParseBinOpRHS(TokPrec + 1, std::move(RHS)); // 계속하여 파싱
            if (!RHS)
                return nullptr;
        }

        // 이항 표현식 AST 구성하여 LHS에 저장
        LHS = std::make_unique<BinaryExprAST>(BinOp, std::move(LHS), std::move(RHS));
    }
    return std::unique_ptr<ExprAST>(nullptr);
}

// 표현식 파싱
std::unique_ptr<ExprAST> ParseExpression() 
{
    auto LHS = ParsePrimary(); // 기본 표현식 파싱
    if (!LHS)
        return nullptr;

    // 연산자 우선순위 기본값을 0으로 주어 이항 표현식 파싱 시작
    return ParseBinOpRHS(0, std::move(LHS));
}

// 함수 프로토타입 파싱 
std::unique_ptr<PrototypeAST> ParsePrototype()
{
    if (CurTok != tok_identifier)
        return LogErrorP("Expected function name in prototype");

    std::string FnName = IdentifierStr; // 함수 이름 저장
    getNextToken(); // 함수 이름 소모

    if (CurTok != '(')
        return LogErrorP("Expected '(' in prototype");

    std::vector<std::string> ArgNames;
    while (getNextToken() == tok_identifier) // 여는 괄호 및 이전 argument 소모와 동시에 식별자인지 확인
        ArgNames.push_back(IdentifierStr); // 식별자를 argument list에 저장

    if (CurTok != ')')
        return LogErrorP("Expected ')' in prototype");

    getNextToken(); // 닫는 괄호 소모

    // 프로토타입 AST 구성하여 반환
    return std::make_unique<PrototypeAST>(FnName, std::move(ArgNames));
}

// 함수 정의 파싱
std::unique_ptr<FunctionAST> ParseDefinition() 
{
    getNextToken(); // def 키워드 토큰 소모
    auto Proto = ParsePrototype(); // 프로토타입 파싱
    if (!Proto) return nullptr;

    if (auto E = ParseExpression()) // 표현식 파싱
        // 함수 AST 구성하여 반환
        return std::make_unique<FunctionAST>(std::move(Proto), std::move(E));
    return nullptr;
}

// extern 구문 파싱
std::unique_ptr<PrototypeAST> ParseExtern()
{
    getNextToken(); // extern 키워드 토큰 소모
    return ParsePrototype(); // 프로토타입 파싱하여 반환
}

// 최상위 익명 함수 표현식 파싱
std::unique_ptr<FunctionAST> ParseTopLevelExpr()
{
    if (auto E = ParseExpression())
    {
        auto Proto = std::make_unique<PrototypeAST>("", std::vector<std::string>());
        return std::make_unique<FunctionAST>(std::move(Proto), std::move(E));
    }
    return nullptr;
}

// 함수 정의 처리
void HandleDefinition()
{
    if (ParseDefinition()) // 함수 정의 파싱
    {
        fprintf(stderr, "Parsed a function definition.\n");
    }
    else // 오류 발생 시
    {
        getNextToken(); // unknown 토큰 소모
    }
}

// Extern 구문 처리
void HandleExtern()
{
    if (ParseExtern()) // Extern 구문 파싱
    {
        fprintf(stderr, "Parsed an extern\n");
    }
    else // 오류 발생 시
    {
        getNextToken(); // unknown 토큰 소모
    }
}

// 최상위 (익명 함수) 표현식 처리
void HandleTopLevelExpression()
{
    if (ParseTopLevelExpr()) // 최상위 (익명 함수) 표현식 파싱
    {
        fprintf(stderr, "Parsed a top-level expr\n");
    }
    else // 오류 발생 시
    {
        getNextToken(); // unknown 토큰 소모
    }
}

void MainLoop()
{
    while (true)
    {
        fprintf(stderr, "ready> ");
        switch (CurTok)
        {
        case tok_eof:
            return;
        case ';':
            getNextToken(); // 최상위 세미콜론 소모
            break;
        case tok_def:
            HandleDefinition();
            break;
        case tok_extern:
            HandleExtern();
            break;
        default:
            HandleTopLevelExpression();
            break;
        }
    }
}