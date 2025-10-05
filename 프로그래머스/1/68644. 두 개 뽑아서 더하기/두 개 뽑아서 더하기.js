function solution(numbers) {
    const results = [];
    for(let i = 0; i < numbers.length; i++) {
        for(let j = 0; j < i; j++) {
            results.push(numbers[i] + numbers[j])
        }
    }
    const uniqueResults = [...new Set(results)];
    const sortedResults = uniqueResults.sort((a, b) => a - b);
    return sortedResults;
}