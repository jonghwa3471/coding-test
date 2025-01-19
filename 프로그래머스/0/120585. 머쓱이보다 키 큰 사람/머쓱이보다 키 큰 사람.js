const solution = (array, height) => {
    const taller = array.filter((friendsHeight)=> friendsHeight > height);
    return taller.length
}