function solution(numStr) {
  let sum = 0;

  if (typeof numStr !== "number" && typeof numStr !== "string") {
    return 0;
  }

  if (typeof numStr === "number") {
    numStr = numStr.toString();
  }

  let numbers = numStr.split(".");
  for (let i = 0; i < numbers.length; i++) {
    numbers[i] = parseInt(numbers[i], 10);

    while (numbers[i] > 0) {
      if (i == 0) {
        sum += numbers[i] % 10;
        numbers[i] = parseInt(numbers[i] / 10, 10);
      } else {
        sum -= numbers[i] % 10;
        numbers[i] = parseInt(numbers[i] / 10, 10);
      }
    }
  }

  sum = Math.abs(sum);
  sum = sum.toString();
  console.log(typeof sum);

  numDigit = sum.length;
  console.log(numDigit);

  return sum;
}

solution("1234.56");
