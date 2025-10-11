/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        if(functions.length === 0) {
            return x
        }

        let result = functions[functions.length-1](x)
        for(let i=1; i<functions.length; i++) {
            result = functions[functions.length-1-i](result)
        }
        return result
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */