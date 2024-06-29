## 컴파일러

### 어휘 분석 (Lexical Analysis)

토크나이저와 렉서를 이용하여 코드(문자열)의 어휘 항목(lexeme)들을 식별하고 이를 토큰으로 변환하여 파서에게 넘겨준다.

### AST와 PT

* AST
  * 추상 구문 트리 (abstract syntax tree)
* PT
  * 파스 트리 (parse tree)

둘의 차이점이 뭘까.. 일단 교재에서는 AST를 통해 언어의 문법을 트리 구조로 표현하였다.

파스트리는 파서(parser)에 의해 실제 코드를 AST의 구조에 따라 분석하여 각 토큰들을 트리 구조로 배치한 것?

https://www.geeksforgeeks.org/abstract-syntax-tree-vs-parse-tree/

시간이 날 때 위 링크를 읽어보자.
