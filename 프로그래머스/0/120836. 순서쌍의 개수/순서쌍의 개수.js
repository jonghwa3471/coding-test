const solution = (n) => {
    let count = 0;
    for (let i = 1; i * i <= n; i++) {
        if(n % i === 0) {
            count += 2;
            if(i * i === n) count--;
        }
    }
    return count;
}