const solution = (bin1, bin2) => (BigInt(`0b${bin1}`) + BigInt(`0b${bin2}`)).toString(2);
