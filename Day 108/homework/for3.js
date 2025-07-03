// გააკეთეთ კალკულატორი. მომხმარებელს შემოატანინეთ ოპერაციაც და 2 რიცხვიც. შემდეგ შეასრულეთ შესაბამისი მოქმედება და გამოიტანეთ კონსოლში.



let num1 = Number(prompt("Enter num: "))
let num2 = Number(prompt("Enter second number: "))


let opp = prompt("Please enter operator for numbers(+ - * ** / %): ")

if(opp == "+"){
    console.log(`${num1} + ${num2} = ${num1 + num2}`)
}else if(opp == "-"){
    console.log(`${num1} - ${num2} = ${num1 - num2}`)
}else if(opp == "*"){
    console.log(`${num1} * ${num2} = ${num1 * num2}`)
}else if(opp == "/"){
    if(num2 != 0){
        console.log(`${num1} / ${num2} = ${num1 / num2}`)
    }else{
        console.log("Cannot divide by zero")
    }
}else if(opp == "**"){
    console.log(`${num1} ** ${num2} = ${num1 ** num2}`)
}else if(opp == "%"){
     if(num2 != 0){
        console.log(`${num1} % ${num2} = ${num1 % num2}`)
    }else{
        console.log("Cannot divide by zero")
    }
} else{
    console.log("error opp not found ")
}





