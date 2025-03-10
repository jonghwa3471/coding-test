const solution = (lines) => {
    let count = Array(201).fill(0);
    
    lines.forEach(([start, end]) => {
        for (let i = start; i < end; i++) {
            count[i + 100]++;
        }
    })
    
    return count.filter((value) => value > 1).length;
}