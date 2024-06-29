#include "./ast.h"

// 숫자 표현식 AST
NumberExprAST::NumberExprAST(double Val) : Val(Val) {}

// 변수 표현식 AST
VariableExprAST::VariableExprAST(const std::string &Name) : Name(Name) {}

// 이항 표현식 AST
BinaryExprAST::BinaryExprAST(char Op, std::unique_ptr<ExprAST> LHS, std::unique_ptr<ExprAST> RHS)
    : Op(Op), LHS(std::move(LHS)), RHS(std::move(RHS)) {}

// 호출 표현식 AST
CallExprAST::CallExprAST(const std::string &Callee, std::vector<std::unique_ptr<ExprAST>> Args)
    : Callee(Callee), Args(std::move(Args)) {}

// 프로토타입 AST
PrototypeAST::PrototypeAST(const std::string &Name, std::vector<std::string> Args)
    : Name(Name), Args(std::move(Args)) {}

const std::string &PrototypeAST::getName() const
{
    return Name;
}

// 함수 AST
FunctionAST::FunctionAST(std::unique_ptr<PrototypeAST> Proto, std::unique_ptr<ExprAST> Body)
    : Proto(std::move(Proto)), Body(std::move(Body)) {}