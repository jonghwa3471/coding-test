function solution(N, stages) {
    let total = stages.length;
    const fail = {};
    let challengers = new Array(N + 2).fill(0);
    for(const stage of stages) {
        challengers[stage] += 1; 
    }
    console.log(challengers);
    for(let i = 1; i <= N; i++) {
        if(challengers[i] === 0) {
            fail[i] = 0;
            continue;
        }
        fail[i] = challengers[i] / total;
        total -= challengers[i];
    }
    return Object.entries(fail).sort((a, b) => b[1] - a[1]).map((v) => Number(v[0]));
}