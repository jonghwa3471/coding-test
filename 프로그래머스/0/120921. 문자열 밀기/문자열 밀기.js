const solution = (A, B) => {
    if (A === B) return 0;
    let count = 0;
    const last = A.length - 1;
    let slide = A.split("");
    for (let i = 1; i <= last; i++) {
            slide = slide.map((value, index) => {
            if (index === 0) return slide[last];
            return slide[index - 1];
        })
        count ++;
        if (slide.join("") === B) return count;
    }
    return -1;
}