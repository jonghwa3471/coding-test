function solution(numbers) {
    const answer = new Set();
    for(let i = 0; i < numbers.length; i ++) {
        for(let j = 0; j < i; j++) {
            answer.add(numbers[i] + numbers[j]);
        }
    }
    return Array.from(answer).sort((a, b) => a - b);
}