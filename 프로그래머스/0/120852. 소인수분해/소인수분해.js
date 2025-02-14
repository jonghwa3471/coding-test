function solution(n) {
    let factors = new Set();  
    for (let i = 2; i * i <= n; i++) {
        while (n % i === 0) {  
            factors.add(i);
            n /= i;  
        }
    }
    if (n > 1) factors.add(n); 
    return [...factors].sort((a, b) => a - b); 
}