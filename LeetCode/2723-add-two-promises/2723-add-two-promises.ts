type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    const first = await promise1;
    const second = await promise2;
    return first + second
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */