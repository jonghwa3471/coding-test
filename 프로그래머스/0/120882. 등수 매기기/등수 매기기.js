const solution = (score) => {
    const averages = score.map(([eng, math], index) => ({
        index,
        avg: (eng + math) / 2
    }))
    averages.sort((a, b) => b.avg - a.avg);
    
    const result = Array(score.length).fill(0);
    
    let ranking = 1;
    for (let i = 0; i < score.length; i++) {
        if (i > 0 && averages[i].avg !== averages[i - 1].avg) {
            ranking = i + 1;
        }
        result[averages[i].index] = ranking;
    }
    return result;
}