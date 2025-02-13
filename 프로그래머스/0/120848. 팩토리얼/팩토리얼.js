const factorial = (number) => number === 1 ? 1 : number * factorial(number - 1);

const solution = (n) => {
    if(n < 2) return 1;
    let result = 0;
    for (let i = 2; i <= 10; i++) {
        factorial(i);
        if(factorial(i) <= n){
            result = i;
        }
    }
    return result;
}