const solution = (dots) => {
    const getSlope = ([x1, y1], [x2, y2]) => (y2 - y1) / (x2 - x1);

    return (
        getSlope(dots[0], dots[1]) === getSlope(dots[2], dots[3]) ||
        getSlope(dots[0], dots[2]) === getSlope(dots[1], dots[3]) ||
        getSlope(dots[0], dots[3]) === getSlope(dots[1], dots[2])
    ) ? 1 : 0;
};
