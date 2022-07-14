function solution(dirs) {
  let answer = 0;
  let cnt = 0;
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  const arrays = [];
  const pos = [0, 0];

  for (let i = 0; i < dirs.length; i++) {
    switch (dirs[i]) {
      case "U":
        pos[0] += dx[0];
        pos[1] += dy[0];
        break;

      case "D":
        pos[0] += dx[1];
        pos[1] += dy[1];
        break;

      case "R":
        pos[0] += dx[2];
        pos[1] += dy[2];
        break;

      case "L":
        pos[0] += dx[3];
        pos[1] += dy[3];
        break;

      default:
        break;
    }

    for (let j = 0; j < arrays.length; j++) {
      if (JSON.stringify(arrays[j]) === JSON.stringify(pos)) {
        cnt += 1;
        break;
      }
    }

    arrays.push([pos[0], pos[1]]);
  }

  console.log(cnt);
  answer = (cnt - 1) * 2;
  return answer;
}

solution("LULLLLLLU");
