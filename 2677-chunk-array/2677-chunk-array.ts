type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let result = []
    let cur = []
    for(const num of arr) {
        if (cur.length < size) {
            cur.push(num)
        } 

        if (cur.length == size) {
            result.push(cur)
            cur = []
        }
    }
    
    if(cur.length !== 0) {
        result.push(cur)
    }
    return result
};
