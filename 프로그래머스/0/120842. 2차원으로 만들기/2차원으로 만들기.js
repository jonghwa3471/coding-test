const solution = (num_list, n) => {
    let result = [];
    for (let i = 0; i < num_list.length / n; i++) {
        result.push(num_list.slice(n * i, n + (n * i)));
    }
    return result;
}