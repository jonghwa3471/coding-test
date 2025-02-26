const solution = (quiz) => {
    let result = [];
    quiz.forEach((value) => {
        const replace = value.replace("=", "===");
        if(eval(replace)) result.push("O");
        else result.push("X");
    })
    return result;
}