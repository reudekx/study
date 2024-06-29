#pragma once

#ifndef PARSER_H
#define PARSER_H

#include "./../lexer/lexer.h"
#include "./../ast/ast.h"

#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <memory>
#include <map>

extern std::map<char, int> BinopPrecedence;
extern int CurTok;

int getNextToken();

int GetTokPrecedence();

std::unique_ptr<ExprAST> ParseNumberExpr();

std::unique_ptr<ExprAST> ParseParenExpr();

std::unique_ptr<ExprAST> ParseIdentifierExpr();

std::unique_ptr<ExprAST> ParsePrimary();

std::unique_ptr<ExprAST> ParseBinOpRHS(int ExprPrec, std::unique_ptr<ExprAST> LHS);

std::unique_ptr<ExprAST> ParseExpression();

std::unique_ptr<PrototypeAST> ParsePrototype();

std::unique_ptr<FunctionAST> ParseDefinition();

std::unique_ptr<PrototypeAST> ParseExtern();

std::unique_ptr<FunctionAST> ParseTopLevelExpr();

void HandleDefinition();

void HandleExtern();

void HandleTopLevelExpression();

void MainLoop();

#endif