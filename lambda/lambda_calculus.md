# 람다 대수 (lambda calculus)

* 위키 백과를 보고 정리하는 중. 검증 必

### 변수 (variable)

* x
  * 변수는 매개변수(parameter)를 의미하는 알파벳 혹은 문자열

### 추상화 (abstraction)

* (&lambda;x.M)
  * 단일 입력 x를 받아 M의 표현으로 치환하는 익명의 함수
  * 가령 λ&lambda;.x + 1은 함수 f(x) = x + 1의 람다 추상화이다.
  * 람다 추상화를 통해 변수 x는 M에 속박(bound)된다.


### 적용 (application)

* (M N)
  * 함수(function) M을 인자(argument) N에 적용한다. M과 N은 모두 람다 항이다. 


### Reduction operations

* 알파 변환 (&alpha;-conversion)
  * (&lambda;x.M[x]) &rarr; (&lambda;y.M[y])
  * 표현식에서 제한변수(bound variable)의 이름을 새로 바꾼다.
  * Name collision을 피하기 위해 사용된다.
* 베타 축약 (&beta;-reduction)
  * ((&lambda;x.M) N) &rarr; (M[x := N])
  * 추상화의 body 내의 제한 변수를 인자 표현식으로 치환한다.
  * 베타 축약은 하스켈과 같은 함수형 프로그래밍 언어의 이상적 버전으로 보일 수 있다.
    * 이러한 견해 하에서, 베타 축약은 계산 단계에 대응될 수 있다.
    * 이 단계는 더이상 축약할 게 없을 때까지 추가적인 베타 축약에 의해 반복될 수 있다.
      * 다만 형식화되지 않은 람다 대수에선, 이 축약 과정이 종료되지 않을 수 있다.
      * 가령 (&lambda;x.xx)(&lambda;x.xx) 에서 베타 축약을 한 차례 진행하면, 자기 자신이 그대로 반복되어 나타나는 것을 확인할 수 있다.
        * 해당 함수를 &omega; combinator라고 한다.

### 람다 항 (lambda term)

* 다음의 3가지 규칙들은 구문적으로 유효한 모든 람다 항을 작성하는 데 적용할 수 있는 귀납적 정의를 제공한다.
  * 모든 변수와 상수는 람다 항이다.
  * 만약 t가 람다 항이고 x가 변수라면, (&lambda;x.t)는 람다 항이다.
  * 만약 t와 s가 람다 항이면, (t s)는 람다 항이다.

### 자유 변수와 제한 변수

* 자유 변수 (free variable)
  * 람다 항 M의 자유 변수의 집합 FV(M)은 M의 구조에 따라 다음과 같이 재귀적으로 정의된다.
    * 변수 x에 대하여, FV(x) = {x}
    * 상수 &alpha;에 대하여, FV(&alpha;) = &emptyset;
    * 두 람다 항 M, N에 대하여, FV(M N) = FV(M) &cup; FV(N)
    * 람다 항 M 및 변수 x에 대하여, FV(&lambda;x.M) = FV(M) &setminus; {x}
* 제한 변수 (bound variable)
  * 람다 항 M에 등장하는 변수 가운데 자유 변수가 아닌 것들을 M의 제한 변수라고 한다.

* 가령 변수 x, y, z에 대하여 (&lambda;x.&lambda;y.xyz)x 의 자유 변수의 집합은 {x, z}이며, 제한 변수의 집합은 {y}이다.

### 치환 (substitution)

* 치환 연산의 정의는 자연스러우며, 다만 원래 람다 항의 의미가 변질되는 경우에는 알파 변환이 선행되어야 한다.
* 구체적으로, 람다 항 M, N 및 변수 x에 대하여, x를 N으로 치환한 M의 치환 실례(substitution instance) M[N / x]는 M의 구조에 따라 다음과 같이 재귀적으로 정의된다.
  * 변수 y에 대하여, y[x := N] =
    * N (y = x)
    * y (y != x)
  * 상수 &alpha;에 대하여, &alpha;[x := N] = &alpha;
  * 람다항 A, B에 대하여, (A B)[x := N] = (A[x := N])(B[x := N])
  * 람다 항 M 및 변수 y에 대하여, (&lambda;y.M)[x := N] =
    * &lambda;y.M (y = x)
    * &lambda;y.(M[x := N])  ((y != x)  and (y &notin; FV(N) or x &notin; FV(M)))
    * &lambda;z.(M[y := z]  [x := N]) (y != x) and (y &in; FV(N) and x &in; FV(M)) and (z = M과 N의 자유 변수 집합 중 max보다 큰 집합의 원소 중 min -> 즉 새로운 변수 z를 이용)
  * 1번째 조건은, y = x인 경우 치환하지 않겠다는 의미인 듯?
  * 2번째 조건에서, y가 N의 자유변수가 아닐 때 y는 N에 대해 fresh하다고 일컬어진다.
  * 3번째 조건은 2번째 조건에 포함되는데, 그럼에도 불구하고 따로 분리되어 있는 이유는 아마 변수 shadowing을 피하기 위함인 것 같다.

* 영문 위키백과를 확인한 결과, 결국 위의 치환 연산들이 정의되어진 이유는 capture-avoiding을 위해서인 것 같다.
* 즉 capture-avoiding을 하며 베타 축약을 하는 것 (아마도?)
