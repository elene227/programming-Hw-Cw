//  1) მომხმარებელს შემოატანინეთ ასაკი შემდეგ კი დაბეჭდეთ სრულწლოვანია თუ არა


const user = Number(prompt("enter your age: "))

if(user < 18){
    console.log("user is not adult")
}else{
    console.log("user is adult")
}