const solution = (array) => {
    const sortArray = array.sort((a, b)=> a - b);
    const middleIndex = Math.floor(sortArray.length / 2);
    return sortArray[middleIndex];
}