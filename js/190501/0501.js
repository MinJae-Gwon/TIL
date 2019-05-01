// Array helper methods

//case1.
//ESS
var colors = ['red', 'blue', 'green']

for (var i =0; i < colors.length; i++){
    console.log(colors[i])
}

//ES6+ - forEach
const colors = ['red', 'blue', 'green']

const f = function(color){ // callback function
    console.log(color)
}

colors.forEach(f) //익명 함수를 인자로 넘겨 줌 => callback 함수


//case.2
//ESS
var numbers = [1,2,3]
var doubleNumbers =[]

for (var i = 0; i < numbers.length; i++){
    doubleNumbers.push(numbers[i]*2)
}

console.log(doubleNumbers)

//ES6+ - map
const numbers = [1,2,3]

const doubleNumbers = numbers.map(function(number){ //map은 뒤에 함수가 return이 무조건 있어야함, map함수가 하나씩 뽑아서 앞에 함수에 넘겨주게 됨
    return number*2
})

console.log(doubleNumbers) // forEach는 결과값이 없다(단순 반복), map은 결과값이 있다(새로운 배열) 


//case.3
//ES6+ - filter

const products =[
    {name: 'cucumber', type: 'vegie'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegie'},
    {name: 'apple', type: 'fruit'},
]

const fruitProducts = products.filter(function(product){ // 바나나, 사과가 배열에 들어간 것이 return됨
    return product.type === 'fruit' //filter는 해당조건이 true일 경우, item을 가져와 배열에 넣음 
})

console.log(fruitProducts)


//case4.
//ES6+ - find

const users = [
    {name: 'nwith'},
    {name: 'admin'},
    {name: 'zzuli'},
]

const founduser = users.find(function(user){ //순회를 하면서 해당조건이 true일 경우 반환 후 종료, 1개의 값만 반환
    return user.name ==='admin'
})

console.log(founduser)


case5.
ES6+ - every & some

const computers = [
    {name: 'mac', ram: 16},
    {name: 'gram', ram: 8},
    {name: 'series9', ram: 32},
]

const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16
})

const someComputersAvailable = computers.some(function(computer){
    return computer.ram > 16
})

console.log(everyComputersAvailable)
console.log(someComputersAvailable)
