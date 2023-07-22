module LambdaParser where

import Parser
import Data.Lambda
import Data.Builder

-- You can add more imports if you need them

-- Remember that you can (and should) define your own functions, types, and
-- parser combinators. Each of the implementations for the functions below
-- should be fairly short and concise.
-- <letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
-- <lambda> ::= "λ" <letter> "."
-- <normalLambda> ::= <lambda> <letter>
-- <lambdaWithInput> ::= <normalLambda> "(" (<letter>+ | <normalLambda>) ")"
-- <LongForm> ::= "(" <lambdaWithInput> ")" | <section>+ "(" <lambdaWithInput> ")"  ")"+
-- <section> ::= "(" <lambda>  

-- section 
-- section = longLambdaP
-- recur a = 
{-|
    Part 1
-}

-- | Exercise 1

-- | Parses a string representing a lambda calculus expression in long form
--
-- >>> parse longLambdaP "(λx.xx)"
-- Result >< \x.xx
--
-- >>> parse longLambdaP "(λx.(λy.xy(xx)))"
-- Result >< \xy.xy(xx)
--
-- >>> parse longLambdaP "(λx(λy.x))"
-- UnexpectedChar '('
letter ::Parser Char
letter = oneof['a'..'z']
lambda :: Parser (Builder -> Builder)
lambda = do
    is 'λ'
    x <- letter
    is '.'
    pure (lam x)

check :: Parser Builder
check = repeatL ||| termexc ||| termnew ||| termbase
    
termnew :: Parser Builder
termnew = do 
    is '('
    a <- list1 letter
    is ')'
    pure  (foldr1 (ap) (term <$> a) )



repeatL :: Parser Builder
repeatL= do
    is '('
    x <- lambda 
    y <- check
    pure $ x y
termexc :: Parser Builder
termexc = do
    a <- list1 letter
    b <- check
    is ')'
    pure  (foldr1 (ap) (term <$> a) `ap` b)
termbase :: Parser Builder
termbase = do 
    a <- list1 letter
    pure  (foldr1 (ap) (term <$> a) )


longLambdaP :: Parser Lambda
longLambdaP = do
    is '('
    x <- lambda
    y <- check
    is ')'
    pure (build $  x y)

-- | Parses a string representing a lambda calculus expression in short form
--
-- >>> parse shortLambdaP "λx.xx"
-- Result >< \x.xx
--
-- >>> parse shortLambdaP "λxy.xy(xx)"
-- Result >< \xy.xy(xx)
--
-- >>> parse shortLambdaP "λx.x(λy.yy)"
-- Result >< \x.x\y.yy
--
-- >>> parse shortLambdaP "(λx.x)(λy.yy)"
-- Result >< (\x.x)\y.yy
--
-- >>> parse shortLambdaP "λxyz"
-- UnexpectedEof
checks :: Parser Builder
checks = stermexc ||| termnew |||termbase |||newLamb 

newLamb= do
    is '('
    a<- noBrac
    is ')'
    pure (a)
    


lambdaS = noBrac ||| gotBrac

noBrac = do 
    is 'λ'
    a <- list1 letter
    is '.'
    b <- checks 
    
    pure (foldr1 (.) (lam <$> a)  b)
gotBrac = do 
    is '('
    a<- noBrac
    is ')'
    b <- checks
    pure (a `ap` b )

stermexc :: Parser Builder
stermexc = do
    a <- list1 letter
    b <- checks
    pure  (foldr1 (ap) (term <$> a) `ap` b )


shortLambdaP :: Parser Lambda
shortLambdaP = do 
    a <- lambdaS
    
    pure (build $  (a))
-- | Parses a string representing a lambda calculus expression in short or long form
-- >>> parse lambdaP "λx.xx"
-- Result >< \x.xx
--
-- >>> parse lambdaP "(λx.xx)"
-- Result >< \x.xx
--
-- >>> parse lambdaP "λx..x"
-- UnexpectedChar '.'
--

lambdaP :: Parser Lambda
lambdaP = shortLambdaP ||| longLambdaP

{-|
    Part 2
-}

-- | Exercise 1

-- IMPORTANT: The church encoding for boolean constructs can be found here -> https://tgdwyer.github.io/lambdacalculus/#church-encodings

-- | Parse a logical expression and returns in lambda calculus
-- >>> lamToBool <$> parse logicP "True and False"
-- Result >< Just False
--
-- >>> lamToBool <$> parse logicP "True and False or not False and True"
-- Result >< Just True
--
-- >>> lamToBool <$> parse logicP "not not not False"
-- Result >< Just True
--
-- >>> parse logicP "True and False"
-- Result >< (\xy.(\btf.btf)xy\_f.f)(\t_.t)\_f.f
--
-- >>> parse logicP "not False"
-- Result >< (\x.(\btf.btf)x(\_f.f)\t_.t)\_f.f
-- >>> lamToBool <$> parse logicP "if True and not False then True or True else False"
-- Result >< Just True




letters ::Parser Char
letters = oneof['a'..'z'] ||| oneof['A'..'Z']
trueLogic :: Builder
trueLogic = boolToLam True
falseLogic :: Builder
falseLogic = boolToLam False
ifLogic :: Builder
ifLogic = lam 'b' $ lam 't' $ lam 'f' ( term 'b'`ap` term 't'`ap` term 'f')  
andLogic :: Builder 
andLogic  =  
    ((lam 'x'$ lam 'y' $( ifLogic `ap` term 'x' `ap` term 'y' `ap` falseLogic)) )
