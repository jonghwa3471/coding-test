const solution = (array) => {
    let filtered = [];
    const sortArray = array.sort((a, b) => a - b);
    const max = Math.max(...sortArray);
    for (let i = 0; i < max + 1; i++) {
        const newArray = array.filter((item) => item === i);
        if (filtered.length < newArray.length) {
            filtered = [...newArray];
        } else if (filtered.length === newArray.length) {
            filtered = [];
        }
    }
    const result = filtered.length === 0 ? -1 : filtered[0];
    return result;
}