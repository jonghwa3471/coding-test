const solution = (num_list) => {
    const even = [];
    const odd = [];
    num_list.forEach((num)=> {
        if(num % 2 === 0) {
            even.push(num)
        }
        else {
            odd.push(num)
        }
    })
    const result = [even.length, odd.length]
    return result
    
}