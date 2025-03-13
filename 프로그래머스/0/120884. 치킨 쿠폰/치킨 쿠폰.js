const solution = (chicken) => {
    let bonus = 0;
    for (let i = 10; i <= chicken; i += 10) {
        bonus += 1;
        chicken += 1;
    }
    return bonus;
}