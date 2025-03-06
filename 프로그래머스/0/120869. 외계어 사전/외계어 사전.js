const solution = (spell, dic) => {
    const string = spell.join("");
    const length = string.length;
    const regex = new RegExp(`^(?!.*(.).*\\1)[${string}]{${length}}$`);
    const filtered = dic.filter((word) => word.match(regex));
    return filtered.length > 0 ? 1 : 2;
}