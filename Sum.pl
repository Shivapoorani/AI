go:- write('Enetr first number : '), read(X),n1,
    write('Enter second number : '),read(Y),n1,
    addmul(X,Y).
addmul(X,Y):-
    S is X+Y,

    M is X*Y,

    write('Addition is : '),write(S),n1,

    write('Multiplication is : '),write(M).
% End of code