orLogic :: Builder 
orLogic =
    (lam 'x'$ lam 'y' $( ifLogic `ap` term 'x' `ap` trueLogic `ap` term 'y')) 
notLogic :: Builder
notLogic = (lam 'x'$( ifLogic `ap` term 'x' `ap` falseLogic `ap` trueLogic))

checkString = aND ||| oR  ||| nOT |||tRUE ||| fALSE
aND :: Parser Builder
aND = do 
    string "and"
    return andLogic
tRUE :: Parser Builder
tRUE = do
    string "True"   
    return trueLogic
    
fALSE ::Parser Builder
fALSE = do 
    string "False"
    return falseLogic
oR :: Parser Builder
oR = do 
    string "or"
    return orLogic
nOT:: Parser Builder
nOT = do
    string "not"
    return notLogic
-- chain :: Parser a -> Parser (a->a->a) -> Parser a
-- chain p expression = p >>= rest
--    where
--    rest a = (do
--                f <- expression
--                b <- p
--                rest (f a b)
--             ) ||| pure a
-- test = chain checkString andLogic
-- andChain = chain () andLogic

logicP :: Parser Lambda
logicP = 
    do 
    x <- checkString
    pure (build $ x)


-- | Exercise 2

-- | The church encoding for arithmetic operations are given below (with x and y being church numerals)

-- | x + y = add = λxy.y succ m
-- | x - y = minus = λxy.y pred x
-- | x * y = multiply = λxyf.x(yf)
-- | x ** y = exp = λxy.yx

-- | The helper functions you'll need are:
-- | succ = λnfx.f(nfx)
-- | pred = λnfx.n(λgh.h(gf))(λu.x)(λu.u)
-- | Note since we haven't encoded negative numbers pred 0 == 0, and m - n (where n > m) = 0

-- | Parse simple arithmetic expressions involving + - and natural numbers into lambda calculus
-- >>> lamToInt <$> parse basicArithmeticP "5 + 4"
-- Result >< Just 9
--
-- >>> lamToInt <$> parse basicArithmeticP "5 + 9 - 3 + 2"
-- Result >< Just 13
basicArithmeticP :: Parser Lambda
basicArithmeticP = undefined

-- | Parse arithmetic expressions involving + - * ** () and natural numbers into lambda calculus
-- >>> lamToInt <$> parse arithmeticP "5 + 9 * 3 - 2**3"
-- Result >< Just 24
--
-- >>> lamToInt <$> parse arithmeticP "100 - 4 * 2**(4-1)"
-- Result >< Just 68
arithmeticP :: Parser Lambda
arithmeticP = undefined


-- | Exercise 3

-- | The church encoding for comparison operations are given below (with x and y being church numerals)

-- | x <= y = LEQ = λmn.isZero (minus m n)
-- | x == y = EQ = λmn.and (LEQ m n) (LEQ n m)

-- | The helper function you'll need is:
-- | isZero = λn.n(λx.False)True

-- >>> lamToBool <$> parse complexCalcP "9 - 2 <= 3 + 6"
-- Result >< Just True
--
-- >>> lamToBool <$> parse complexCalcP "15 - 2 * 2 != 2**3 + 3 or 5 * 3 + 1 < 9"
-- Result >< Just False
complexCalcP :: Parser Lambda
complexCalcP = undefined


{-|
    Part 3
-}

-- | Exercise 1

-- | The church encoding for list constructs are given below
-- | [] = null = λcn.n
-- | isNull = λl.l(λht.False) True
-- | cons = λhtcn.ch(tcn)
-- | head = λl.l(λht.h) False
-- | tail = λlcn.l(λhtg.gh(tc))(λt.n)(λht.t)
--
-- >>> parse listP "[]"
-- Result >< \cn.n
--
-- >>> parse listP "[True]"
-- Result >< (\htcn.ch(tcn))(\xy.x)\cn.n
--
-- >>> parse listP "[0, 0]"
-- Result >< (\htcn.ch(tcn))(\fx.x)((\htcn.ch(tcn))(\fx.x)\cn.n)
--
-- >>> parse listP "[0, 0"
-- UnexpectedEof
listP :: Parser Lambda
listP = undefined

-- >>> lamToBool <$> parse listOpP "head [True, False, True, False, False]"
-- Result >< Just True
--
-- >>> lamToBool <$> parse listOpP "head rest [True, False, True, False, False]"
-- Result >< Just False
--
-- >>> lamToBool <$> parse listOpP "isNull []"
-- Result >< Just True
--
-- >>> lamToBool <$> parse listOpP "isNull [1, 2, 3]"
-- Result >< Just False
listOpP :: Parser Lambda
listOpP = undefined


-- | Exercise 2

-- | Implement your function(s) of choice below!
digit :: Parser Char
digit = oneof ['0'..'9']
numberFact :: Parser Integer     
numberFact = read <$> list1 digit
fact :: Parser Integer
fact = do
    rhv <- numberFact
    is '!'
    pure $ factorial rhv

factorial :: Integer -> Integer
factorial n
    | n == 0 || n == 1 = 1
    | otherwise = acc n 1
    where
    acc 0 a = a
    acc b a = acc (b-1) (b * a) 