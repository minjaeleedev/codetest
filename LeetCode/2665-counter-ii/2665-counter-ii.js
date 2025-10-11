/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let f = init
    let x = init
    return {
        increment: ()=>x+=1,
        reset: ()=>x=f,
        decrement: ()=>x-=1
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */