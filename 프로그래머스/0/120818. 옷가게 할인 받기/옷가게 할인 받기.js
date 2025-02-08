const solution = (price) => {
    let result = 0;
    switch(true) {
        case price >= 500000:
            result =  price - price * 0.2;
            break;
        case price >= 300000:
            result =  price - price * 0.1;
            break;
        case price >= 100000:
            result = price - price * 0.05;
            break;
        default:
            return price;
    }
    return Math.trunc(result);
}