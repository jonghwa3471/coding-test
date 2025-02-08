const solution = (money) => {
    const maxCoffee = Math.trunc(money / 5500);
    const leftMoney = money - (maxCoffee * 5500);
    return [maxCoffee, leftMoney];
}