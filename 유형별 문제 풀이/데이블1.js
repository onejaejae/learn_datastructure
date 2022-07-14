function solution(s) {
  const results = [];

  for (let i = 0; i < s.length; i++) {
    for (let j = 1; j < s.length + 1; j++) {
      let flag = true;
      let str = s.slice(i, j).split("");

      for (let k = 0; k < str.length; k++) {
        if (str.indexOf(str[k]) !== k) {
          flag = false;
          break;
        }
      }

      if (flag) {
        str = str.filter((v, i) => str.indexOf(v) === i);
        if (str.length > 0) {
          const joinStr = str.join("");
          if (!results.find((result) => result === joinStr)) {
            if (joinStr === "abc") {
              console.log(i, j);
            }
            results.push(joinStr);
          }
        }
      }
    }
  }
  console.log(results.length);
}

solution("abac");
