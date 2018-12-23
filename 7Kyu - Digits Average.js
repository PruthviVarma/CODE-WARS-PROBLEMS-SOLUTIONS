function digitsAverage(input) {
  if (input < 10) { return input; }
  
  while (input > 9) {
    input = String(input); 
    let arr = [];
    for (let i = 0; i < input.length-1; i++) 
      arr.push(Math.round((+input[i]+ +input[i+1])/2)); 
    input = parseInt(arr.join(''));
    if (input<10) 
      return input;
  }

}
