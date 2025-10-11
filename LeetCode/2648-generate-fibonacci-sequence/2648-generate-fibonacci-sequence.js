/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let x0 = 0;
    let x1 = 1;
    yield x0
    yield x1
    while (true) {
        let temp = x0
        x0 = x1
        x1 = temp + x1
        yield x1
    }
    return 
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */