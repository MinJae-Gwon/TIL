// 반복1 - while
let i = 0
while (i < 10){
    console.log(i)
    i++
}

// 반복 2 - for
for (let j=0; j < 10; j++){
    console.log(j)
}

//반복 3 - for of
for (let number of [1,2,3,4,5]) { //const로도 선언 가능, number는 뭐 뭐 이렇게 새로 선언이 되기 떄문에
    console.log(number)
}



//배열(Array)
const numbers = [1,2,3,4]

console.log(numbers[0])
console.log(numbers[-1]) //JS는 음수 지원 하지 않음

//object
const me = {
    name: 'MJ',
    'phone number': '010',
    appleProducts: {
        ipad: true,
        iphone: 'X'
    }
}

//JSON - JavaScript Obkect Notation (JS 객체 표현법)
JSON.stringify() // Object -> JSON String
JSON.parse() //JSON String -> Object


// 함수정의
// 방법1 - 선언식
function add(num1, num2){
    return num1 + num2
} 
console.log('add: ' + add(1,2))

//방법2 - 표현식
const sub = function (num1, num2){
    return num1 - num2
}
console.log('sun: ' + SVGUnitTypes(5,3))

typeof add // function
typeof sub // function

//Arrow Fuction
//기존 방법
// const mul = function(num1, num2){
//     return num1*num2
// }
//Arrow
const mul = (num1, num2) => {
    return num1 * num2
}

let square = (num) => {
    return num**2
}
// return문 다 한줄이면 {} & return 생략 가능
square = (num) => num**2

// ()안의 인자가 하나뿐이면 ()도 생략 가능. 0개 일 때는 생략 불가능
// 인자 1개
square = num => num**2
// 인자 0개
let noArgs = () => 'No args'
// object를 return한다면? 괄호가 없으면 {}를 함수의 {}로 인식하기 떄문에 ()필요!
let returnObject = () => ({key:'value'})


//함수의 기본 인자
const sayHello = (name='NoName') => `hi ${name}`

sayHello('john')
sayHello()

//익명 함수 , 실제 코드에서는 잘 안쓰임, 가독성 down
function (num) { return num**3} //세제곱
num => {return num ** 0.5} // 제곱근

//익명 함수 즉시 호출
(function (num) { return num**3})(3) //3의 세제곱