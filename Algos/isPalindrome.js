

function decode(str){
    myStr = "";
    for(i = 0; i < str.length; i++){
        num = 0;
        if (parseInt(str[i])){
            num += str[i];
            if (parseInt(str[i+1])){
                num += str[i+1];
            }
            for(j = 0; j < num; j++){
                myStr += str[i-1]
            }
        }
    }
    return myStr;
}

console.log(decode("a3b2c4"));
console.log(decode("t2h10j4"));