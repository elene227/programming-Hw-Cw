// მომხმარებელს შემოატანინეთ ასაკი. თუ 5-ზე ნაკლები შემოიტანა გამოიტანეთ კონსოლში 'ბაღის მოსწავლე ხარ'. 6-დან 18-მდე თუ შემოიტანა გამოიტანეთ 'სკოლის მოსწავლე ხარ'. 18-დან 19-მდე       -      '  აბიტურიენტი'; 20-დან 25-მდე სტუდენტი. დანარჩენ სხვა შემთხვევაში შეეკითხეთ თუ მუშაობს პროგრამისტად. თუ შემოიტანა მომხმარებელმა 'კი' მაშინ გამოიტანეთ 'შენ ნამდვილი ჩადი ხარ'. სხვა შემთხვევაში 'კარგია'.


let user = Number(prompt("Enter your Age: "))

if(user < 5){
    console.log('ბაღის მოსწავლე ხარ (go back to kindergarten L)')
}else if(user > 6 && user <= 18){
    console.log('სკოლის მოსწავლე ხარ')
}else if(user > 18 && user <= 19){
    console.log("აბიტურიენტი ხარ")
}else if(user > 20 && user <= 25){
    console.log("სტუდენტი ხარ.")
}else{
    const work = prompt("do you work as programmer?: ")
    if(work == 'yes'){
        console.log("you are real chad")
    }else{
        console.log("good.")
    }

}
