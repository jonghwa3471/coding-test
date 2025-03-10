const solution = (a, b) => {
    const gcd = (x, y) => y ? gcd(y, x % y) : x;
    const g = gcd(a, b);
    b /= g;
    
    while (b % 2 === 0) b /= 2;
    while (b % 5 === 0) b /= 5;
    
    return b === 1 ? 1 : 2;
}