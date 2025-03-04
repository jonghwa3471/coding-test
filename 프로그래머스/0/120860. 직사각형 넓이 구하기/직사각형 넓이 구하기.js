const solution = (dots) => {
    const dots1 = dots.filter((dot) => dots[0][1] === dot[1]);
    const dots2 = dots.filter((dot) => dots[0][1] !== dot[1]);
    const x = Math.abs(dots1[1][0] - dots[0][0]);
    const y = Math.abs(dots2[0][1] - dots1[0][1]);
    const result = x * y;
    return result;
}