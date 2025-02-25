const solution = (my_string) => {
    const numbers = my_string.split(" ");
    let result = Number(numbers[0]);
    
    for(let i = 1; i < numbers.length; i += 2) {
        let operator = numbers[i];
        let number = Number(numbers[i + 1]);
        
        if(operator === "+") {
            result += number;
        }
        
        if(operator === "-") {
            result -= number;
        }
        
    }
    return result;
}