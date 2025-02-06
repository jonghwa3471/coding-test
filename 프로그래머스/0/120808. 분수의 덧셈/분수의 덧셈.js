const solution = (numer1, denom1, numer2, denom2) => {
    const gcd = (a, b) => b ? gcd(b, a % b) : a;
    const lmc = (a, b) => (a * b) / gcd(a, b);
    
    const commonDenom = lmc(denom1, denom2);
    const commonNumer = (numer1 * (commonDenom / denom1)) + (numer2 * (commonDenom / denom2));
    
    const gcdValue = gcd(commonNumer, commonDenom);
    return [commonNumer / gcdValue, commonDenom / gcdValue];
}